import pygame
from Engine.Engine import Engine
from Engine.Camera import Camera
from Engine.Grid import Grid
from Engine.Config import get_screenrect
from GameObjects.World import World
from GameObjects.Player import Player
from GameObjects.GameMenu import GameMenu
from GameObjects import Data


class Game:
	def __init__(self):
		self.screenrect = get_screenrect()
		self.world = World(Data.world_data)
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
		world_rect = self.world.get_rect()

		if not self.screenrect.contains(rect):
			print("Player is going to be off of the screen, returning false")
			return False

		if fixed_rect.right > world_rect.width or fixed_rect.bottom > world_rect.height:
			print("Player is going to be outside of the world, returning false")
			return False

		tile = self.world.get_tile_at_rect(fixed_rect)

		if tile["solid"]:
			print("Player tried to walk on a solid tile, returning false")
			return False
		teleport_tile = self.world.is_teleport_tile(tile)
		if teleport_tile:
			self.teleport(teleport_tile)
			return

		camera_rect = self.camera.get_rect()
		has_moved = False
		if world_rect.contains(rect):
			if direction == "right":
				if rect.right > self.screenrect.width - self.map_pad:
					# player is in an area where we should scroll the camera
					camera_moved = self.camera.move(camera_rect, world_rect, 32, direction)
					if not camera_moved:
						has_moved = True
				else:
					has_moved = True
			if direction == "left":
				if rect.x < self.map_pad:
					# player is in an area where we should scroll the camera
					camera_moved = self.camera.move(camera_rect, world_rect, 32, direction)
					if not camera_moved:
						has_moved = True
				else:
					has_moved = True
			if direction == "up":
				if rect.y < self.map_pad:
					# player is in an area where we should scroll the camera
					camera_moved = self.camera.move(camera_rect, world_rect, 32, direction)
					if not camera_moved:
						has_moved = True
				else:
					has_moved = True
			if direction == "down":
				if rect.bottom > self.screenrect.bottom - self.map_pad:
					# player is in an area where we should scroll the camera
					camera_moved = self.camera.move(camera_rect, world_rect, 32, direction)
					if not camera_moved:
						has_moved = True
				else:
					has_moved = True
		return has_moved

	def teleport(self, to):
		print("TELEPORT: ", to)
		old_map = self.world.map_name
		self.world.load_map(to)
		new_player_pos = self.world.get_teleport_from(old_map)
		self.player.x = new_player_pos[0] * 32
		self.player.y = new_player_pos[1] * 32

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
