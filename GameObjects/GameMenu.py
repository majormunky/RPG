import pygame
from Engine.Config import get_screenrect
from Engine.Text import text_surface
from Engine.MenuWidget import MenuWidget


class GameMenu:
	def __init__(self):
		self.screenrect = get_screenrect()
		self.image = None
		self.active = False
		self.menu_items = [
			"Status",
			"Quests",
			"Magic",
			"Equipment"
		]
		self.menu_width = 200
		self.page_width = self.screenrect.width - self.menu_width
		self.padding = 16
		self.menu = MenuWidget(
			self.menu_items, 
			self.page_width, 
			20, 
			text_color=(255, 255, 255),
			font_size=32
		)
		self.render()

	def draw_menu_page(self, page_name):
		print("Drawing menu page: ", page_name)
		if page_name == "Status":
			self.draw_status_page()
		elif page_name == "Quests":
			self.draw_quests_page()
		elif page_name == "Magic":
			self.draw_magic_page()
		elif page_name == "Equipment":
			self.draw_equipment_page()

	def draw_title(self, title):
		y_pos = self.padding
		title = text_surface(title, font_size=40, color=(255, 255, 255))
		self.image.blit(title, (self.padding, self.padding))
		y_pos += title.get_rect().height
		pygame.draw.line(
			self.image, 
			(255, 255, 255), 
			(self.padding, y_pos), (self.page_width - (self.padding * 2), y_pos), 
			2
		)

	def draw_status_page(self):
		self.draw_title("Status")

	def draw_quests_page(self):
		self.draw_title("Quests")

	def draw_magic_page(self):
		self.draw_title("Magic")

	def draw_equipment_page(self):
		self.draw_title("Equipment")

	def render(self):
		self.image = pygame.Surface((self.screenrect.width, self.screenrect.height), pygame.SRCALPHA)
		self.image.fill((0, 0, 200))
		self.menu.draw(self.image)
		selected_item = self.menu.get_current_item()
		self.draw_menu_page(selected_item)

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
			else:
				self.menu.handle_key(event.key, self.on_menu_change)
