from machine import Pin
from utime import sleep
from picozero import RGBLED
import network
import urequests as requests
import time

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
        raise RuntimeError('Echec connexion')
    else:
        print('Connexion reussie')
        status = wlan.ifconfig()
        print( 'ip = ' + status[0] )
connectme()


print("Hello, Pi Pico!")

led = Pin(5, Pin.OUT)

rgb = RGBLED(blue = 20, red = 19, green = 18)

ldr = machine.ADC(27)



while True:
    resultdata = ldr.read_u16()
    if resultdata < 650:
        led.off()
        rgb.color = (0, 0, 255)
    else:
        rgb.color = (0, 255, 0)
        led.on()
    sleep(0.5)
  
