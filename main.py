
import pygame
import menu

if __name__ == "__main__":
    print('Loading main')
    gameExit = False
    menuScreen = menu.AddScreen()
    menuScreen.run()
    pygame.display.quit()
    pygame.quit()
    
