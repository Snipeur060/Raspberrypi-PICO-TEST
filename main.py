from machine import Pin, ADC
from utime import sleep
from picozero import RGBLED
import network
import urequests as requests
import time
import dht
import max7219
import uasyncio as asyncio

# Wifi cred
ssid = 'picolepetit'
password = 'PICOnotnow'
wlan = network.WLAN(network.STA_IF)

def connectme():
    global ssid, password, wlan
    wlan.active(True)
    wlan.config(pm=0xa11140)  # désactive le mode power-save
    wlan.connect(ssid, password)
    
    # Attente connexion ou erreur de connexion
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('Attente connexion...')
        sleep(1)

    # Gestion erreur de connexion
    if wlan.status() != 3:
        print('Network not active')
    else:
        print('Connexion reussie')
        status = wlan.ifconfig()
        print('ip = ' + status[0])

connectme()

print("Hello, Pi Pico!")


# Les def de pin
led = Pin(2, Pin.OUT)
rgb = RGBLED(blue=20, red=19, green=18)
ldr = ADC(27)
#Capteur temp + humidité
capteur = dht.DHT11(Pin(5))
ldv = Pin(14, Pin.OUT)  # Ajouter la LED verte
#laser
laser = Pin(15, Pin.OUT)
sound = Pin(12, Pin.IN, Pin.PULL_DOWN)  # Port internal pull-down
ledintr = Pin(22,Pin.OUT)
def blink_led(pin, times=1, delay=1):
    """Fait clignoter la LED spécifiée."""
    for _ in range(times):
        pin.on()
        sleep(delay)
        pin.off()
        sleep(delay)


#la fonction fonctionnera en même temps que le main (attention selon le hz du pico il peut galerer un peu)
async def detecterbruit():
    """
    Permet de fonctionner de manière asyncrhrone
    """
    while True:
        
        if sound.value() == 1:
            print('Intrusion')
            blink_led(ledintr,5,0.2)
        await asyncio.sleep(0.1)  # Vérifier le bruit toutes les 0.1s

async def main_loop():
    while True:
        resultdata = ldr.read_u16()
        capteur.measure()
        
        # led en fonction du resultat du capt lumi
        if resultdata < 650:
            led.off()
            rgb.color = (0, 0, 255)
        else:
            rgb.color = (0, 255, 0)
            led.on()

        if capteur.temperature() > 20:
            if wlan.status() == 3:
                #https://docs.python.org/3/library/asyncio-task.html
                await sendtemp(capteur.temperature())
                await sendtime()
                blink_led(laser, 10, 0.4)
            rgb.color = (128, 128, 0)

        await asyncio.sleep(1)  # Attendre 1 seconde avant la prochaine itération

#pourquoi en async ??
#la fonction va prendre du temps sauf que je ne veux pas que ça bloque la detection du bruit donc on le met en ascynhrone
# (idem pour sendtime)
async def sendtemp(temp):
    try:
        # Construire l'URL pour envoyer la température
        url = f"https://interaction.snipeur060.fr/settemp?temp={temp}"
        data = requests.get(url)
        data.close()
        print(f"Temperature sent: {temp}°C")
        blink_led(ldv)  # Faire clignoter la LED verte
    except Exception as e:
        print(f"Connect impossible (status = {wlan.status()}), error: {e}")

async def sendtime():
    try:
        # Obtenir l'heure actuelle
        current_time = time.localtime()
        formatted_time = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
            current_time[0], current_time[1], current_time[2], 
            current_time[3], current_time[4], current_time[5]
        )  # format qui est analysé par l'api php
        
        # Construire l'URL pour envoyer l'heure
        url = f"https://interaction.snipeur060.fr/settime?time={formatted_time}"
        data = requests.get(url)
        data.close()
        print(f"Time sent: {formatted_time}")
        blink_led(ldv)  # Faire clignoter la LED verte
    except Exception as e:
        print(f"Connect impossible (status = {wlan.status()}), error: {e}")

# Exécution asynchrone des tâches
async def main():
    asyncio.create_task(detecterbruit())  # Créer une tâche pour la détection du bruit
    await main_loop()  # Exécuter la boucle principale

# Lancer la boucle principale
asyncio.run(main())


