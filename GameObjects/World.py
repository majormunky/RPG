import pygame
from Engine.Grid import Grid


class World:
	def __init__(self, world_data):
		self.data = world_data
		self.tile_size = None
		self.grid = None
		self.image = None
		self.tile_info = None
		self.load_map("world")
	
	def load_map(self, map_name):
		if map_name in self.data.keys():
			self.tile_size = self.data[map_name]["tile_size"]
			self.grid = Grid(self.data[map_name]["grid"])
			self.tile_info = self.data[map_name]["tile_info"]
			self.render_map()

	def get_width(self):
		return self.grid.width * self.tile_size

	def get_height(self):
		return self.grid.height * self.tile_size

	def get_rect(self):
		return pygame.Rect(0, 0, self.get_width(), self.get_height())

	def render_map(self):
		self.image = pygame.Surface((
			self.tile_size * self.grid.width,
			self.tile_size * self.grid.height,
		), pygame.SRCALPHA)
		for y in range(self.grid.height):
			for x in range(self.grid.width):
				cell_type = self.grid.get_cell(x, y)
				cell_info = self.tile_info.get(cell_type, None)
				if cell_info:
					pygame.draw.rect(
						self.image, 
						cell_info["color"], 
						(
							x * self.tile_size, 
							y * self.tile_size, 
							self.tile_size, 
							self.tile_size
						)
					)


	def get_tile_at_rect(self, rect):
		tx = self.pixel_to_tile(rect.x)
		ty = self.pixel_to_tile(rect.y)
		tile_info = self.grid.get_cell(tx, ty)
		return self.tile_info.get(tile_info, None)

	def pixel_to_tile(self, val):
		return val // self.tile_size

	def update(self, dt):
		pass

	def draw(self, canvas, camera):
		canvas.blit(self.image, (0, 0), camera)

	def handle_event(self, event):
		pass
