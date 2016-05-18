import pygame
from pygame.locals import *
from ProgramEvent import *
from Screen import *
class Gray:
	def __init__(self, color='gray'):
		self.x=0
		self.y=0
		self.image=pygame.image.load('..\\res\\image\\system\\back\\'+color+'.png').convert_alpha()
	def cut(self,w,h):
		return self.image.subsurface((0,0),(w,h))
class Button:
	def __init__(self, x=0, y=0, text='Button', ftext='Button', size=30, color=(0,200,0), font='Font'):
		self.x=x
		self.y=y
		self.text=text
		self.ftext = text
		fontstyle=pygame.font.Font(font, size)
		self.image_back=fontstyle.render(text,True,(255,255,255))
		self.image_row=fontstyle.render(text,True,color)
		self.image_on=fontstyle.render(text,True,tuple(x/2 for x in color))
		self.image_pressed=fontstyle.render(text,True,tuple(x/4 for x in color))
		self.w,self.h=self.image_back.get_size()
		self.status='row'
		self.shadow=size/15
		self.kind=1
		self.disable = False
	def draw(self):
		if self.disable:
			return
		screen.blit(self.image_back,(self.x,self.y))
		if self.status=='row':screen.blit(self.image_row,(self.x+self.shadow,self.y+self.shadow))
		if self.status=='on':screen.blit(self.image_on,(self.x+self.shadow,self.y+self.shadow))
		if self.status=='pressed':screen.blit(self.image_pressed,(self.x+self.shadow*7/10,self.y+self.shadow*7/10))

class Button_Image(Button):
	def __init__(self, x=0, y=0, text='IButton', ftext='IButton'):
		self.x=x
		self.y=y
		self.ftext = text
		self.image_back=Gray(color = 'gray').cut(190,50)
		self.image_white=Gray(color = 'white').cut(190,50)
		self.w,self.h=self.image_back.get_size()
		self.image_row=pygame.image.load('..\\res\\image\\system\\button\\button.png').convert_alpha()
		fontstyle = pygame.font.Font("..\\res\\font\\ls.ttf", 35)
		image_temp = fontstyle.render(text, True, (222, 222, 222))
		x_temp =100 - len(text)*20
		self.image_row.blit(image_temp,(x_temp, 10))

		self.w,self.h=self.image_back.get_size()
		self.status='row'
		self.shadow=6
		self.kind=2
		self.disable = False
	def draw(self):
		if self.disable:
			return
		screen.blit(self.image_back,(self.x+self.shadow,self.y+self.shadow))
		if self.status=='row':screen.blit(self.image_row,(self.x,self.y))
		else:
			screen.blit(self.image_row,(self.x,self.y))
			screen.blit(self.image_white,(self.x,self.y))

class Button_RealImage(Button):
	def __init__(self, x=0, y=0, ftext='RIButton', fname='hhw'):
		self.x = x
		self.y = y
		self.ftext = ftext
		self.fname = fname
		self.status = 'disabled'
		self.image_normal = pygame.image.load('..\\res\\image\\system\\button\\irregular\\'+fname+'-normal.png').convert_alpha()
		self.image_hover = pygame.image.load('..\\res\\image\\system\\button\\irregular\\'+fname+'-hover.png').convert_alpha()
		self.image_down = pygame.image.load('..\\res\\image\\system\\button\\irregular\\'+fname+'-down.png').convert_alpha()
		self.image_disabled = pygame.image.load('..\\res\\image\\system\\button\\irregular\\'+fname+'-disabled.png').convert_alpha()
		self.w, self.h = self.image_normal.get_size()
		self.disable = False
	def draw(self):
		if self.status == 'normal':
			screen.blit(self.image_normal, (self.x, self.y))
		elif self.status == 'hover':
			screen.blit(self.image_hover, (self.x, self.y))
		elif self.status == 'down':
			screen.blit(self.image_down, (self.x, self.y))
		elif self.status == 'disabled':
			screen.blit(self.image_disabled, (self.x, self.y))

class Buttons:
	def __init__(self):
		self.blst = []
		self.pressed = ''

	def add(self, button):
		self.blst.append(button)

	def update(self):
		#ipt.update()
		mouse_x,mouse_y = pygame.mouse.get_pos()
		for button in self.blst:
			if button.disable:
				continue
			if (button.x < mouse_x < button.x+button.w) and (button.y < mouse_y < button.y+button.h):
				if inputs.mousepressed[1]:
					button.status='pressed'
				else:
					if inputs.mouseclick[1]:
						self.pressed = button.ftext
						continue
					button.status='on'
			else:
				button.status='row'

	def draw(self):
		for button in self.blst:
			button.draw()

	def disable(self, s):
		for button in self.blst:
			if button.ftext == s:
				button.disable = True
				break

class PlayerButtons:
	def __init__(self):
		self.blst = []
		self.pressed = ''

	def add(self, button):
		self.blst.append(button)

	def update(self):
		mouse_x,mouse_y = pygame.mouse.get_pos()
		for button in self.blst:
			if button.status != 'disabled':
				if (button.x < mouse_x < button.x+button.w) and (button.y < mouse_y < button.y+button.h):
					if inputs.mousepressed[1]:
						button.status='down'
					else:
						if inputs.mouseclick[1]:
							self.pressed = button.ftext
							#button.event()
							continue
						button.status='hover'
				else:
					button.status='normal'

	def draw(self):
		for button in self.blst:
			button.draw()

