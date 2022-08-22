import pygame
from settings import *
from menu import Menu

class Overlay:
	
	def __init__(self,player):

		# general setup
		self.display_surface = pygame.display.get_surface()
		self.player = player
		self.font = pygame.font.Font( 'assets/font/LycheeSoda.ttf',30)

		# imports 
		overlay_path = 'assets/graphics/overlay/'
		self.tools_surf = {tool: pygame.image.load(f'{overlay_path}{tool}.png').convert_alpha() for tool in player.tools}
		self.seeds_surf = {seed: pygame.image.load(f'{overlay_path}{seed}.png').convert_alpha() for seed in player.seeds}

		money_surf = self.font.render(f'£{self.player.money}',False, 'White')
      

	def display(self):
		money_rect = pygame.display.get_surface()

		# tool
		tool_surf = self.tools_surf[self.player.selected_tool]
		tool_rect = tool_surf.get_rect(midbottom = OVERLAY_POSITIONS['tool'])
		self.display_surface.blit(tool_surf,tool_rect)

		# seeds
		seed_surf = self.seeds_surf[self.player.selected_seed]
		seed_rect = seed_surf.get_rect(midbottom = OVERLAY_POSITIONS['seed'])
		self.display_surface.blit(seed_surf,seed_rect)

		# money
		money_surf = self.font.render(f'£{self.player.money}',False, 'White')
		money_rect = pygame.Rect(20,10,300,0)
		self.display_surface.blit(money_surf, money_rect)
