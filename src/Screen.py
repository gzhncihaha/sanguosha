import pygame
from pygame.locals import *
class Screen:
	def __init__(self):
		self.screen = None
	def initialize(self):
		self.screen = pygame.display.set_mode((1280, 720), 0, 32)
	def blit(self, img, pos):
		self.screen.blit(img, pos)

screen = Screen()


