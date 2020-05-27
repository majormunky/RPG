import pygame
from Engine.Engine import Engine
from Engine.Camera import Camera
from Engine.Grid import Grid
from Engine.Config import get_screenrect
from GameObjects.World import World
from GameObjects.Player import Player
from GameObjects.GameMenu import GameMenu


class Game:
	def __init__(self):
		self.screenrect = get_screenrect()
		self.world = World()
		self.player = Player()
		self.camera = Camera()
		self.menu = GameMenu()

		# figure out where this should go
		self.map_pad = 128

	def update(self, dt):
		pass

	def draw(self, canvas):
		if self.menu.active:
			self.menu.draw(canvas)
		else:
			camera_rect = self.camera.get_rect()
			self.world.draw(canvas, camera_rect)
			self.player.draw(canvas, camera_rect)

	def check_player_position(self, rect, direction):
		print("checking player position")
		fixed_rect = pygame.Rect(
			rect.x + self.camera.x,
			rect.y + self.camera.y,
			rect.width,
			rect.height
		)

		if not self.screenrect.contains(rect):
			print("Player is going to be off of the screen, returning false")
			return False

		if fixed_rect.right > self.world.get_width() or fixed_rect.bottom > self.world.get_height():
			print("Player is going to be outside of the world, returning false")
			return False

		tile_info = self.world.get_tile_at_rect(fixed_rect)
		if tile_info["solid"]:
			print("Player tried to walk on a solid tile, returning false")
			return False

		map_rect = self.world.get_rect()
		camera_rect = self.camera.get_rect()
		has_moved = False
		if map_rect.contains(rect):
			if direction == "right":
				if rect.right > self.screenrect.width - self.map_pad:
					# player is in an area where we should scroll the camera
					camera_moved = self.camera.move(camera_rect, map_rect, 32, direction)
					if not camera_moved:
						has_moved = True
				else:
					has_moved = True
			if direction == "left":
				if rect.x < self.map_pad:
					# player is in an area where we should scroll the camera
					camera_moved = self.camera.move(camera_rect, map_rect, 32, direction)
					if not camera_moved:
						has_moved = True
				else:
					has_moved = True
			if direction == "up":
				if rect.y < self.map_pad:
					# player is in an area where we should scroll the camera
					camera_moved = self.camera.move(camera_rect, map_rect, 32, direction)
					if not camera_moved:
						has_moved = True
				else:
					has_moved = True
			if direction == "down":
				if rect.bottom > self.screenrect.bottom - self.map_pad:
					# player is in an area where we should scroll the camera
					camera_moved = self.camera.move(camera_rect, map_rect, 32, direction)
					if not camera_moved:
						has_moved = True
				else:
					has_moved = True
		return has_moved

	def handle_event(self, event):
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_TAB:
				self.menu.toggle()
				return
		if self.menu.active:
			self.menu.handle_event(event)
		else:
			self.player.handle_event(event, self.check_player_position)


def main():
	e = Engine(Game)
	e.game_loop()


if __name__ == '__main__':
	main()
