import pygame
import defaults as df

print('Loading vars')
assetsDir = 'assets/'

map_gap = df.display_height * 0.08

gameDisplay = pygame.display.set_mode( (  df.display_width, df.display_height ) )

fps = 30

map_settings = [ "", 0,assetsDir + "map1.jpg", 0]

clock = pygame.time.Clock()
total = 10