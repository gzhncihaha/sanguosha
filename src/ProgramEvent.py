import pygame
from pygame.locals import *
class HandleEvent:
	def initialize(self):
		self.keystate = None
		self.mousepressed = [False for i in range(10)]
		self.mouseclick = [False for i in range(10)]
		self.update()

	def update(self):
		pygame.event.pump()
		if self.keystate:
			self.oldkeystate = self.keystate
			self.keystate = pygame.key.get_pressed()
			self.newkeys = list(map(lambda o,c: c and not o, self.oldkeystate, self.keystate))
		else:
			self.keystate = pygame.key.get_pressed()
			self.newkeys = self.keystate 
		self.mouseclick = [False for i in range(10)]

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				self.mousepressed[event.button] = True
			if event.type == pygame.MOUSEBUTTONUP:
				self.mousepressed[event.button] = False
				self.mouseclick[event.button] = True
		self.mousePos = pygame.mouse.get_pos()


class ProgramEvent:
	def __init__(self):
		self.keystate = [False for i in range(255)]
		self.mouseButtons = [False for i in range(255)]
		self.oldkeystate = [False for i in range(255)]
		self.oldmouseButtons = [False for i in range(255)]
		self.newkeys = [False for i in range(255)]
		self.mousetemp = [False for i in range(255)]
		self.update()


	def update(self):
		self.oldkeystate = self.keystate
		self.oldmouseButtons = self.mouseButtons
		self.mousetemp = [False for i in range(255)]
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.KEYDOWN:
				self.keystate[event.key] = True
			if event.type == pygame.KEYUP:
				self.keystate[event.key] = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				print(event.button)
			self.mousetemp = list(map(lambda o,c: c or o, self.mousetemp, pygame.mouse.get_pressed()))  
		self.mouseButtons = self.mousetemp
		self.newkeys = list(map(lambda o,c: c and not o, self.oldkeystate, self.keystate))
		self.mousePos = pygame.mouse.get_pos()



	def updateold(self):
		pygame.event.pump()

		if self.keystate:
			self.oldkeystate = self.keystate
			self.keystate = pygame.key.get_pressed()
			self.newkeys = list(map(lambda o,c: c and not o, self.oldkeystate, self.keystate))
		else:
			self.keystate = pygame.key.get_pressed()
			self.newkeys = self.keystate 
		if self.mouseButtons:
			self.oldmouseButtons=self.mouseButtons
			self.mouseButtons = pygame.mouse.get_pressed()
		else:
			self.mouseButtons = pygame.mouse.get_pressed()
		self.mousePos = pygame.mouse.get_pos()

inputs = HandleEvent()