import pygame
import menu

print('Loading main')
gameExit = False
menuScreen = menu.AddScreen()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    menuScreen.run()

