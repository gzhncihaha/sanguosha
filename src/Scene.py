import pygame
from pygame.locals import *
from ProgramEvent import *
from Button import *
from ToServer import *
from Player import *
from OtherPlayer import *
from TipHandler import *
from Screen import *
from HeroSelecter import * 
from CardSelecter import * 
from BuildCards import *
import copy
import time
import sys

class Scene_Base:
	def main(self):
		self.clock = pygame.time.Clock()
		self.refreshtime = 0
		self.refreshtimes = 0
		self.fps = 0
		self.start()
		self.update()
		while True:
			self.refresh()
			self.update()
			if self.scene_now != self.scene_temp:break
		return self.scene_now
	def start(self):
		pass
	def update(self):
		pass
	def refresh(self):
		pass
class Scene_Title(Scene_Base):
	def __init__(self):		
		self.buttons = Buttons()
		self.scene_temp = self
		self.scene_now = self
		self.background = pygame.image.load('..\\res\\image\\backdrop\\background.jpg').convert_alpha()
		self.background = pygame.transform.scale(self.background, (1280,720))
		self.sendData("UserName," + communicater.nick)

	def start(self):
		self.createButton()
		
	def update(self):
		inputs.update()
		self.screenUpdate()
		self.buttons.update()
		self.handleButtonEvents()

	def refresh(self):
		screen.blit(self.background, (0,0))
		self.buttons.draw()
		pygame.display.update()

	def screenUpdate(self):
		pass
		#if self.input.newkeys[K_1]:
		#	self.screen = pygame.display.set_mode((1280, 720), FULLSCREEN, 32)
		#if self.input.newkeys[K_2]:
		#	self.screen = pygame.display.set_mode((1280, 720), 0, 32)

	def createButton(self):
		self.buttons.add(Button_Image(x=200,y=200,text='开始'))
		self.buttons.add(Button_Image(x=450,y=200,text='离开'))

	def sendData(self, s):
		communicater.sendStr(s)

	def handleButtonEvents(self):
		if self.buttons.pressed == '开始':
			self.scene_now = Scene_Room()
		elif self.buttons.pressed == '离开':
			sys.exit()
		self.buttons.pressed = ''

