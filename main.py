import pygame
import menu

print('Loading main')
gameExit = False
menuScreen = menu.AddScreen()
menuScreen.run()
pygame.display.quit()
pygame.quit()