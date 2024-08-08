import neopixel
from machine import Pin
import time

ws_pin = 0
led_num = 64
BRIGHTNESS = 0.2 

neoRing = neopixel.NeoPixel(Pin(ws_pin), led_num)

def set_brightness(color):
    r, g, b = color
    r = int(r * BRIGHTNESS)
    g = int(g * BRIGHTNESS)
    b = int(b * BRIGHTNESS)
    return (r, g, b)

while True:
    color = (255, 0, 0)  
    color = set_brightness(color)
    neoRing.fill(color)
    neoRing.write()
    time.sleep(1)


    color = (0, 255, 0)
    color = set_brightness(color)
    neoRing.fill(color)
    neoRing.write()
    time.sleep(1)

    # Display blue
    color = (0, 0, 255)  # Blue color
    color = set_brightness(color)
    neoRing.fill(color)
    neoRing.write()
    time.sleep(1)
