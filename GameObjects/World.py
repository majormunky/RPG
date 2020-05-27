import pygame
from Engine.Grid import Grid


class World:
	def __init__(self):
		self.tile_size = 32
		self.grid = Grid([
			["0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0"],
			["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
			["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
			["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
			["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
			["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
			["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
			["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
			["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
			["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
		])
		self.tile_info = {
			"0": {
				"color": (0, 200, 0),
				"solid": False
			},
			"1": {
				"color": (100, 100, 100),
				"solid": True
			}
		}
		self.image = None
		self.render_map()

	def get_width(self):
		return self.grid.width * self.tile_size

	def get_height(self):
		return self.grid.height * self.tile_size

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

	def draw(self, canvas):
		canvas.blit(self.image, (0, 0))

	def handle_event(self, event):
		pass
