import network
import time
import socket

html = """
    <!DOCTYPE html>
    <html>
        <head>
           <title>Pico W - wifi_web_server_simplest</title>
        </head>
        <body>
           <h1>Pico W</h1>
           <p>wifi_web_server_simplest : {}</p>
        </body>
    </html>
"""

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = 'picolepetit'
password = 'nonono'

wlan.connect(ssid, password)

while wlan.status() != 3:
    print('waiting for connection...')
    time.sleep(1)
print(socket.getaddrinfo('0.0.0.0',80))
      
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

print("URL for this Pico W : http://{}:{}".format(wlan.ifconfig()[0], addr[-1]))

s = socket.socket()
s.bind(addr)
s.listen(1)

while True:
    try:
        client, addr = s.accept()
        request = str(client.recv(1024))
        html = "Just a single line of text"
        client.send(html)
        print(f'html sent {html}')
        client.close()

    except OSError as e:
        client.close()
