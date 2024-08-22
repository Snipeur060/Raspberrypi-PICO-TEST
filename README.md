## TEST 1

Tentative pour se connecter avec Thonny sur le pico

<a href="https://github.com/Snipeur060/Raspberrypi-PICO-TEST/blob/main/thonnyerr.png" target="_blank">Thonny error</a>

17h54 Tentative pour réinstaller MicroPython


18h00 ![image](https://github.com/user-attachments/assets/ea177032-adc2-445f-9e07-084c2de4a25e)



J'essaie de faire briller la led (onboard led) sans succès



Le raspberry pico W ne foncitonne pas avec le pin 25
```py

from machine import * 
import utime
 
led = Pin('LED', Pin.OUT)

 
while True:
    led.value(1)
    utime.sleep(1)
    led.value(0)
    utime.sleep(1)

```

![image](https://github.com/user-attachments/assets/e4196496-ad98-46b2-ae3d-71d77e5c5960)



Allumer une LED 🥳✅


Tentative Pour récuperer la luminosité avec un capteur de lumière


Ajout du capteur de luminosité

```py
from machine import Pin
from utime import sleep

print("Hello, Pi Pico!")

led = Pin(5, Pin.OUT)
ldr = machine.ADC(27)
while True:
  led.toggle()
  print(ldr.read_u16())
  sleep(0.5)
```
![IMG_20240805_182026](https://github.com/user-attachments/assets/9d4f4fec-33ff-4416-8911-a44f0368b3ee)

Dans la console:
![image](https://github.com/user-attachments/assets/1ce9c4a8-8284-455d-95a1-52be06e2900a)


Try to fix neopixel error 
https://github.com/blaz-r/pi_pico_neopixel/issues/7

Abandon du neopixel 

https://wokwi.com/projects/405403990069658625

Tout est dans https://github.com/Snipeur060/Raspberrypi-PICO-TEST/blob/main/main.py

## On avance

Mise en place d'un système de couleur qui permet de savoir si on approche ou non de la nuit ou du jour

![IMG_20240805_204849](https://github.com/user-attachments/assets/bcf1d031-3005-475d-abd2-7f154b00a64d)



Ajout du capteur de temperature et implementation de l'api PHP avec la page web

Lien de la démo 🚀:  https://interaction.snipeur060.fr/



Retour du neopixel et encore un echec rien ne s'allume
![image](https://github.com/user-attachments/assets/e7689330-a85a-442d-b5af-efa8af231689)

![IMG_20240805_221315](https://github.com/user-attachments/assets/e37332f3-7a92-40c1-bee8-e7d45d2348e5)

Essayer de créer sa propre carte pour des led et une antenne
![image](https://github.com/user-attachments/assets/523fe6d5-506d-4bad-aa79-e0bf2f6f96a0)

Ajout d'une led pour visualiser l'envoie de data
![IMG_20240809_225353](https://github.com/user-attachments/assets/32b7d3ec-b09c-4ff9-87eb-80ef08ad7f6e)


Ajout d'un laser
![image](https://github.com/user-attachments/assets/b801eea6-f78a-43b4-9ac2-bc3b25308fc8)


On installe la lib Rpi.GPIO
![image](https://github.com/user-attachments/assets/c1c23598-354d-4e26-9c63-3441db83fb94)

C'est pour Cpython pas micropython mdr

Ajout du capteur de bruit + la led Système anti intrusion 
![image](https://github.com/user-attachments/assets/96be425f-bc7d-4771-b37f-8a4438d988c6)


On réecrie le code en asynchrone
https://jacobpadilla.com/articles/recreating-asyncio
https://docs.python.org/3/library/asyncio-task.html


https://wokwi.com/projects/406945266078910465

![image](https://github.com/user-attachments/assets/54b93dea-ec75-4930-a66c-3cd4ce56de9a)