class Scene_Room(Scene_Base):
	def __init__(self):
		self.buttons = Buttons()
		self.scene_temp = self
		self.scene_now = self
		self.player = None
		self.otherPlayer = []
		self.background = pygame.image.load('..\\res\\image\\backdrop\\background.jpg').convert_alpha()
		self.background = pygame.transform.scale(self.background, (1280,720))
		self.lsfontstyle = pygame.font.Font("..\\res\\font\\ls.ttf", 20)
		self.tipHandler = TipHandler()
		self.recvStrList = []
		self.tempOtherPlayer = ['' for i in range(10)]
		self.heroSelecter = None
		self.cardSelecter = None
		
	def start(self):
		self.createButton()
		self.createPlayer()
		
	def update(self):
		self.recvUpdate()
		inputs.update()
		self.player.update()
		self.otherplayerUpdate()
		self.screenUpdate()
		self.buttons.update()
		self.handleButtonEvents()
		self.fpsUpdate()
		self.heroSelecterUpdate()
		self.cardSelecterUpdate()

	def refresh(self):	
		self.backgroundDraw()
		self.buttons.draw()
		self.player.draw()
		self.otherPlayerDraw()
		self.tipDraw()
		self.fpsDraw()	
		self.heroSelecterDraw()
		self.cardSelecterDraw()
		pygame.display.update()

	def backgroundDraw(self):
		screen.blit(self.background, (0,0))

	def otherPlayerDraw(self):
		for op in self.otherPlayer:
			op.draw()

	def tipDraw(self):
		if self.tipHandler.visable == True:
			self.tipHandler.draw()

	def heroSelecterDraw(self):
		if self.player.status != 'selecthero':
			return
		self.heroSelecter.draw()

	def cardSelecterDraw(self):
		if self.player.showCard == True:
			self.cardSelecter.draw()

	def fpsDraw(self):
		image_temp = self.lsfontstyle.render("fps:"+str(self.fps), True, (255, 255, 255))
		screen.blit(image_temp, (1200,20))

	def sendData(self, s):
		communicater.sendStr(s)

	def getOpByNo(self, no):
		for op in self.otherPlayer:
			if op.No == no:
				return op
		return None

	def handleSetRoomSize(self, s):
		self.player.roomSize = int(s[1])

	def handleSetPlayNumber(self, s):
		if s[1] == self.player.username:
			self.player.setNo(s[2])
			self.createOtherPlayer()
		else:
			self.tempOtherPlayer[int(s[2])] = s[1]
			if self.player.No != '':
				op = self.getOpByNo(s[2])
				op.username = s[1]

	def handleSetLord(self, s):
		if s[1] == self.player.No:
			self.player.setIdentity("lord")
		else:
			op = self.getOpByNo(s[1])
			op.setIdentity("lord")

	def handleSetIdentity(self, s):
		if s[1] == self.player.No:
			self.player.setIdentity(s[2])

	def handleSelectHero(self, s):
		if s[1] == self.player.No:
			self.heroSelecter = HeroSelecter(s)
			self.player.status = 'selecthero'

	def handleChoosedHero(self, s):
		if s[1] == self.player.No:
			self.player.setHero(int(s[2]))
		else:
			op = self.getOpByNo(s[1])
			op.setHero(int(s[2]))

	def handleSendCards(self, s):
		if s[2] == self.player.No:
			cardNum = int(s[3])
			for i in range(cardNum):
				cardIdent = int(s[i+4])
				self.player.addCard(cardIdent)
			if s[1] == 'Draw':
				self.sendData("DrawOver," + s[2])
			if s[1] == 'Ex':
				self.sendData("TrickEffectOver," + s[2])
			if s[1] == 'Grace':
				self.player.status = 'none'
				self.sendData("TrickEffectOver," + s[2])
		else:
			op = self.getOpByNo(s[2])
			op.addCard(int(s[3]))
			if s[1] == 'Grace':
				self.cardSelecter.disableCard(int(s[4]))

	def handleShowCards(self, s):
		self.cardSelecter = CardSelecter(s)
		self.player.showCard = True

	def handleShowCardsOff(self, s):
		self.player.showCard = False
		self.cardSelecter.visable = False

	def handleRoundStart(self, s):
		if s[1] == self.player.No:
			self.sendData("RoundStartOver," + s[1])

	def handleStart(self, s):
		if s[1] == self.player.No:
			self.sendData("StartOver," + s[1])

	def handleJudge(self, s):
		if s[1] == self.player.No:
			self.sendData("JudgeOver," + s[1])

	def handleDraw(self, s):
		if s[1] == self.player.No:
			self.sendData("DrawOk," + s[1])

	def handlePlay(self, s):
		if s[1] == self.player.No:
			self.player.setStatus("play")

	def handleEffect(self, s):
		tempPlayer = s[1]
		card = copy.copy(iCard[int(s[2])])

		if tempPlayer == self.player.No:
			if card.basetype == "equip":
				self.player.equipCard(card)		
			if card.subtype == "recover":
				self.player.incHP(1)
		else:
			op = self.getOpByNo(tempPlayer)
			if card.basetype == "equip":
				op.equipCard(card)
			if card.subtype == "recover":
				op.incHP(1)

	def handleSlash(self, s):
		if s[3] == self.player.No:
			self.player.slashSource = s[1]
			self.player.slashCard = s[2]
			self.tipHandler.setText("请打出一张【闪】以响应杀")
			self.tipHandler.setVisable(True, False)
			#self.tipHandler.visable = True
			self.player.setStatus("beslash")

	def handleSlashJinked(self, s):
		if s[1] == self.player.No:
			self.sendData("NotAppendSlash,"+s[1]) 

	def handleSlashDamage(self, s):
		if s[2] == self.player.No:
			self.player.decHP(1)
			self.sendData("NotLaunchAfterBeDamage,"+s[2])
		else:
			op = self.getOpByNo(s[2])
			op.decHP(1)

	def handleAskNullification(self, s):
		goodTrick = ["amazing_grace", "god_salvation", "ex_nihilo", "nullification"]
		if s[1] == self.player.No:
			if len(s) == 4:
				self.player.trickSource = ''
				self.player.trickCard = s[3]
				self.player.trickTarget = s[2]
			else:
				self.player.trickSource = s[4]
				self.player.trickCard = s[3]
				self.player.trickTarget = s[2]

			card = copy.copy(bCards[int(self.player.trickCard) - 1])
			if self.player.trickSource == '' and self.player.No == self.player.trickTarget:
				self.sendData("NotUseNullification,"+self.player.No)
				return

			if self.player.trickSource == '' and self.player.No == self.player.trickTarget and card.subtype == 'single':
				self.sendData("NotUseNullification,"+self.player.No)
				return

			if self.player.No == self.player.trickSource and card.subtype == 'single':
				self.sendData("NotUseNullification,"+self.player.No)
				return

			if self.player.No == self.player.trickTarget and card.name in goodTrick:
				self.sendData("NotUseNullification,"+self.player.No)
				return

			self.tipHandler.setText("是否使用【无懈可击】？")
			if self.player.trickTarget == self.player.No:
				self.tipHandler.setTarget(self.player.hero.hero.name)
			else:
				op = self.getOpByNo(self.player.trickTarget)
				self.tipHandler.setTarget(op.hero.hero.name)

			if self.player.trickSource != '':
				if self.player.trickSource == self.player.No:
					self.tipHandler.setSource(self.player.hero.hero.name)
				else:
					op = self.getOpByNo(self.player.trickSource)
					self.tipHandler.setSource(op.hero.hero.name)

			self.tipHandler.setCard(int(self.player.trickCard))

			#self.tipHandler.showImage = True
			self.tipHandler.setVisable(True, True)
			#self.tipHandler.refresh()
			self.player.status = "usenullification"

	def handleTrickEffect(self, s):
		card = copy.copy(iCard[int(s[2])])
		if card.name == "ex_nihilo":
			if s[1] == self.player.No:
				self.sendData("AskCards,"+s[1]+",2")
		elif card.name == "amazing_grace":
			if s[1] == self.player.No:
				self.player.status = 'selectcard'
		elif card.name == "god_salvation":
			if s[1] == self.player.No:
				self.player.incHP(1)
				self.sendData("TrickEffectOver,"+s[1])
			else:
				op = self.getOpByNo(s[1])
				op.incHP(1)

	def handleDecreaseCard(self, s):
		if s[1] != self.player.No:
			op = self.getOpByNo(s[1])
			op.addCard(-int(s[2]))

	def handleDiscard(self, s):
		if s[1] == self.player.No:
			self.player.status = "discard"
			for hcard in self.player.clst:
				hcard.select = False
 
	def handleRecv(self):
		for s in self.recvStrList:
			tempStr = s.split(",")
			if tempStr[0] == "SetRoomSize":
				self.handleSetRoomSize(tempStr)
			elif tempStr[0] == "SetPlayNumber":
				self.handleSetPlayNumber(tempStr)
			elif tempStr[0] == "SetLord":
				self.handleSetLord(tempStr)
			elif tempStr[0] == "SetIdentity":
				self.handleSetIdentity(tempStr)
			elif tempStr[0] == "SelectHero":
				self.handleSelectHero(tempStr)
			elif tempStr[0] == "ChoosedHero":
				self.handleChoosedHero(tempStr)
			elif tempStr[0] == "SendCards":
				self.handleSendCards(tempStr)
			elif tempStr[0] == "ShowCards":
				self.handleShowCards(tempStr)
			elif tempStr[0] == "ShowCardsOff":
				self.handleShowCardsOff(tempStr)
			elif tempStr[0] == "RoundStart":
				self.handleRoundStart(tempStr)
			elif tempStr[0] == "Start":
				self.handleStart(tempStr)
			elif tempStr[0] == "Judge":
				self.handleJudge(tempStr)
			elif tempStr[0] == "Draw":
				self.handleDraw(tempStr)
			elif tempStr[0] == "Play":
				self.handlePlay(tempStr)
			elif tempStr[0] == "Effect":
				self.handleEffect(tempStr)
			elif tempStr[0] == "Slash":
				self.handleSlash(tempStr)
			elif tempStr[0] == "SlashJinked":
				self.handleSlashJinked(tempStr)
			elif tempStr[0] == "SlashDamage":
				self.handleSlashDamage(tempStr)
			elif tempStr[0] == "AskNullification":
				self.handleAskNullification(tempStr)
			elif tempStr[0] == "TrickEffect":
				self.handleTrickEffect(tempStr)
			elif tempStr[0] == "DecreaseCard":
				self.handleDecreaseCard(tempStr)
			elif tempStr[0] == "Discard":
				self.handleDiscard(tempStr)

	def recvUpdate(self):
		self.recvStrList = communicater.recvStrList()
		self.handleRecv()

	def getBaseDistance(self, op):
		dis1 = 0
		dis2 = 0
		tempNo = self.player.No
		while tempNo != op.No:
			tempNo = str(int(tempNo) % self.player.roomSize + 1)
			if self.getOpByNo(tempNo).isDeath == False:
				dis1 += 1
		tempNo = self.player.No
		while tempNo != op.No:
			tempNo = str((int(tempNo) - 2 + self.player.roomSize)% self.player.roomSize + 1)
			if self.getOpByNo(tempNo).isDeath == False:
				dis2 += 1
		return min(dis1, dis2)

	def canUse(self, op, card):
		if op.isDeath:
			return False
		if card.name == "slash":
			dis = self.getBaseDistance(op)
			if self.player.ahourse != None:
				dis -= 1
			if op.ghourse != None:
				dis += 1
			attrange = 1
			if self.player.weapon != None:
				if self.player.weapon.card.name == 'axe':
					attrange = 3
				elif self.player.weapon.card.name == 'blade':
					attrange = 3
				elif self.player.weapon.card.name == 'crossbow':
					attrange = 1
				elif self.player.weapon.card.name == 'double_sword':
					attrange = 2
				elif self.player.weapon.card.name == 'halberd':
					attrange = 4
				elif self.player.weapon.card.name == 'kylin_bow':
					attrange = 5
			if attrange >= dis:
				return True
			else:
				return False
		elif card.name == "dismantlement":
			return True
		elif card.name == "snatch":
			dis = self.getBaseDistance(op)
			if self.player.ahourse != None:
				dis -= 1
			if op.ghourse != None:
				dis += 1
			if 1 >= dis:
				return True
			else:
				return False
		elif card.name == "duel":
			return True
			
		return False

	def otherplayerUpdate(self):
		if self.player.No == "":
			return
		if self.player.status == "play":
			if self.player.selectCard != None and self.player.selectCard.noSelection() == False:
				for op in self.otherPlayer:
					if op.status != 'selected':
						if self.canUse(op, self.player.selectCard):
							op.status = 'selectable'
						else:
							op.status = 'disable'
							
				mouse_x,mouse_y = pygame.mouse.get_pos()
				for op in self.otherPlayer:
					if op.status != 'disable':
						if (op.x < mouse_x < op.x+143) and (op.y < mouse_y < op.y+195):
							if inputs.mouseclick[1]:
								if op.status == 'selectable':
									op.status = 'selected'
									self.player.selectPlayer = op
									for oo in self.otherPlayer:
										if oo != self.player.selectPlayer:
											if oo.status == 'selected':
												oo.status = 'selectable'
								elif op.status == 'selected':
									op.status = 'selectable'
									self.player.selectPlayer = None
			else:
				for op in self.otherPlayer:
					op.status = 'row'	
		else:
			for op in self.otherPlayer:
				op.status = 'row'

	def screenUpdate(self):
		#if inputs.newkeys[K_1]:
		#	screen = pygame.display.set_mode((1280, 720), FULLSCREEN, 32)
		#if inputs.newkeys[K_2]:
		#	screen = pygame.display.set_mode((1280, 720), 0, 32)
		pass

	def fpsUpdate(self):
		time_passed = self.clock.tick()
		if time_passed < 30:
			time.sleep((30-time_passed) / 1000.0)
		time_passed2 = self.clock.tick()

		self.refreshtime += time_passed + time_passed2
		self.refreshtimes += 1
		self.fps = int(self.refreshtimes / (self.refreshtime/1000.0))
		if self.refreshtimes >= 10000:
			self.refreshtime /= 2
			self.refreshtimes /= 2

	def heroSelecterUpdate(self):
		if self.player.status != 'selecthero':
			return
		self.heroSelecter.update()
		if self.heroSelecter.pressed != -1:
			self.sendData("ChooseHero,"+self.player.No+","+str(self.heroSelecter.pressed))
			self.heroSelecter.visable = False
			self.player.status = 'none'

	def cardSelecterUpdate(self):
		if self.player.status != 'selectcard':
			return
		self.cardSelecter.update()
		if self.cardSelecter.pressed != -1:
			self.sendData("ChooseCard,"+self.player.No+","+str(self.cardSelecter.pressed))
			self.cardSelecter.disableCard(self.cardSelecter.pressed)
			self.cardSelecter.setAllRow()
			self.player.status = 'none'


	def createButton(self):
		self.buttons.add(Button_Image(x=200,y=200,text='准备'))

	def createPlayer(self):
		self.player = Player() 

	def buildOtherPlayerNo(self):
		temp = int(self.player.No)
		tlst = []
		for i in range(self.player.roomSize - 1):
			temp = temp % self.player.roomSize + 1
			tlst.append(str(temp))
		return tlst

	def createOtherPlayer(self):
		nlst = self.buildOtherPlayerNo()
		x = []
		y = []
		if self.player.roomSize == 2:
			x = [475]
			y = [50]
		elif self.player.roomSize == 3:
			x = [650, 300]
			y = [50, 50]
		elif self.player.roomSize == 4:
			x = [850, 475, 100]
			y = [200, 50, 200]
		elif self.player.roomSize == 5:
			x = [850, 600, 350, 100]
			y = [200, 50, 50, 200]

		for i in range(self.player.roomSize - 1):
			self.otherPlayer.append(OtherPlayer(x = x[i], y = y[i], No = nlst[i], username = self.tempOtherPlayer[int(nlst[i])]))

	def handleOkButton(self):
		if self.player.status == 'play': 
			if self.player.selectPlayer != None:
				self.sendData("Apply,"+self.player.No+","+str(self.player.selectCard.ident)+","+self.player.selectPlayer.No)
			else:
				self.sendData("Apply,"+self.player.No+","+str(self.player.selectCard.ident))
			self.player.deleteCard(self.player.selectCard.ident)
			self.player.selectCard = None
			self.player.selectPlayer = None
			self.player.setStatus("none")
		elif self.player.status == 'beslash':
			self.sendData("Jink,"+self.player.No+","+self.player.slashSource+","+self.player.slashCard+","+str(self.player.selectCard.ident))
			self.player.deleteCard(self.player.selectCard.ident)
			self.player.selectCard = None
			self.player.status = 'none'
			self.tipHandler.setVisable(False, False)
		elif self.player.status == 'usenullification':
			self.sendData("Apply,"+self.player.No+","+str(self.player.selectCard.ident))
			self.player.deleteCard(self.player.selectCard.ident)
			self.player.selectCard = None
			self.player.status = 'none'
			self.tipHandler.setVisable(False, False)
		elif self.player.status == 'discard':
			self.sendData("Throw,"+self.player.No+","+str(self.player.selectCardNum)+self.player.selectCardsToSting())
			self.player.deleteSelect()
			self.player.status = 'none'
			self.player.selectCardNum = 0
			self.tipHandler.setVisable(False, False)

	def handleCancelButton(self):
		if self.player.status == 'beslash':
			self.sendData("NotJink,"+self.player.No+","+self.player.slashSource+","+self.player.slashCard)
			self.player.slashSource = ''
			self.player.slashCard = ''
			self.player.selectCard = None
			self.player.selectPlayer = None
			self.player.status = 'none'
			self.tipHandler.setVisable(False, False)
		elif self.player.status == 'usenullification':
			self.sendData("NotUseNullification,"+self.player.No)
			self.player.selectCard = None
			self.player.selectPlayer = None
			self.player.status = 'none'
			self.tipHandler.setVisable(False, False)

	def handleDiscardButton(self):
		if self.player.status == 'play':
			disNum = len(self.player.clst) - self.player.nowHP
			if disNum <= 0:
				self.sendData("PlayOver,"+self.player.No+",NotDiscard")
				self.player.status = 'none'
			else:
				self.sendData("PlayOver,"+self.player.No+",Discard")
				self.tipHandler.setText("请弃置"+str(disNum)+"张手牌")
				self.tipHandler.setVisable(True, False)
				#self.tipHandler.visable = True

	def handleButtonEvents(self):
		if self.buttons.pressed == '准备':
			self.sendData("Ready," + communicater.nick)
			self.buttons.disable('准备')
		self.buttons.pressed = ''

		if self.player.playerButtons.pressed == '确定':
			self.handleOkButton()	
		elif self.player.playerButtons.pressed == '取消':
			self.handleCancelButton()
		elif self.player.playerButtons.pressed == '结束':
			self.handleDiscardButton()
		self.player.playerButtons.pressed = ''



