import pygame
from pygame.locals import *
from Button import *
from Screen import *
class Card:
	def __init__(self, suit="spade", number="1", name="slash", ident=1, basetype="base", subtype="attack"):
		self.suit = suit
		self.number = number
		self.name = name
		self.ident = ident
		self.basetype = basetype
		self.subtype = subtype

	def toIMG(self, kind=1):
		background = pygame.image.load('..\\res\\image\\card\\'+self.name+'.jpg').convert_alpha()
		suitImage = pygame.image.load('..\\res\\image\\system\\cardsuit\\'+self.suit+'.png').convert_alpha()
		numberImage = None
		if self.suit=="spade" or self.suit=="club":
			numberImage = pygame.image.load('..\\res\\image\\system\\black\\'+self.number+'.png').convert_alpha()
		else:
			numberImage = pygame.image.load('..\\res\\image\\system\\red\\'+self.number+'.png').convert_alpha()
		background.blit(numberImage, (1,3))
		if self.suit == "diamond":
			background.blit(suitImage, (2,15))
		else:
			background.blit(suitImage, (1,16))
		if kind == 2:
			image_back = Gray(color = 'gray').cut(93,130)
			background.blit(image_back, (0,0))
		elif kind == 3:
			background = pygame.transform.rotozoom(background,0,1.1)
		return background

	def toEIMG(self):
		img = pygame.image.load('..\\res\\image\\equips\\'+self.name+'.png').convert_alpha()
		return img

	def noSelection(self):
		if self.basetype == 'equip':
			return True
		if self.name == 'peach':
			return True
		if self.name == 'amazing_grace':
			return True
		if self.name == 'archery_attack':
			return True
		if self.name == 'ex_nihilo':
			return True
		if self.name == 'god_salvation':
			return True
		if self.name == 'lightning':
			return True
		if self.name == 'savage_assault':
			return True
		
		return False

class HandCard:
	def __init__(self, card, status = "disable"):
		self.card = card
		self.status = status
		self.select = False
		self.IMG1 = self.card.toIMG(1)
		self.IMG2 = self.card.toIMG(2)
		self.IMG3 = self.card.toIMG(3)
		self.c_w, self.c_h = self.IMG3.get_size()
		self.c_w = (self.c_w - 93)/2
		self.c_h = (self.c_h - 130)/2

	def draw(self, x, y):
		if self.select == True:
			y -= 30
		if self.status == "disable":
			screen.blit(self.IMG2, (x,y))
		elif self.status == "row":
			screen.blit(self.IMG1, (x,y))
		elif self.status == "on":
			screen.blit(self.IMG3, (x-self.c_w,y-self.c_h))

	def noSelection(self):
		if self.card.basetype == 'equip':
			return True
		if self.card.name == 'peach':
			return True
		if self.card.name == 'amazing_grace':
			return True
		if self.card.name == 'archery_attack':
			return True
		if self.card.name == 'ex_nihilo':
			return True
		if self.card.name == 'god_salvation':
			return True
		if self.card.name == 'lightning':
			return True
		if self.card.name == 'savage_assault':
			return True
		
		return False

class EquipCard:
	def __init__(self, card):
		self.card = card
		self.select = False
		self.IMG = self.card.toEIMG()
		suitImage = pygame.image.load('..\\res\\image\\system\\cardsuit\\'+card.suit+'.png').convert_alpha()
		numberImage = None
		if card.suit=="spade" or card.suit=="club":
			numberImage = pygame.image.load('..\\res\\image\\system\\black\\'+card.number+'.png').convert_alpha()
		else:
			numberImage = pygame.image.load('..\\res\\image\\system\\red\\'+card.number+'.png').convert_alpha()
		if card.suit == "diamond":
			self.IMG.blit(suitImage, (111, -1))
		else:
			self.IMG.blit(suitImage, (110, 0))
		self.IMG.blit(numberImage, (125, 0))

	def draw(self, x, y):
		screen.blit(self.IMG, (x,y))



