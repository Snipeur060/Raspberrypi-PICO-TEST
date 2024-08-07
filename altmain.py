from machine import Pin
from utime import sleep
from picozero import RGBLED
import network
import urequests as requests
import time
import dht
import array
import rp2
#https://core-electronics.com.au/guides/how-to-use-ws2812b-rgb-leds-with-raspberry-pi-pico/

NUM_LEDS = 64
PIN_NUM = 20
brightness = 0.7

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()


# Create the StateMachine with the ws2812 program, outputting on pin
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))

# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)

# Display a pattern on the LEDs via an array of LED RGB values.
ar = array.array("I", [0 for _ in range(NUM_LEDS)])

##########################################################################
def pixels_show():
    dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
    for i,c in enumerate(ar):
        r = int(((c >> 8) & 0xFF) * brightness)
        g = int(((c >> 16) & 0xFF) * brightness)
        b = int((c & 0xFF) * brightness)
        dimmer_ar[i] = (g<<16) + (r<<8) + b
    sm.put(dimmer_ar, 8)
    time.sleep_ms(10)

def pixels_set(i, color):
    ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]

def pixels_fill(color):
    for i in range(len(ar)):
        pixels_set(i, color)

def color_chase(color, wait):
    for i in range(NUM_LEDS):
        pixels_set(i, color)
        time.sleep(wait)
        pixels_show()
    time.sleep(0.2)
 
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)
 
 
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(NUM_LEDS):
            rc_index = (i * 256 // NUM_LEDS) + j
            pixels_set(i, wheel(rc_index & 255))
        pixels_show()
        time.sleep(wait)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)

print("fills")
for color in COLORS:       
    pixels_fill(color)
    pixels_show()
    time.sleep(0.2)

print("chases")
for color in COLORS:       
    color_chase(color, 0.01)

print("rainbow")
rainbow_cycle(0)

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
  
