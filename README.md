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
