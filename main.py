import pygame
from Engine.Engine import Engine
from Engine.Grid import Grid


class World:
	def __init__(self):
		self.tile_width = 32
		self.tile_height = 32
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
		return self.grid.width * self.tile_width

	def get_height(self):
		return self.grid.height * self.tile_height

	def render_map(self):
		self.image = pygame.Surface((
			self.tile_width * self.grid.width,
			self.tile_height * self.grid.height,
		), pygame.SRCALPHA)
		for y in range(self.grid.height):
			for x in range(self.grid.width):
				cell_type = self.grid.get_cell(x, y)
				cell_info = self.tile_info.get(cell_type, None)
				if cell_info:
					pygame.draw.rect(self.image, cell_info["color"], (x * self.tile_width, y * self.tile_height, self.tile_width, self.tile_height))


	def update(self, dt):
		pass

	def draw(self, canvas):
		canvas.blit(self.image, (0, 0))

	def handle_event(self, event):
		pass


class Player:
	def __init__(self):
		self.width = 32
		self.height = 32
		self.x = 0
		self.y = 0
		self.color = (0, 0, 200)

	def update(self, dt):
		pass

	def draw(self, canvas):
		pygame.draw.rect(canvas, self.color, (self.x, self.y, self.width, self.height))

	def get_rect(self):
		return pygame.Rect(self.x, self.y, self.width, self.height)

	def handle_event(self, event, player_check):
		if event.type == pygame.KEYUP:
			new_rect = self.get_rect()
			if event.key == pygame.K_UP:
				new_rect.y -= self.height
			elif event.key == pygame.K_DOWN:
				new_rect.y += self.height
			elif event.key == pygame.K_LEFT:
				new_rect.x -= self.width
			elif event.key == pygame.K_RIGHT:
				new_rect.x += self.width
			
			if player_check(new_rect):
				self.x = new_rect.x
				self.y = new_rect.y


class Game:
	def __init__(self):
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

		return True

	def handle_event(self, event):
		self.player.handle_event(event, self.check_player_position)


def main():
	e = Engine(Game)
	e.game_loop()


if __name__ == '__main__':
	main()
