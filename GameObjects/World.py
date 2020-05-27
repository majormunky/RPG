import pygame
from Engine.Grid import Grid


class World:
	def __init__(self, world_data):
		self.data = world_data
		self.map = None
		self.load_map("world")
	
	def load_map(self, map_name):
		if map_name in self.data.keys():
			self.map = Map(self.data[map_name])

	def get_rect(self):
		if self.map:
			return self.map.get_rect()
		return None

	def get_tile_at_rect(self, rect):
		return self.map.get_tile_at_pos(rect.x, rect.y)

	def update(self, dt):
		pass

	def draw(self, canvas, camera):
		canvas.blit(self.map.image, (0, 0), camera)

	def handle_event(self, event):
		pass



class Map:
	def __init__(self, data):
		self.tile_size = data.get("tile_size")
		self.grid = Grid(data.get("grid"))
		self.tile_info = data.get("tile_info")
		self.image = None
		self.render()

	def render(self):
		self.image = pygame.Surface((self.grid.width * self.tile_size, self.grid.height * self.tile_size), pygame.SRCALPHA)
		for y in range(self.grid.height):
			for x in range(self.grid.width):
				cell_type = self.grid.get_cell(x, y)
				cell_info = self.tile_info.get(cell_type, None)
				if cell_info:
					pygame.draw.rect(
						self.image, 
						cell_info.get("color"), 
						(
							x * self.tile_size, 
							y * self.tile_size, 
							self.tile_size, 
							self.tile_size
						)
					)

	def get_width(self):
		return self.grid.width * self.tile_size

	def get_height(self):
		return self.grid.height * self.tile_size

	def get_rect(self):
		return pygame.Rect(0, 0, self.get_width(), self.get_height())

	def pixel_to_tile(self, val):
		return val // self.tile_size

	def get_tile_at_pos(self, x, y):
		tx = self.pixel_to_tile(x)
		ty = self.pixel_to_tile(y)
		tile_info = self.grid.get_cell(tx, ty)
		return self.tile_info.get(tile_info, None)

