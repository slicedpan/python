#!/usr/bin/python

from pygame import *

init()
screen = display.set_mode((640,480))
display.set_caption('Test')
backdrop = image.load('test.jpg')

quit = 0

while (quit == 0):
	screen.blit(backdrop, (0,0))
	display.update()
	ourevent = event.wait()
	if ourevent.type == KEYDOWN:
		if ourevent.key == K_ESCAPE:
			quit = 1
