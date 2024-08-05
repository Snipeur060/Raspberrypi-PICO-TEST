from machine import Pin
from utime import sleep


print("Hello, Pi Pico!")

led = Pin(5, Pin.OUT)
ldr = machine.ADC(27)
while True:
    resultdata = ldr.read_u16()
    print(resultdata)
    if resultdata < 650:
        led.off()
    else:
        led.on()
    sleep(0.5)
  

 
