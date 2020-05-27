import pygame
from Engine.Engine import Engine
from Engine.Camera import Camera
from Engine.Grid import Grid
from Engine.Config import get_screenrect
from GameObjects.World import World
from GameObjects.Player import Player


class Game:
	def __init__(self):
		self.screenrect = get_screenrect()
		self.world = World()
		self.player = Player()
		self.camera = Camera()

		# figure out where this should go
		self.map_pad = 128

	def update(self, dt):
		pass

	def draw(self, canvas):
		camera_rect = self.camera.get_rect()
		self.world.draw(canvas, camera_rect)
		self.player.draw(canvas, camera_rect)

	def check_player_position(self, rect):
		fixed_rect = pygame.Rect(
			rect.x + self.camera.x,
			rect.y + self.camera.y,
			rect.width,
			rect.height
		)

		if not self.screenrect.contains(fixed_rect):
			return False

		if fixed_rect.right > self.world.get_width() or fixed_rect.bottom > self.world.get_height():
			return False

		tile_info = self.world.get_tile_at_rect(fixed_rect)
		if tile_info["solid"]:
			return False

		return True

	def handle_event(self, event):
		self.player.handle_event(event, self.check_player_position)


def main():
	e = Engine(Game)
	e.game_loop()


if __name__ == '__main__':
	main()
