from machine import Pin
from utime import sleep
from picozero import RGBLED
import network
import urequests as requests
import time
import dht


# Wi-Fi credentials
ssid = 'picolepetit'
password = 'PICOnotnow'
wlan = network.WLAN(network.STA_IF)


def connectme():
    global ssid,password,wlan
    wlan.active(True)
    wlan.config(pm = 0xa11140)              # désactive le mode power-save
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
        print( 'ip = ' + status[0] )
connectme()


print("Hello, Pi Pico!")

led = Pin(2, Pin.OUT)

rgb = RGBLED(blue = 20, red = 19, green = 18)

ldr = machine.ADC(27)

capteur = dht.DHT11(Pin(5))

def sendtemp(temp):
    try:
        url = f"https://interaction.snipeur060.fr/settemp?temp={temp}"
        data=requests.get(url)
        data.close()
        print(f"temp ok {temp}")

    except:
        print("could not connect (status =" + str(wlan.status()) + ")")



while True:

    resultdata = ldr.read_u16()
    capteur.measure()
    if resultdata < 650:
        led.off()
        rgb.color = (0, 0, 255)
    else:
        rgb.color = (0, 255, 0)
        led.on()
        
        
    if capteur.temperature() > 20:
        sendtemp(capteur.temperature())
        rgb.color = (255, 128, 0)
    sleep(1)
  
