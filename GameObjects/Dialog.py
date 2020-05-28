import pygame
from Engine.Config import get_screenrect
from Engine.Text import text_surface


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
		self.lines = None
		self.render_lines(["test", "test2"])

	def render(self):
		self.image = pygame.Surface((self.screenrect.width, self.screenrect.height), pygame.SRCALPHA)
		self.image.fill((100, 100, 100, 128))
		pygame.draw.rect(self.image, (0, 0, 200), self.dialog_rect)

		x = self.dialog_rect.x + self.padding
		y = self.dialog_rect.y + self.padding

		for line in self.lines:
			text = text_surface(line, font_size=32)
			self.image.blit(text, (x, y))
			y += text.get_rect().height + self.padding

	def render_lines(self, lines):
		self.lines = lines
		self.render()

	def update(self, dt):
		pass

	def toggle(self):
		self.active = not self.active

	def draw(self, canvas):
		canvas.blit(self.image, (0, 0))

	def handle_event(self, event):
		pass