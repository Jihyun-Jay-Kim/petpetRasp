import socket
import time
import serial
import bluetooth

time.sleep(10)

bluetoothFromArduino = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1
bluetoothFromArduino.connect(("98:D3:71:FD:3B:DF",port))
#bluetoothFromArduino.listen(1)
#blue = bluetoothFromArduino.accept()
print("connect with : ")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.1.27', 5555))
server_socket.listen(0)
client_socket, addr = server_socket.accept()
print("connect with : ", addr)
info = 0
while True:
        data=client_socket.recv(65535)
        dataDe = data.decode()
        if dataDe == "hand":
            send = 'h'
            bluetoothFromArduino.send(send)
            bluetoothFromArduino.close()
        if dataDe == "end":
            bluetoothFromArduino = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            bluetoothFromArduino.connect(("98:D3:71:FD:3B:DF",port))
        if dataDe == "auto":
            send = 'a'
            bluetoothFromArduino.send(send)
        if dataDe == "info":
            send = 'i'
            bluetoothFromArduino.send(send)
            info = (bluetoothFromArduino.recv(1024))
            info = (bluetoothFromArduino.recv(1024))
            print(info)
            client_socket.sendall(bytes(info))
        if not data: break
        print("recv data : ", dataDe)
client_socket.close()
 
