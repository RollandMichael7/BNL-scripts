import os
import time
import threading
from socket import *

# def recvLoop():
# 	addr = ("", 13000)
# 	recvSize = 1024
# 	UDPSock = socket(AF_INET, SOCK_STREAM)
# 	UDPSock.bind(addr)
# 	while True:
# 	    (data, addr) = UDPSock.recvfrom(recvSize)
# 	    data = data.decode('utf-8')
# 	    print("Received message: " + data)

def sendLoop():
	host = "10.10.192.18"
	port = 13000
	TCPSock = socket(AF_INET, SOCK_STREAM)
	TCPSock.connect((host, port))
	try:
		while True:
			data = input("Enter data to send: ")
			TCPSock.sendall(str.encode(data))
			data = TCPSock.recv(1024)
			print("Received: " + data.decode('utf-8'))
	except KeyboardInterrupt:
		TCPSock.close()
sendLoop()