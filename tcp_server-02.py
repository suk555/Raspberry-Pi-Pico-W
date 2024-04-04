import network
import usocket as socket
from machine import Pin

# 네트워크 인터페이스 설정
wlan = network.WLAN(network.STA_IF)
wlan.active(True)  # WiFi 활성화
wlan.connect('SK_WiFiGIGA83E4', '1903001744')  # WiFi에 연결

# IP 획득 및 커텍트 확인
while wlan.isconnected() == False:
    print('Waiting for connection...')
    sleep(1)
ip = wlan.ifconfig()[0]
port = 8080
print(f'Connected on telnet {ip}:{port}')

# 핀 설정
# led_pin = Pin(25, Pin.OUT)  # GPIO 25번 핀을 출력으로 설정 (내장 LED)
led_pin = Pin('LED', Pin.OUT)

# 서버 설정
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8080))
server_socket.listen(1)  # 최대 연결 수

print('Waiting for connection...')

# 연결 대기 및 데이터 수신
while True:
    conn, addr = server_socket.accept()  # 클라이언트 연결 수락
    print('Connected to', addr)

    # 클라이언트로부터 데이터 수신 및 핀 제어
    while True:
        data = conn.recv(1024)  # 클라이언트로부터 데이터 수신
        if not data:
            break  # 데이터가 없으면 연결 종료
        message = data.decode().strip().lower()  # 수신한 데이터를 소문자로 변환
        print('Received:', message)
        
        # 받은 메시지에 따라 LED를 켜거나 끕니다.
        if message == 'on':
            led_pin.value(1)  # LED 켜기
            conn.sendall(b'LED is on\n')
            state = "ON"
        elif message == 'off':
            led_pin.value(0)  # LED 끄기
            conn.sendall(b'LED is off\n')
            state = 'OFF'
        elif message == 'msg':
            msg = input('Hellow My Name is raspberry ip pico w')
            conn.send(msg.encode())
        elif message == 'quit':
            conn.close()
        else:
            conn.sendall(b'Unknown command\n')

    conn.close() 