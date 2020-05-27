import pygame


class Player:
	def __init__(self):
		self.width = 32
		self.height = 32
		self.x = 0
		self.y = 0
		self.color = (0, 0, 200)
		self.directions = {
			pygame.K_DOWN: "down",
			pygame.K_UP: "up",
			pygame.K_RIGHT: "right",
			pygame.K_LEFT: "left"
		}

	def update(self, dt):
		pass

	def draw(self, canvas, camera):
		pygame.draw.rect(canvas, self.color, (self.x, self.y, self.width, self.height))

	def get_rect(self):
		return pygame.Rect(self.x, self.y, self.width, self.height)

	def handle_event(self, event, player_check):
		direction = None
		if event.type == pygame.KEYUP:
			new_rect = self.get_rect()
			if event.key == pygame.K_UP:
				new_rect.y -= self.height
				direction = self.directions[event.key]
			elif event.key == pygame.K_DOWN:
				new_rect.y += self.height
				direction = self.directions[event.key]
			elif event.key == pygame.K_LEFT:
				new_rect.x -= self.width
				direction = self.directions[event.key]
			elif event.key == pygame.K_RIGHT:
				new_rect.x += self.width
				direction = self.directions[event.key]
			
			if player_check(new_rect, direction):
				self.x = new_rect.x
				self.y = new_rect.y
