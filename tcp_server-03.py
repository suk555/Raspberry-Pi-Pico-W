import network
import socket

# Wi-Fi 연결 설정
WIFI_SSID = 'SK_WiFiGIGA83E4'
WIFI_PASSWORD = '1903001744'
IP_ADDRESS = '192.168.35.222'  # 고정 IP 주소 설정
SUBNET_MASK = '255.255.255.0'
GATEWAY = '192.168.35.1'

# Wi-Fi 모듈 초기화
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

# 고정 IP 주소 설정
wifi.ifconfig((IP_ADDRESS, SUBNET_MASK, GATEWAY, '8.8.8.8'))

# TCP 서버 설정
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP_ADDRESS, 8080))  # 포트 8080으로 바인딩
server_socket.listen(5)  # 최대 5개의 연결 대기

print("Server started at", IP_ADDRESS)

while True:
    client_socket, addr = server_socket.accept()
    print('Client connected from', addr)
    client_socket.sendall("Welcome to Server\n".encode())
    client_socket.sendall("Please Input TXT!\n".encode())
    
    while True:
        # 클라이언트로부터 데이터 수신
        data = client_socket.recv(1024)
        data = data.strip()
        
        print("Received:", data.decode())
        
        if data == 'quit':
            client_socket.close()
