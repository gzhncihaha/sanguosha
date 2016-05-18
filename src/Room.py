import socket  
import sys  
import threading    
import time
from Deck import *
from BuildCards import *	
from random import *

#inStringList = []
#data = ''
#con = threading.Condition()  
#
#
#def ClientThreadIn(conn, username):#开辟线程  
#	global inStringList  
#	while True:
#		try:  
#			temp = conn.recv(1024)  
#			print("server recv:"+str(temp, encoding = "utf8"))
#			inStringList.append(str(temp, encoding = "utf8"))
#		except:  
#
#			NotifyAll(username + " leaves the room!")  
#			return  
#
#def NotifyAll(sss):#广播  
#	global data  
#	if con.acquire():  
		#
#		data = sss  
#		print("server send:"+data)
#		con.notifyAll()  
#		con.release()  
#
#def ClientThreadOut(conn): 
#	global data  
#	while True:  
#		if con.acquire():  
#			con.wait()  
#			if data:  
#				try:  
#					conn.sendall(bytes(data, encoding="utf-8"))  
#					con.release()  
#				except:  
#					con.release()  
#					return  

class Room:
	def __init__(self, host, port, capacity):
		self.players = []
		self.host = host
		self.port = port
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		self.socket.bind((self.host, self.port))
		self.socket.listen(20)
		self.capacity = capacity
		self.recvStrList = ''
		self.allIn = False
		self.isReady = [False for i in range(self.capacity)]
		self.heroSelected = [False for i in range(50)]
		self.choosedHero = [False for i in range(10)]
		self.deck = Deck()
		self.nowRoundPlayer = "1"
		self.trickStack = ["" for i in range(10)]
		self.trickPointer = 0
		self.trickList = []
		self.havePeople = True
		self.playerNum = 0

		self.inStringList = []
		self.data = ''
		self.con = threading.Condition()  
	
	
	def ClientThreadIn(self, conn, username):#开辟线程  
		#global inStringList  
		while True:
			try:  
				temp = conn.recv(1024)  
				print("server recv:"+str(temp, encoding = "utf8"))
				self.inStringList.append(str(temp, encoding = "utf8"))
			except:  
				self.playerNum -= 1
				if self.playerNum == 0:
					self.havePeople = False
				self.NotifyAll(username + " leaves the room!")  
				return  
	
	def NotifyAll(self, sss):#广播  
		#global data  
		if self.con.acquire():  
			
			self.data = sss  
			print("server send:"+self.data)
			self.con.notifyAll()  
			self.con.release()  
	
	def ClientThreadOut(self, conn): 
		#global data  
		while True:  
			if self.con.acquire():  
				self.con.wait()  
				if self.data:  
					try:  
						conn.sendall(bytes(self.data, encoding="utf-8"))  
						self.con.release()  
					except:  
						self.con.release()  
						return  

	def addPlayer(self, rp):
		self.players.append(rp)
		if int(rp.prepareNo) == self.capacity:
			self.allIn = True
		self.playerNum += 1
		threading.Thread(target = self.ClientThreadIn , args = (rp.conn, rp.username)).start()
		threading.Thread(target = self.ClientThreadOut , args = (rp.conn,)).start()  

	def full(self):
		return self.allIn

	def recvData(self):
		#global inStringList
		self.recvStrList = self.inStringList
		self.inStringList = []

	def sendData(self, s, pausetime):
		self.NotifyAll(s)
		time.sleep(pausetime)

	def nextPlayer(self, s):
		n = int(s)
		n = n % self.capacity + 1
		return str(n)

	def allReady(self):
		for i in range(self.capacity):
			if self.isReady[i] == False:
				return False
		return True

	def selectHeroList(self, lord):
		temps = ''
		if lord:
			self.heroSelected[1] = True
			self.heroSelected[8] = True
			self.heroSelected[15] = True
			temps = temps + ',1,8,15'
			for i in range(2):
				j = -1
				while (j == -1):
					k = randint(1, 25)
					if self.heroSelected[k] == False:
						j = k
						self.heroSelected[k] = True
				temps = temps + ',' + str(j)
		else:
			for i in range(5):
				j = -1
				while (j == -1):
					k = randint(1, 25)
					if self.heroSelected[k] == False:
						j = k
						self.heroSelected[k] = True
				temps = temps + ',' + str(j)
		return temps

	def setRoomSize(self):
		self.sendData("SetRoomSize,"+str(self.capacity), 0.2)

	def setNo(self):
		number = randint(1, self.capacity)
		for rp in self.players:
			if rp.prepareNo == str(number):
				rp.playNo = '1'
				self.sendData("SetPlayNumber,"+rp.username+",1", 0.2)
				break

		nlst = self.getNoList(self.capacity)
		nlst = self.randList(nlst)
		i = 0
		for rp in self.players:
			if rp.playNo != '1':
				rp.playNo = nlst[i]
				self.sendData("SetPlayNumber,"+rp.username+","+rp.playNo, 0.2)
				i += 1

	def chooseLord(self):
		for rp in self.players:
			if rp.playNo == '1':
				rp.identity = 'lord'
				self.sendData("SetLord,"+rp.playNo, 0.2)
				break

	def lordSelectHero(self):
		self.sendData("SelectHero,1" + self.selectHeroList(True), 0.2)

	def getNoList(self, size):
		if size == 2:
			return ['2']
		elif size == 3:
			return ['2','3']
		elif size == 4:
			return ['2','3','4']
		elif size == 5:
			return ['2','3','4','5']

	def getRoleList(self, size):
		if size == 2:
			return ['rebel']
		elif size == 3:
			return ['rebel', 'renegade']
		elif size == 4:
			return ['rebel', 'renegade', 'loyalist']
		elif size == 5:
			return ['rebel', 'renegade', 'loyalist', 'rebel']

	def randList(self, lst):
		l = len(lst)
		for i in range(l*l):
			j = randint(0, l-1)
			k = randint(0, l-1)
			temp = lst[j]
			lst[j] = lst[k]
			lst[k] = temp		
		return lst

	def chooseOther(self):
		rlst = self.getRoleList(self.capacity)
		rlst = self.randList(rlst)
		i = 0
		for rp in self.players:
			if rp.playNo != '1':
				rp.identity = rlst[i]
				self.sendData("SetIdentity,"+rp.playNo+","+rp.identity, 0.2)
				i += 1

	def otherSelectHero(self):
		nlst = self.getNoList(self.capacity)
		for n in nlst:
			self.sendData("SelectHero," + str(n) + self.selectHeroList(False), 0.2)

	def handleReady(self, s):
		playerid = ''
		for rp in self.players:
			if rp.username == s[1]:
				playerid = int(rp.prepareNo) - 1
		self.isReady[playerid] = True

		if self.allReady():
			self.setRoomSize()
			self.setNo()
			self.chooseLord()
			self.chooseOther()
			self.lordSelectHero()

	def allChoosedHero(self):
		for i in range(self.capacity):
			if self.choosedHero[i+1] == False:
				return False
		return True
	def sendAllInitialCard(self):
		for i in range(self.capacity):
			self.sendData("SendCards,No,"+str(i+1)+",4"+self.deck.draw(4), 0.2)
		self.sendData("SendCards,No,1,3,73,98,98", 0.2)
		self.sendData("SendCards,No,2,3,72,99,99", 0.2)
	def handleChooseHero(self, s):
		self.sendData("ChoosedHero,"+s[1]+","+s[2], 0.2)
		self.choosedHero[int(s[1])] = True
		print(self.choosedHero)
		if s[1] == '1':
			self.otherSelectHero()
		if self.allChoosedHero():
			self.sendAllInitialCard()
			self.sendData("RoundStart,1", 0.2)
			self.nowRoundPlayer = "1"

	def handleRoundStartOver(self, s):
		self.sendData("Start,"+s[1], 0.2)

	def handleStartOver(self, s):
		self.sendData("Judge,"+s[1], 0.2)

	def handleJudgeOver(self, s):
		self.sendData("Draw,"+s[1], 0.2)

	def handleDrawOk(self, s):
		self.sendData("SendCards,Draw,"+s[1]+",2"+self.deck.draw(2), 0.2)

	def handleDrawOver(self, s):
		self.sendData("Play,"+s[1], 0.2)

	def showCardsAmazingGrace(self):
		self.sendData("ShowCards,Grace,"+str(self.capacity)+self.deck.draw(self.capacity), 0.2)

	def showCardsAmazingGraceOff(self):
		self.sendData("ShowCardsOff,Grace,"+str(self.capacity)+self.deck.draw(self.capacity), 0.2)

	def askNullificationFliter(self, s):
		self.sendData(s, 0.2)

	def finishNullification(self):
		if self.trickPointer % 2 == 1:
			self.sendData("TrickEffect"+self.trickStack[0], 0.2)
		else:
			self.handleTrickEffectOver("")

	def handleApply(self, s):
		targetNum = getCardsTargetNum(s[2])
		isImmediate = getCardsIsImmediate(s[2])
		if isImmediate:
			if targetNum == 0:
				self.sendData("Effect,"+s[1]+","+s[2], 0.2)
				self.sendData("Play,"+self.nowRoundPlayer, 0.2)
				self.sendData("DecreaseCard,"+s[1]+",1", 0.2)
			elif targetNum == 1:
				self.sendData("Effect,"+s[1]+","+s[2]+","+s[3], 0.2)
				self.sendData("Play,"+self.nowRoundPlayer, 0.2)
				self.sendData("DecreaseCard,"+s[1]+",1", 0.2)
			elif targetNum == 2:
				self.sendData("Effect,"+s[1]+","+s[2]+","+s[3]+","+s[4], 0.2)
				self.sendData("Play,"+self.nowRoundPlayer, 0.2)
				self.sendData("DecreaseCard,"+s[1]+",1", 0.2)
		card = iCard[int(s[2])]
		if card.name == "slash":
			self.sendData("Slash,"+s[1]+","+s[2]+","+s[3], 0.2)
			self.sendData("DecreaseCard,"+s[1]+",1", 0.2)
		elif card.basetype == "trick":
			if card.subtype == "single":
				temp = ""
				stemp = self.nowRoundPlayer
				if targetNum == 0:
					temp = ","+s[1]+","+s[2]
					self.askNullificationFliter("AskNullification,"+stemp+","+s[1]+","+s[2])
				elif targetNum == 1:
					temp = ","+s[1]+","+s[2]+","+s[3]
					self.askNullificationFliter("AskNullification,"+stemp+","+s[3]+","+s[2]+","+s[1])
				elif targetNum == 2:
					temp = ","+s[1]+","+s[2]+","+s[3]+","+s[4]
					self.askNullificationFliter("AskNullification,"+stemp+","+s[3]+","+s[2]+","+s[1]+","+s[4])
				self.trickStack[self.trickPointer] = temp
				self.trickPointer += 1
				self.sendData("DecreaseCard,"+s[1]+",1", 0.2)
			elif card.subtype == "global":
				if card.name == "amazing_grace":
					self.showCardsAmazingGrace()
				tempNo = self.nowRoundPlayer
				tempNo = str(int(tempNo) % self.capacity + 1)
				self.trickList = []
				while tempNo != self.nowRoundPlayer:
					temp = ","+tempNo+","+s[2]+","+s[1]
					self.trickList.append(temp)
					tempNo = str(int(tempNo) % self.capacity + 1)

				temp = ","+s[1]+","+s[2]+","+s[1]
				stemp = self.nowRoundPlayer
				self.askNullificationFliter("AskNullification,"+stemp+","+s[1]+","+s[2]+","+s[1])
				self.trickStack[self.trickPointer] = temp
				self.trickPointer += 1
				self.sendData("DecreaseCard,"+s[1]+",1", 0.2)

	def handleJink(self, s):
		self.sendData("SlashJinked,"+s[2]+","+s[1]+","+s[3]+","+s[4], 0.2)

	def handleNotJink(self, s):
		self.sendData("SlashDamage,"+s[2]+","+s[1]+","+s[3], 0.2)

	def handleNotAppendSlash(self, s):
		self.sendData("Play,"+self.nowRoundPlayer, 0.2)

	def handleNotLaunchAfterBeDamage(self, s):
		self.sendData("Play,"+self.nowRoundPlayer, 0.2)

	def handleNotUseNullification(self, s):
		stemp = self.nextPlayer(s[1])
		if (stemp == self.nowRoundPlayer):
			self.finishNullification()
		else:
			self.askNullificationFliter("AskNullification,"+stemp+self.trickStack[self.trickPointer-1])

	def handleTrickEffectOver(self, s):
		if self.trickList == []:
			card = copy.copy(bCards[int(self.trickStack[0].split(",")[2]) - 1])
			if card.name == "amazing_grace":
				self.showCardsAmazingGraceOff()
			self.trickPointer = 0
			self.sendData("Play,"+self.nowRoundPlayer, 0.2)
		else:
			self.trickPointer = 0
			temp = self.trickList[0]
			del self.trickList[0]

			ss = temp.split(",")

			stemp = self.nowRoundPlayer
			self.askNullificationFliter("AskNullification,"+stemp+temp)
			self.trickStack[self.trickPointer] = temp
			self.trickPointer += 1
			

	def handleAskCards(self, s):
		self.sendData("SendCards,Ex,"+s[1]+","+s[2]+self.deck.draw(int(s[2])), 0.2)

	def haneleChooseCard(self, s):
		self.sendData("SendCards,Grace,"+s[1]+",1,"+s[2], 0.2)

	def handlePlayOver(self, s):
		if s[2] == "NotDiscard":
			nextPlayer = self.nextPlayer(s[1])
			self.sendData("RoundStart,"+nextPlayer, 0.2)
			self.nowRoundPlayer = nextPlayer
		else:
			self.sendData("Discard,"+s[1], 0.2)

	def handleThrow(self, s):
		self.sendData("DecreaseCard,"+s[1]+","+s[2], 0.2)
		nextPlayer = self.nextPlayer(s[1])
		self.sendData("RoundStart,"+nextPlayer, 0.2)
		self.nowRoundPlayer = nextPlayer

	def handleRecv(self):
		for s in self.recvStrList:
			tempStr = s.split(",")
			if tempStr[0] == "Ready":
				self.handleReady(tempStr)
			elif tempStr[0] == "ChooseHero":
				self.handleChooseHero(tempStr)
			elif tempStr[0] == "RoundStartOver":
				self.handleRoundStartOver(tempStr)
			elif tempStr[0] == "StartOver":
				self.handleStartOver(tempStr)
			elif tempStr[0] == "JudgeOver":
				self.handleJudgeOver(tempStr)
			elif tempStr[0] == "DrawOk":
				self.handleDrawOk(tempStr)
			elif tempStr[0] == "DrawOver":
				self.handleDrawOver(tempStr)
			elif tempStr[0] == "Apply":
				self.handleApply(tempStr)
			elif tempStr[0] == "Jink":
				self.handleJink(tempStr)
			elif tempStr[0] == "NotJink":
				self.handleNotJink(tempStr)
			elif tempStr[0] == "NotAppendSlash":
				self.handleNotAppendSlash(tempStr)
			elif tempStr[0] == "NotLaunchAfterBeDamage":
				self.handleNotLaunchAfterBeDamage(tempStr)
			elif tempStr[0] == "NotUseNullification":
				self.handleNotUseNullification(tempStr)
			elif tempStr[0] == "TrickEffectOver":
				self.handleTrickEffectOver(tempStr)
			elif tempStr[0] == "AskCards":
				self.handleAskCards(tempStr)
			elif tempStr[0] == "ChooseCard":
				self.haneleChooseCard(tempStr)
			elif tempStr[0] == "PlayOver":
				self.handlePlayOver(tempStr)
			elif tempStr[0] == "Throw":
				self.handleThrow(tempStr)

	def main(self):
		numPlayer = 0
		while 1:
			conn, addr = self.socket.accept() 
			print ('Connected with ' + addr[0] + ':' + str(addr[1]))
			numPlayer += 1
			nick = conn.recv(1024)
			nick = str(nick, encoding = "utf8")
			while (nick.split(",")[0] != "UserName"):
				nick = conn.recv(1024)
			self.addPlayer(RoomPlayer(conn=conn, username=nick.split(",")[1], No=str(numPlayer)))
			if self.full():
				break

		while self.havePeople:
			self.recvData()
			self.handleRecv()
			#self.update()

class RoomPlayer:
	def __init__(self, conn, username, No):
		self.conn = conn
		self.username = username
		self.prepareNo = No
		self.ready = False
		self.identity = ''
		self.playNo = ''


		
