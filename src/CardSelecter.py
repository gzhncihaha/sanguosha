import pygame
import copy
from Screen import *
from ProgramEvent import *
from Card import *
from BuildCards import *
class CardSelecter:
	def __init__(self, s):
		self.visable = True
		self.clst = []
		self.pressed = -1
		self.size = int(s[2])
		x = 200
		y = 200
		for i in range(self.size):
			num = int(s[i + 3])
			self.clst.append(CardInSelecter(num, x, y))
			x += 93

	def draw(self):
		if self.visable == False:
			return
		
		for card in self.clst:
			if card.status == 'pressed':
				screen.blit(card.img1, (card.x+3, card.y+3))
			elif card.status == 'disable':
				screen.blit(card.img2, (card.x, card.y))
			else:
				screen.blit(card.img1, (card.x, card.y))

	def update(self):
		if self.visable == False:
			return
		mouse_x,mouse_y = pygame.mouse.get_pos()
		for card in self.clst:
			if card.status == 'disable':
				continue
			if (card.x < mouse_x < card.x+card.w) and (card.y < mouse_y < card.y+card.h):
				if inputs.mousepressed[1]:
					card.status='pressed'
				else:
					if inputs.mouseclick[1]:
						self.pressed = card.card.ident
						#button.event()
						continue
					card.status='on'
			else:
				card.status='row'

	def disableCard(self, ident):
		for card in self.clst:
			if card.card.ident == ident:
				card.status = 'disable'
				return

	def setAllRow(self):
		for card in self.clst:
			if card.status != 'disable':
				card.status = 'row'
		
class CardInSelecter:
	def __init__(self, ident, x, y):
		self.card = copy.copy(bCards[ident-1])
		#self.img = pygame.image.load('..\\res\\image\\generals\\card\\' + self.hero.name + '.jpg').convert_alpha()
		self.img1 = self.card.toIMG(1)
		self.img2 = self.card.toIMG(2)
		#self.img3 = self.card.toIMG(3)
		self.x = x
		self.y = y
		self.w, self.h = self.img1.get_size()
		self.status = 'row'