import pygame
from Engine.Engine import Engine


class Player:
	def __init__(self):
		self.width = 32
		self.height = 32
		self.x = 0
		self.y = 0

	def update(self, dt):
		pass

	def draw(self, canvas):
		pygame.draw.rect(canvas, (100, 100, 100), (self.x, self.y, self.width, self.height))

	def handle_event(self, event):
		pass


class Game:
	def __init__(self):
		self.player = Player()

	def update(self, dt):
		pass

	def draw(self, canvas):
		self.player.draw(canvas)

	def handle_event(self, event):
		pass


def main():
	e = Engine(Game)
	e.game_loop()


if __name__ == '__main__':
	main()
