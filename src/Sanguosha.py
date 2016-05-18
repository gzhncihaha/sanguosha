# -*- coding: utf-8 -*- 
import os,sys
import pygame
from pygame.locals import *
from ProgramEvent import *
from Scene import *
from ToServer import *

if __name__ == "__main__":

	pygame.init()
	screen.initialize()
	inputs.initialize()
	communicater.initialize("192.168.19.1", 5001)
	Scene = Scene_Title()
	while Scene != None:
		Scene = Scene.main()