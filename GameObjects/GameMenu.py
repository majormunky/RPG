import pygame
from Engine.Config import get_screenrect
from Engine.Text import text_surface
from Engine.MenuWidget import MenuWidget


class GameMenu:
	def __init__(self):
		self.screenrect = get_screenrect()
		self.image = None
		self.active = False
		self.menu = MenuWidget([
			"Status",
			"Quests",
			"Magic",
			"Equipment"
		], 20, 20, text_color=(255, 255, 255))
		self.render()

	def render(self):
		self.image = pygame.Surface((self.screenrect.width, self.screenrect.height), pygame.SRCALPHA)
		self.image.fill((0, 0, 200))
		main_title = text_surface("RPG Game", font_size=32, color=(255, 255, 255))
		main_title_width = main_title.get_rect().width
		center_x = (self.screenrect.width - main_title_width) // 2
		self.image.blit(main_title, (center_x, 20))
		self.menu.draw(self.image)

	def toggle(self):
		self.active = not self.active

	def update(self, dt):
		pass

	def on_menu_change(self, item):
		self.menu.render_images()
		self.render()

	def draw(self, canvas):
		canvas.blit(self.image, (0, 0))

	def handle_event(self, event):
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RETURN:
				current_item = self.menu.get_current_item()
				print(current_item)
			else:
				self.menu.handle_key(event.key, self.on_menu_change)
