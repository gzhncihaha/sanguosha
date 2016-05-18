#import Skill
import pygame
from pygame.locals import *
class Hero:
	def __init__(self, cname='曹操', name='caocao', country='wei', sex=1, baseHP=4, ident=1, s1='', s2='', s3=''):
		self.cname = cname
		self.name = name
		self.country = country
		self.sex = sex
		self.baseHP = baseHP
		self.ident = ident
		self.slst = []
		if s1 != '':
			self.slst.append(s1)
		if s2 != '':
			self.slst.append(s1)
		if s3 != '':
			self.slst.append(s1)

	def toFullImg(self):
		background = pygame.image.load('..\\res\\image\\generals\\card\\'+self.name+'.jpg').convert_alpha()
		return background

	def toBigImg(self):
		background = pygame.image.load('..\\res\\image\\generals\\big\\'+self.name+'.png').convert_alpha()
		return background

	def toSmallImg(self):
		background = pygame.image.load('..\\res\\image\\generals\\small\\'+self.name+'.png').convert_alpha()
		return background
		
class IHero:
	def __init__(self, hero):
		self.hero = hero
		self.bigImg = hero.toBigImg()

class SIHero:
	def __init__(self, hero):
		self.hero = hero
		self.smallImg = hero.toSmallImg()
