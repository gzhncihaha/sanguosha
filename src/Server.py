# -*- coding: utf-8 -*-  
#!/usr/local/bin/python  
  
import socket  
import sys  
import threading    
import time
from Room import * 

mainSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
ipAddr = socket.gethostbyname(socket.gethostname())
mainSocket.bind((ipAddr, 5001))
mainSocket.listen(20)
roomList = [None for i in range(100)]
threadList = [None for i in range(100)]

print("ip:"+ipAddr)

for i in range(4):
	roomList[i] = Room(host = ipAddr, port = 5002 + i, capacity = i + 2)
	threadList[i] = threading.Thread(target = roomList[i].main , args = ())
	threadList[i].start()

while 1:
	conn, addr = mainSocket.accept()
	msg = conn.recv(1024)
	temps = str(msg, encoding = "utf8").split(",")
	if temps[0] == "CreateRoom":
		roomNo = -1
		for i in range(100):
			if roomList[i] == None:
				roomNo = i
				break
			if roomList[i].havePeople == False:
				roomList[i] = None
				roomNo = i
				break
		roomList[i] = Room(host = ipAddr, port = 5002 + roomNo, capacity = int(temps[1]))
		threadList[i] = threading.Thread(target = roomList[i].main , args = ())
		threadList[i].start()
		conn.send("CreateSuccess,"+str(5002 + roomNo))

	#elif temps[0] == "InRoom":


