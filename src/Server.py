# -*- coding: utf-8 -*-  
#!/usr/local/bin/python  
  
import socket  
import sys  
import threading    
import time
from Room import * 
  			  
numPlayer = 0
room = Room(host="192.168.19.1", port=5001, capacity=2)

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








while 1:  
	conn, addr = s.accept()  
	numPlayer += 1
	print ('Connected with ' + addr[0] + ':' + str(addr[1])  )

	threading.Thread(target = clientThreadIn , args = (conn, numPlayer)).start()#开辟线程  
	threading.Thread(target = ClientThreadOut , args = (conn, numPlayer)).start()  
	time.sleep(5)
	if numPlayer == 2:
		deck = Deck()

		NotifyAll("SelectHero,3,13")
		time.sleep(0.2)
		NotifyAll("SelectHero,4,3")
		time.sleep(0.2)
		NotifyAll("SelectHero,5,8")
		time.sleep(0.2)
		NotifyAll("roundstart,1")
		time.sleep(0.2)

		#break
s.close()  
