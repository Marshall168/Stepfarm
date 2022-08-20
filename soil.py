import pygame
from settings import *
from pytmx.util_pygame import load_pygame

class SoilLayer:
    def __init__(self, all_sprites):

        #sprite groups
        self.all_sprites = all_sprites
        self.soil_sprites = pygame.sprite.Group()

        #graphics
        self.soil_surf = pygame.image.load('assets/graphics/soil/o.png')
        self.create_soil_grid()


    def create_soil_grid(self):
        ground = pygame.image.load('assets/graphics/world/ground.png')
        h_tiles, v_tiles = ground.get_width() // TILE_SIZE, ground.get_height() // TILE_SIZE

        self.grid = [[[] for col in range (h_tiles)] for row in range (v_tiles)]
        for x, y, _ in load_pygame('assets/data/map.tmx').get_layer_by_name('Farmable').tiles():
            self.grid[y][x].append('F')


    def create_hit_rects(self):
        self.hit_rects = []
        for index_row, row in enumerate(self.grid):
            for index_col, cell in enumerate(row):
                if 'F' in cell:
                    x = index_col * TILE_SIZE
                    y = index_row * TILE_SIZE
                    rect = pygame.Rect(x,y,TILE_SIZE,TILE_SIZE)
                    self.hit_rects.append(rect)


