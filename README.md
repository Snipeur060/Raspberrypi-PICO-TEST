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
