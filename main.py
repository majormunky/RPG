import pygame
from Engine.Engine import Engine
from Engine.Grid import Grid
from Engine.Config import get_screenrect
from GameObjects.World import World
from GameObjects.Player import Player


class Game:
	def __init__(self):
		self.screenrect = get_screenrect()
		self.world = World()
		self.player = Player()

	def update(self, dt):
		pass

	def draw(self, canvas):
		self.world.draw(canvas)
		self.player.draw(canvas)

	def check_player_position(self, rect):
		if rect.x < 0 or rect.y < 0:
			return False

		if rect.right > self.world.get_width() or rect.bottom > self.world.get_height():
			return False

		tile_info = self.world.get_tile_at_rect(rect)
		if tile_info["solid"]:
			return False

		if rect.bottom > self.screenrect.bottom:
			return False

		if rect.right > self.screenrect.right:
			return False

		return True

	def handle_event(self, event):
		self.player.handle_event(event, self.check_player_position)


def main():
	e = Engine(Game)
	e.game_loop()


if __name__ == '__main__':
	main()
