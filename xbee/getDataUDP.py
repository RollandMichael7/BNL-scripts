import os
import time
import threading
from socket import *

def recvLoop():
	addr = ("", 13000)
	recvSize = 1024
	UDPSock = socket(AF_INET, SOCK_DGRAM)
	UDPSock.bind(addr)
	while True:
	    (data, addr) = UDPSock.recvfrom(recvSize)
	    data = data.decode('utf-8')
	    print("Received message: " + data)

def sendLoop():
	UDPSock = socket(AF_INET, SOCK_DGRAM)
	addr= ("10.10.192.18", 13000)
	while True:
		data = input("Enter data to send: ")
		UDPSock.sendto(str.encode(data), addr)
		time.sleep(5)

threading.Thread(target=sendLoop).start()
recvLoop()