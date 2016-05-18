import pygame
import copy
from Screen import *
from ProgramEvent import *
from Hero import *
from BuildHeros import *
class HeroSelecter:
	def __init__(self, s):
		self.visable = True
		self.hlst = []
		self.pressed = -1
		x = 100
		y = 100
		for i in range(5):
			num = int(s[i + 2])
			self.hlst.append(HeroInSelecter(num, x, y))
			x += 200

	def draw(self):
		if self.visable == False:
			return
		
		for h in self.hlst:
			if h.status == 'pressed':
				screen.blit(h.img, (h.x+5, h.y+5))
			else:
				screen.blit(h.img, (h.x, h.y))

	def update(self):
		if self.visable == False:
			return
		mouse_x,mouse_y = pygame.mouse.get_pos()
		for h in self.hlst:
			if (h.x < mouse_x < h.x+h.w) and (h.y < mouse_y < h.y+h.h):
				if inputs.mousepressed[1]:
					h.status='pressed'
				else:
					if inputs.mouseclick[1]:
						self.pressed = h.hero.ident
						#button.event()
						continue
					h.status='on'
			else:
				h.status='row'
		
class HeroInSelecter:
	def __init__(self, ident, x, y):
		self.hero = copy.copy(bHeros[ident-1])
		#self.img = pygame.image.load('..\\res\\image\\generals\\card\\' + self.hero.name + '.jpg').convert_alpha()
		self.img = self.hero.toFullImg()
		self.x = x
		self.y = y
		self.w, self.h = self.img.get_size()
		self.status = 'row'



