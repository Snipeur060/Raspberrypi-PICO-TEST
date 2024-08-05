from machine import Pin
from utime import sleep
from picozero import RGBLED
import network
import socket
import time

# Wi-Fi credentials
ssid = 'picolepetit'
password = 'PICOnotnow'


# HTML template for the webpage
def webpage(random_value, state):
    html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Pico Web Server</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body>
            <h1>Raspberry Pi Pico Web Server</h1>
            <h2>Led Control</h2>
            <form action="./test">
                <input type="submit" value="Test" />
            </form>
            <br>
            <p>LED state: {state}</p>
        </body>
        </html>
        """
    return str(html)

# Connect to WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for Wi-Fi connection
connection_timeout = 10
while connection_timeout > 0:
    if wlan.status() >= 3:
        break
    connection_timeout -= 1
    print('Waiting for Wi-Fi connection...')
    time.sleep(1)

# Check if connection is successful
if wlan.status() != 3:
    raise RuntimeError('Failed to establish a network connection')
else:
    print('Connection successful!')
    network_info = wlan.ifconfig()
    print('IP address:', network_info[0])


# Set up socket and start listening
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen()

print('Listening on', addr)

print("Hello, Pi Pico!")

led = Pin(5, Pin.OUT)

rgb = RGBLED(blue = 20, red = 19, green = 18)

ldr = machine.ADC(27)



while True:
    try:
        conn, addr = s.accept()
        print('Got a connection from', addr)
        request = conn.recv(1024)
        request = str(request)
        print('Request content = %s' % request)
        conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        conn.send(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('Connection closed')
    resultdata = ldr.read_u16()
    if resultdata < 650:
        led.off()
        rgb.color = (0, 0, 255)
    else:
        rgb.color = (0, 255, 0)
        led.on()
    sleep(0.5)
  
