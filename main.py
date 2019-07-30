
if __name__ == "__main__":
    print('Loading main')
    
    import pygame
    import menu
    
    gameExit = False
    menuScreen = menu.AddScreen()
    menuScreen.run()
    pygame.display.quit()
    pygame.quit()
    
