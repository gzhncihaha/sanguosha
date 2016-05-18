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

while 1:
	
	room = Room(host="192.168.1.107", port=5001, capacity=2)
	numPlayer = 0
	while 1:
		conn, addr = room.socket.accept() 
		print ('Connected with ' + addr[0] + ':' + str(addr[1]))
		numPlayer += 1
		nick = conn.recv(1024)
		nick = str(nick, encoding = "utf8")
		while (nick.split(",")[0] != "UserName"):
			nick = conn.recv(1024)
		room.addPlayer(RoomPlayer(conn=conn, username=nick.split(",")[1], No=str(numPlayer)))
		if room.full():
			break

	room.main()

