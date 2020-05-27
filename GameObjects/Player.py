import pygame


class Player:
	def __init__(self):
		self.width = 32
		self.height = 32
		self.x = 0
		self.y = 0
		self.color = (0, 0, 200)

	def update(self, dt):
		pass

	def draw(self, canvas):
		pygame.draw.rect(canvas, self.color, (self.x, self.y, self.width, self.height))

	def get_rect(self):
		return pygame.Rect(self.x, self.y, self.width, self.height)

	def handle_event(self, event, player_check):
		if event.type == pygame.KEYUP:
			new_rect = self.get_rect()
			if event.key == pygame.K_UP:
				new_rect.y -= self.height
			elif event.key == pygame.K_DOWN:
				new_rect.y += self.height
			elif event.key == pygame.K_LEFT:
				new_rect.x -= self.width
			elif event.key == pygame.K_RIGHT:
				new_rect.x += self.width
			
			if player_check(new_rect):
				self.x = new_rect.x
				self.y = new_rect.y
