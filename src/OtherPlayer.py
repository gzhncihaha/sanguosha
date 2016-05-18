from BuildCards import *
from Card import *
from Button import *
from BuildHeros import *
from Hero import *
from EquipName import *
from Screen import *
class OtherPlayer:
	def __init__(self, x=0, y=0, No='', username = ''):
		self.hero = None
		self.identity = 'fz'
		self.displayid = 'unknown'
		self.HP = 1
		self.nowHP = 0
		self.cardNum = 0
		self.weapon = None
		self.armor = None
		self.ahourse = None
		self.ghourse = None
		self.No = No
		self.isDeath = False
		
		self.username = username
		self.lsfontstyle = pygame.font.Font("..\\res\\font\\ls.ttf", 15)
		self.NoImg = self.lsfontstyle.render(self.No, True, (255, 255, 255))
		self.xkfontstyle = pygame.font.Font("..\\res\\font\\xk.ttf", 15)
		self.x = x
		self.y = y
		self.handcardimg = pygame.image.load('..\\res\\image\\system\\handcard.png').convert_alpha()
		self.frame = pygame.image.load('..\\res\\image\\system\\photo-back.png').convert_alpha()
		self.suitImg = self.loadSuitImg()
		self.HpBarImg = self.loadHpBarImg()
		self.displayidImg = self.loadDisIdImg()
		self.gray = Gray(color = 'gray').cut(130,185)
		self.red = Gray(color = 'red').cut(130,185)
		self.status = 'row'

	def setHero(self, ident):
		for hero in bHeros:
			if ident == hero.ident:
				self.hero = SIHero(hero)
				if self.identity == 'lord':
					self.HP = hero.baseHP + 1
				else:
					self.HP = hero.baseHP
				self.nowHP = self.HP
				self.kframe = self.loadKframe()
				self.kingdomImg = self.loadkingdomImg()
				break

	def setIdentity(self, ident):
		self.identity = ident

	def addCard(self, num):
		self.cardNum += num

	def deleteCard(self, num):
		self.cardNum -= num

	def loadHpBarImg(self):
		img0 = pygame.image.load('..\\res\\image\\system\\magatamas\\small-0.png').convert_alpha()
		img1 = pygame.image.load('..\\res\\image\\system\\magatamas\\small-1.png').convert_alpha()
		img2 = pygame.image.load('..\\res\\image\\system\\magatamas\\small-2.png').convert_alpha()
		img3 = pygame.image.load('..\\res\\image\\system\\magatamas\\small-3.png').convert_alpha()
		img4 = pygame.image.load('..\\res\\image\\system\\magatamas\\small-4.png').convert_alpha()
		img5 = pygame.image.load('..\\res\\image\\system\\magatamas\\small-5.png').convert_alpha()
		return img0,img1,img2,img3,img4,img5

	def loadSuitImg(self):
		img0 = pygame.image.load('..\\res\\image\\system\\cardsuit\\spade.png').convert_alpha()
		img0 = pygame.transform.rotozoom(img0,0,0.8)
		img1 = pygame.image.load('..\\res\\image\\system\\cardsuit\\heart.png').convert_alpha()
		img1 = pygame.transform.rotozoom(img1,0,0.8)
		img2 = pygame.image.load('..\\res\\image\\system\\cardsuit\\club.png').convert_alpha()
		img2 = pygame.transform.rotozoom(img2,0,0.8)
		img3 = pygame.image.load('..\\res\\image\\system\\cardsuit\\diamond.png').convert_alpha()
		img3 = pygame.transform.rotozoom(img3,0,0.8)
		return  img0,img1,img2,img3

	def loadKframe(self):
		return pygame.image.load('..\\res\\image\\kingdom\\frame\\'+self.hero.hero.country+'.png').convert_alpha()

	def loadkingdomImg(self):
		return pygame.image.load('..\\res\\image\\kingdom\\icon\\'+self.hero.hero.country+'.png').convert_alpha()

	def loadDisIdImg(self):
		img0 = pygame.image.load('..\\res\\image\\system\\roles\\'+self.displayid+'.png').convert_alpha()
		return img0

	def suitToInt(self, s):
		if s == "spade":
			return 0
		elif s == "heart":
			return 1
		elif s == "club":
			return 2
		elif s == "diamond":
			return 3
		return -1

	#def useCard(self, ident):
	#	self.equipItem(ident)

	#def equipItem(self, ident):
	#	ctemp = None
	#	for card in bCards:
	#		if ident == card.ident:
	#			ctemp = card
	#			break
	#	if ctemp.basetype == "equip":
	#		if ctemp.subtype == "weapon":
	#			self.weapon = ctemp
	#		elif ctemp.subtype == "armor":
	#			self.armor = ctemp
	#		elif ctemp.subtype == "ahourse":
	#			self.ahourse = ctemp
	#		elif ctemp.subtype == "ghourse":
	#			self.ghourse = ctemp

	def equipCard(self, card):
		if card.subtype == "weapon":
			self.weapon = card
		elif card.subtype == "armor":
			self.armor = card
		elif card.subtype == "ahourse":
			self.ahourse = card
		elif card.subtype == "ghourse":
			self.ghourse = card

	def decHP(self, num):
		self.nowHP -= num

	def incHP(self, num):
		if self.nowHP + num <= self.HP:
			self.nowHP += num

	def canUse(self, player, card):
		if card.name == "slash":
			dis = min(abs(int(player.No) - int(self.No)), abs(int(player.No) - (int(self.No)-5) ))
			if player.ahourse != None:
				dis -= 1
			if self.ghourse != None:
				dis += 1
			attrange = 1
			if player.weapon != None:
				if player.weapon.card.name == 'axe':
					attrange = 3
				elif player.weapon.card.name == 'blade':
					attrange = 3
				elif player.weapon.card.name == 'crossbow':
					attrange = 1
				elif player.weapon.card.name == 'double_sword':
					attrange = 2
				elif player.weapon.card.name == 'halberd':
					attrange = 4
				elif player.weapon.card.name == 'kylin_bow':
					attrange = 5
			if attrange >= dis:
				return True
			else:
				return False
		elif card.name == "dismantlement":
			return True
		elif card.name == "snatch":
			return True
		return False

	#def update(self):

	def draw(self):
		screen.blit(self.frame, (self.x,self.y))
		if self.No != '':
			screen.blit(self.NoImg, (self.x+20,self.y))
		if self.hero != None:
			screen.blit(self.hero.smallImg, (self.x+5,self.y+14))
			screen.blit(self.kframe, (self.x+3,self.y+12))
			screen.blit(self.kingdomImg, (self.x-9,self.y-9))
			screen.blit(self.displayidImg, (self.x+85,self.y+14))

		screen.blit(self.handcardimg, (self.x+5,self.y+68))
		#fontstyle = pygame.font.Font("..\\res\\font\\xk.ttf", 15)
		image_temp = self.xkfontstyle.render(str(self.cardNum), True, (255, 255, 255))
		screen.blit(image_temp, (self.x+9,self.y+72))
		if self.hero != None:
			xx = self.x+20
			yy = self.y+85
			p = int(self.nowHP * 5 / self.HP)
			step = 17
			for i in range(self.HP):
				#print(x,"  ",y,"  ",p)
				if (i+1) <= self.nowHP:
					screen.blit(self.HpBarImg[p], (xx,yy))
				else:
					screen.blit(self.HpBarImg[0], (xx,yy))
				xx += step

		#fontstyle = pygame.font.Font("..\\res\\font\\ls.ttf", 14)
		if self.weapon != None:
			screen.blit(self.suitImg[self.suitToInt(self.weapon.suit)], (self.x-2, self.y+115))
			image_temp = self.lsfontstyle.render(self.weapon.number+" "+Ename[self.weapon.name], True, (255, 255, 255))
			screen.blit(image_temp, (self.x+18, self.y+119))

		if self.armor != None:
			screen.blit(self.suitImg[self.suitToInt(self.armor.suit)], (self.x-2, self.y+132))
			image_temp = self.lsfontstyle.render(self.armor.number+" "+Ename[self.armor.name], True, (255, 255, 255))
			screen.blit(image_temp, (self.x+18, self.y+136))

		if self.ghourse != None:
			screen.blit(self.suitImg[self.suitToInt(self.ghourse.suit)], (self.x-2, self.y+149))
			image_temp = self.lsfontstyle.render(self.ghourse.number+" "+Ename[self.ghourse.name], True, (255, 255, 255))
			screen.blit(image_temp, (self.x+18, self.y+153))

		if self.ahourse != None:
			screen.blit(self.suitImg[self.suitToInt(self.ahourse.suit)], (self.x-2, self.y+166))
			image_temp = self.lsfontstyle.render(self.ahourse.number+" "+Ename[self.ahourse.name], True, (255, 255, 255))
			screen.blit(image_temp, (self.x+18, self.y+170))

		if self.status == 'disable':
			screen.blit(self.gray, (self.x,self.y))
		elif self.status == 'selected' or self.status == 'pressed':
			screen.blit(self.red, (self.x,self.y))



