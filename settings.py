import pygame
pygame.font.init()
class Settings():
	def __init__(self):
		self.screen_width=400
		self.screen_height=450
		self.bg_color=(187, 173, 160)
		self.cell_color=(205, 193, 180)
		self.cell_width=self.screen_width//4
		self.cell_height=self.cell_width
		self.text_color=(255,255,255)
		self.font=pygame.font.SysFont("arialblack", 32)
		self.end_font=pygame.font.SysFont("arialblack", 52)