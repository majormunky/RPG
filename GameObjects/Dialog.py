import pygame
from Engine.Config import get_screenrect


class Dialog:
	def __init__(self):
		self.screenrect = get_screenrect()
		self.padding = 16
		self.dialog_rect = pygame.Rect(
			self.padding, 
			self.padding, 
			self.screenrect.width - (self.padding * 2), 
			self.screenrect.height // 2
		)
		self.image = None
		self.active = False
		self.render()

	def render(self):
		self.image = pygame.Surface((self.screenrect.width, self.screenrect.height), pygame.SRCALPHA)
		self.image.fill((100, 100, 100, 128))
		pygame.draw.rect(self.image, (0, 0, 200), self.dialog_rect)

	def update(self, dt):
		pass

	def toggle(self):
		self.active = not self.active

	def draw(self, canvas):
		canvas.blit(self.image, (0, 0))

	def handle_event(self, event):
		pass