import network
import usocket as socket
from machine import Pin

# Configure your network settings
SSID = "SK_WiFiGIGA83E4"
PASSWORD = "1903001744"

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while wlan.isconnected() == False:
    print('Waiting for connection...')
    sleep(1)
ip = wlan.ifconfig()[0]
port = 5555
print(f'Connected on telnet {ip}:{port}')

# Wait until connected to WiFi
while not wlan.isconnected():
    pass

print("Connected to WiFi")
print("UDP server listening on {}:{}".format(ip, port))

led_pin = Pin('LED', Pin.OUT)

# Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address and port
server_address = (ip, port)
udp_socket.bind(server_address)

# Start listening for incoming UDP packets
while True:
    try:
        data, client_address = udp_socket.recvfrom(1024)  # 1024 is the buffer size
        print("Received message from {}: {}".format(client_address, data))
        if not data:
            break  # 데이터가 없으면 연결 종료
        message = data.decode().strip().lower()  # 수신한 데이터를 소문자로 변환
        print('Received:', message)
        
        if message == 'on':
            led_pin.value(1)  # LED 켜기
            udp_socket.sendall(b'LED is on')
            state = "ON"
        elif message == 'off':
            led_pin.value(0)  # LED 끄기
            udp_socket.sendall(b'LED is off')
            state = 'OFF'
        elif message == 'msg':
            msg = input('Hellow My Name is raspberry ip pico w')
            udp_socket.send(msg.encode())
        else:
            udp_socket.sendall(b'Unknown command')
        break
    except NotImplementedError:
        print("Oops! Try Again")
        break
    except OSError:
        print("Oops! Try Again")
        break
    udp_socket.close()