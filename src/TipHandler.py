import pygame
import copy
from Screen import *
from BuildCards import *
from BuildHeros import *
class TipHandler:
	def __init__(self):
		self.lsfontstyle = pygame.font.Font("..\\res\\font\\ls.ttf", 22)
		self.tipframe = pygame.image.load('..\\res\\image\\system\\tip.png').convert_alpha()
		self.img = pygame.image.load('..\\res\\image\\system\\tip.png').convert_alpha()
		self.visable = False
		self.text = ''
		self.x = 400
		self.y = 260
		self.showImage = True
		self.sourceImage = None
		self.targetImage = None
		self.cardImage = None
		self.arrow = pygame.image.load('..\\res\\image\\system\\arrow.png').convert_alpha()

	def draw(self):
		screen.blit(self.img, (self.x, self.y))

	def refresh(self):
		self.img = copy.copy(self.tipframe)
		temp = self.lsfontstyle.render("三国杀", True, (50, 180, 50))
		self.img.blit(temp, (200, 27))
		temp = self.lsfontstyle.render(self.text, True, (255, 255, 255))
		self.img.blit(temp, (25, 55))
		if self.showImage:
			if self.sourceImage != None:
				self.img.blit(self.cardImage, (25, 80))
				self.img.blit(self.sourceImage, (125, 90))
				self.img.blit(self.arrow, (225, 90))
				self.img.blit(self.targetImage, (275, 90))
			else:
				self.img.blit(self.cardImage, (25, 80))
				self.img.blit(self.targetImage, (125, 90))
		self.sourceImage = None
		self.targetImage = None

	def setText(self, t):
		self.text = t

	def setSource(self, name):
		self.sourceImage = pygame.image.load('..\\res\\image\\generals\\big\\'+name+'.png').convert_alpha()
		#self.targetImage = pygame.image.load('..\\res\\image\\generals\\big\\'+name+'.png').convert_alpha()
		#self.targetImage = None

	def setTarget(self, name):
		self.targetImage = pygame.image.load('..\\res\\image\\generals\\big\\'+name+'.png').convert_alpha()

	def setCard(self, ident):
		self.cardImage = bCards[ident - 1].toIMG(1)

	def setVisable(self, vis, img):
		self.visable = vis
		self.showImage = img
		self.refresh()

				

