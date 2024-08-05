from machine import Pin
from utime import sleep
from picozero import RGBLED


print("Hello, Pi Pico!")

led = Pin(5, Pin.OUT)

rgb = RGBLED(blue = 20, red = 19, green = 18)

ldr = machine.ADC(27)

rgb.color = (0, 0, 0)

while True:
    resultdata = ldr.read_u16()
    print(resultdata)
    if resultdata < 650:
        led.off()
    else:
        led.on()
    sleep(0.5)
