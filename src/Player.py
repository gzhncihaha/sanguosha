from BuildCards import *
from Card import *
from Button import *
from BuildHeros import *
from Hero import *
from ToServer import *
from ProgramEvent import *
from Screen import *
from PlayerCanUse import *
import pygame
class Player:
	def __init__(self):
		self.hero = None
		self.identity = ''
		self.HP = 1
		self.nowHP = 0
		self.clst = []
		self.playerButtons = PlayerButtons()
		self.weapon = None
		self.armor = None
		self.ahourse = None
		self.ghourse = None
		self.No = ""
		self.prepareNo = ""
		self.status = "none"
		self.isDeath = False
		self.username = communicater.nick
		self.roomSize = 0 

		self.handcardUp = 500
		self.handcardDown = 630
		self.handcardLeft = 200
		self.handcardWide = 93

		self.slashSource = ''
		self.slashCard = ''

		self.trickSource = ''
		self.trickCard = ''
		self.trickTarget = ''

		self.showCard = False

		self.selectCard = None
		self.selectCardNum = 0
		self.selectPlayer = None
		self.lastselectPlayer = None
		self.createButton()
		self.HpBarImg = self.loadHpBarImg()
		self.equipgray = Gray().cut(149,25)

	def setHero(self, ident):
		for hero in bHeros:
			if ident == hero.ident:
				self.hero = IHero(hero)
				if self.identity == 'lord':
					self.HP = hero.baseHP + 1
				else:
					self.HP = hero.baseHP
				self.nowHP = self.HP
				break

	def setIdentity(self, ident):
		self.identity = ident

	def addCard(self, ident):
		for card in bCards:
			if ident == card.ident:
				self.clst.append(HandCard(card, "disable"))
				break

	def deleteCard(self, ident):
		count = 0
		for card in self.clst:
			if ident == card.card.ident:
				del self.clst[count]
				break
			count += 1

	def useCard(self, ident):
		ctemp = None
		for card in bCards:
			if ident == card.ident:
				ctemp = card
				break
		#print("id:"+str(ident))
		if ctemp == None:
			return

		if ctemp.basetype == "equip":
			if ctemp.subtype == "weapon":
				self.weapon = EquipCard(ctemp)
			elif ctemp.subtype == "armor":
				self.armor = EquipCard(ctemp)
			elif ctemp.subtype == "ahourse":
				self.ahourse = EquipCard(ctemp)
			elif ctemp.subtype == "ghourse":
				self.ghourse = EquipCard(ctemp)
			return

	def equipCard(self, card):
		if card.subtype == "weapon":
			self.weapon = EquipCard(card)
		elif card.subtype == "armor":
			self.armor = EquipCard(card)
		elif card.subtype == "ahourse":
			self.ahourse = EquipCard(card)
		elif card.subtype == "ghourse":
			self.ghourse = EquipCard(card)

	def decHP(self, num):
		self.nowHP -= num

	def incHP(self, num):
		if self.nowHP + num <= self.HP:
			self.nowHP += num

	def updateHandcardStatus(self):
		if self.status == "none":
			for hcard in self.clst:
				hcard.status = "disable"
				hcard.select = False
		elif self.status == "play":
			for hcard in self.clst:
				hcard.status = "disable"
				if hcard.card.basetype == "base":
					if hcard.card.subtype == "attack":
						hcard.status = "row"
					elif hcard.card.subtype == "recover" and self.nowHP < self.HP:
						hcard.status = "row"
				elif hcard.card.basetype == "equip":
					hcard.status = "row"
				elif hcard.card.basetype == "trick":
					if hcard.card.name != "nullification":
						hcard.status = "row"
		elif self.status == "beslash":
			for hcard in self.clst:
				hcard.status = "disable"
				if hcard.card.name == "jink":
					hcard.status = "row"
		elif self.status == "usenullification":
			for hcard in self.clst:
				hcard.status = "disable"
				if hcard.card.name == "nullification":
					hcard.status = "row"

		elif self.status == "discard":
			for hcard in self.clst:
				hcard.status = "row"
			if len(self.clst) - self.selectCardNum == self.nowHP:
				for hcard in self.clst:
					if hcard.select == False:
						hcard.status = "disable"

	def updatePlayerButtonStatus(self):
		if self.status == "none":
			for button in self.playerButtons.blst:
				button.status = "disabled"
		elif self.status == "play":
			htemp = None
			for hcard in self.clst:
				if hcard.select == True:
					htemp = hcard
					break
			for button in self.playerButtons.blst:
				button.status = "disabled"
				if button.fname == "discard":
					button.status = "row"
				if htemp != None and htemp.noSelection() and button.fname == "ok":
					button.status = "row"
				if htemp != None and htemp.noSelection() == False and self.selectPlayer != None and button.fname == "ok":
					button.status = "row"
		elif self.status == "beslash" or self.status == "usenullification":
			for button in self.playerButtons.blst:
				button.status = "disabled"
				if button.fname == "cancel":
					button.status = "row"
				if self.selectCard != None and button.fname == "ok":
					button.status = "row"
		elif self.status == "discard":
			for button in self.playerButtons.blst:
				button.status = "disabled"
				#print(len(self.clst), "  ",self.selectCardNum, "  ",self.nowHP)
				if button.fname == "ok" and (len(self.clst) - self.selectCardNum == self.nowHP):
					button.status = "row"

	def update(self):
		self.updateHandcardStatus()
		
		if self.status == "play":
			self.singleSelect()
		elif self.status == "beslash":
			self.singleSelect()
		elif self.status == "usenullification":
			self.singleSelect()
		elif self.status == "discard":
			self.multiSelect()

		self.updatePlayerButtonStatus()
		self.playerButtons.update()

	def singleSelect(self):
		mouse_x,mouse_y = pygame.mouse.get_pos()
		left = self.handcardLeft
		right = self.handcardLeft + self.handcardWide
		up = self.handcardUp
		down = self.handcardDown

		for hcard in self.clst:
			if hcard.select == True:
				if (left < mouse_x < right) and (up-30 < mouse_y < down-30):
					if inputs.mouseclick[1]:
						hcard.select = False
						self.selectCard = None
						left += self.handcardWide
						right += self.handcardWide
						continue
					hcard.status = 'on'
				else:
					hcard.status = 'row'
			else:
				if (left < mouse_x < right) and (up < mouse_y < down):
					if inputs.mouseclick[1] and hcard.status != 'disable':
						hcard.select = True
						self.selectCard = hcard.card
						for hh in self.clst:
							if hh != hcard:
								hh.select = False
						left += self.handcardWide
						right += self.handcardWide
						continue
					if hcard.status != 'disable':
						hcard.status = 'on'
				else:
					if hcard.status != 'disable':
						hcard.status = 'row'
			left += self.handcardWide
			right += self.handcardWide

	def multiSelect(self):
		mouse_x,mouse_y = pygame.mouse.get_pos()
		left = self.handcardLeft
		right = self.handcardLeft + self.handcardWide
		up = self.handcardUp
		down = self.handcardDown
		for hcard in self.clst:
			if hcard.select == True:
				if (left < mouse_x < right) and (up-30 < mouse_y < down-30):
					if inputs.mouseclick[1]:
						hcard.select = False
						self.selectCardNum -= 1
						left += self.handcardWide
						right += self.handcardWide
						continue
					hcard.status = 'on'
				else:
					hcard.status = 'row'
			else:
				if (left < mouse_x < right) and (up < mouse_y < down):
					if inputs.mouseclick[1] and hcard.status != 'disable':
						hcard.select = True
						self.selectCardNum += 1
						left += self.handcardWide
						right += self.handcardWide
						continue
					hcard.status = 'on'
				else:
					hcard.status = 'row'
			left += self.handcardWide
			right += self.handcardWide

	def selectCardsToSting(self):
		returnStr = ''
		for hcard in self.clst:
			if hcard.select == True:
				returnStr = returnStr + ',' + str(hcard.card.ident)
		return returnStr

	def deleteSelect(self):
		i = 0
		while True:
			if self.clst[i].select == True:
				del self.clst[i]
				lentemp = len(self.clst)
				if i == lentemp:
					break
				continue
			i += 1
			lentemp = len(self.clst)
			if i == lentemp:
				break

	def createButton(self):
		self.playerButtons.add(Button_RealImage(x=1020, y=470, ftext='确定', fname='ok'))
		self.playerButtons.add(Button_RealImage(x=1020, y=545, ftext='取消', fname='cancel'))
		self.playerButtons.add(Button_RealImage(x=1090, y=500, ftext='结束', fname='discard'))

	def loadHpBarImg(self):
		img0 = pygame.image.load('..\\res\\image\\system\\magatamas\\0.png').convert_alpha()
		img1 = pygame.image.load('..\\res\\image\\system\\magatamas\\1.png').convert_alpha()
		img2 = pygame.image.load('..\\res\\image\\system\\magatamas\\2.png').convert_alpha()
		img3 = pygame.image.load('..\\res\\image\\system\\magatamas\\3.png').convert_alpha()
		img4 = pygame.image.load('..\\res\\image\\system\\magatamas\\4.png').convert_alpha()
		img5 = pygame.image.load('..\\res\\image\\system\\magatamas\\5.png').convert_alpha()
		return img0,img1,img2,img3,img4,img5

	def setNo(self, no):
		self.No = no

	def setPrepare(self, no):
		self.prepareNo = no

	def setStatus(self, status):
		self.status = status

	def draw(self):
		self.draw_card()
		self.draw_equips()
		self.draw_HPbar()
		self.draw_bigHeroImg()
		self.playerButtons.draw()

	def draw_card(self):
		x = 200
		y = 500
		for card in self.clst:
			card.draw(x, y)
			x += 93

	def draw_equips(self):
		if self.weapon != None:
			self.weapon.draw(10, 500)
		else:
			screen.blit(self.equipgray, (10, 500))

		if self.armor != None:
			self.armor.draw(10, 535)
		else:
			screen.blit(self.equipgray, (10, 535))

		if self.ghourse != None:
			self.ghourse.draw(10, 570)
		else:
			screen.blit(self.equipgray, (10, 570))

		if self.ahourse != None:
			self.ahourse.draw(10, 605)
		else:
			screen.blit(self.equipgray, (10, 605))

	def draw_HPbar(self):
		if self.hero != None:
			x = 1170
			y = 470
			p = int(self.nowHP * 5 / self.HP)
			step = 110 / self.HP
			for i in range(self.HP):
				#print(x,"  ",y,"  ",p)
				if (i+1) <= self.nowHP:
					screen.blit(self.HpBarImg[p], (x,y))
				else:
					screen.blit(self.HpBarImg[0], (x,y))
				x += step

	def draw_bigHeroImg(self):
		if self.hero != None:
			screen.blit(self.hero.bigImg, (1180, 520))




