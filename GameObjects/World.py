import pygame
from Engine.Grid import Grid


class World:
	def __init__(self, world_data):
		self.data = world_data
		self.map = None
		self.map_name = None
		self.load_map("world")
	
	def load_map(self, map_name):
		if map_name in self.data.keys():
			self.map_name = map_name
			self.map = Map(self.data[map_name])

	def get_rect(self):
		if self.map:
			return self.map.get_rect()
		return None

	def get_tile_at_rect(self, rect):
		return self.map.get_tile_at_pos(rect.x, rect.y)

	def get_tiles_at(self, rect):
		rect = rect.inflate(-2, -2)
		return [
			self.map.get_tile_at_pos(rect.x, rect.y),
			self.map.get_tile_at_pos(rect.right, rect.y),
			self.map.get_tile_at_pos(rect.x, rect.bottom),
			self.map.get_tile_at_pos(rect.right, rect.bottom),
		]

	def update(self, dt):
		pass

	def draw(self, canvas, camera):
		canvas.blit(self.map.image, (0, 0), camera)

	def handle_event(self, event):
		pass

	def is_teleport_tile(self, tile):
		return self.map.is_teleport_tile(tile["key"])

	def get_teleport_from(self, map_name):
		return self.map.teleport_from.get(map_name, None)



class Map:
	def __init__(self, data):
		self.teleport_to = data.get("teleport_to", None)
		self.teleport_from = data.get("teleport_from", None)
		self.tile_size = data.get("tile_size")
		self.grid = Grid(data.get("grid"))
		self.tile_info = data.get("tile_info")
		self.image = None
		self.render()

	def render(self):
		self.image = pygame.Surface((self.grid.width * self.tile_size, self.grid.height * self.tile_size), pygame.SRCALPHA)
		half_tile = self.tile_size // 2
		for y in range(self.grid.height):
			for x in range(self.grid.width):
				cell_key = (x, y)
				cell_type = self.grid.get_cell(x, y)
				cell_info = self.tile_info.get(cell_type, None)
				if cell_info:
					px = x * self.tile_size
					py = y * self.tile_size
					pygame.draw.rect(
						self.image, 
						cell_info.get("color"), 
						(px, py, self.tile_size, self.tile_size)
					)
					if cell_key in self.teleport_to.keys():
						pygame.draw.circle(
							self.image,
							(200, 0, 200),
							(px + half_tile, py + half_tile),
							half_tile
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
		tile_type = self.grid.get_cell(tx, ty)
		tile_data = self.tile_info.get(tile_type, None)
		if tile_data:
			tile_data["key"] = (tx, ty)
		return tile_data

	def is_teleport_tile(self, tile_key):
		print("is teleport tile", tile_key)
		if tile_key in self.teleport_to.keys():
			print("It is")
			return self.teleport_to[tile_key]
		print("It is not")
		return False
