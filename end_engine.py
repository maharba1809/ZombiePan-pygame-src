import sprites as sp
import pygame
import var
import random
import time

assetsDir = var.assetsDir

display_width = var.display_width 
display_height = var.display_height
map_gap = var.map_gap
gameDisplay = var.gameDisplay
black = var.black
white = var.white
blue = var.blue

clock = pygame.time.Clock()

def end():
    global engineExit
    endExit = False
    pygame.mixer.music.load(assetsDir + 'Little Swans Game.ogg')
    var.play_music()
    background =  sp.Sprite2( assetsDir + 'end.jpg', 0, 0, display_width, display_height, 0, 0)

    filesRun = [assetsDir + 'Run1.png', assetsDir + 'Run2.png', assetsDir + 'Run3.png', assetsDir + 'Run4.png', assetsDir + 'Run5.png', assetsDir + 'Run6.png']
    height = 77*1
    width = 70*1
    filesRunSize =  (height, width)
    filesDead = [assetsDir + 'Dead1.png', assetsDir + 'Dead2.png', assetsDir + 'Dead3.png', assetsDir + 'Dead4.png', assetsDir + 'Dead5.png', assetsDir + 'Dead6.png', assetsDir + 'Dead7.png',assetsDir + 'Dead8.png']
    filesDeadSize = (96,77)
    files = [filesRun,filesRunSize,filesDead,filesDeadSize]
    
    group_enemies=[]
    group_enemies.append( sp.Sprite3(files, 0, display_height - 20 - height - 20, 5.0, 0))
    group_enemies.append( sp.Sprite3(files, 0, display_height - 20 - height + 0,  9.0, 0))
    group_enemies.append( sp.Sprite3(files, 0, display_height - 20 - height + 10, 8.0, 0))
    group_enemies.append( sp.Sprite3(files, 0, display_height - 20 - height - 20, 8.0, 0))
    group_enemies.append( sp.Sprite3(files, 0, display_height - 20 - height + 0,  5.0, 0))
    group_enemies.append( sp.Sprite3(files, 0, display_height - 20 - height + 15, 4.0, 0))
    group_enemies.append( sp.Sprite3(files, 0, display_height - 20 - height - 20, 3.0, 0))
    group_enemies.append( sp.Sprite3(files, 0, display_height - 20 - height + 10,  2.0, 0))
    group_enemies.append( sp.Sprite3(files, 0, display_height - 20 - height + 15, 3.0, 0))
    
    #KEnemy---------------------------------------------------------------------------------------------------------- 
    filename = ['kz1.png','kz2.png','kz3.png','kz4.png','kz5.png','kz6.png','kz7.png','kz8.png','kz9.png','kz10.png']
    filesRun = []
    for i in filename:
        filesRun.append(assetsDir+i)
    
    filename = ['zd1.png','zd2.png','zd3.png','zd4.png','zd5.png','zd6.png','zd7.png','zd8.png','zd9.png','zd10.png']
    filesDead = []
    for i in filename:
        filesDead.append(assetsDir+i)
    
    filesRunSize = (70,77)
    filesDeadSize = (70,77)
    
    files = [filesRun, filesRunSize, filesDead, filesDeadSize]
    
    y0 = display_height - map_gap - filesRunSize[1]
    group_enemies.append( sp.Sprite3(files, 0, y0 + 10, 2, 0))
    
    y0 = display_height - map_gap - filesRunSize[1]
    group_enemies.append( sp.Sprite3(files, 0, y0 - 10, 3, 0))
    
    while not endExit:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:    
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:    
                    engineExit = True
                    endExit = True
        
        gameDisplay.fill( black )
        var.draw_sprite2( background )        
        
        for enemy in group_enemies:
            if enemy.rect.x == 0 :            
                enemy.rect.x += 2
                mood = 1.5 + random.random()                
                enemy.u = enemy.u * mood 
                if enemy.u > 5:          
                    enemy.u = 2.0
                if enemy.u < 1:          
                    enemy.u = 2.0                
            
            if enemy.rect.x > display_width:
                enemy.rect.x = 0            
            else:                
                var.draw_sprite2(enemy)
                enemy.update()
                enemy.rect.x += enemy.u 
                enemy.rect.y += enemy.v
             
        
        var.draw_selected((0, 20), (display_width,40), 100, white, gameDisplay )
        var.message_display('Thanks.. Danke... Gracias', "monospace", 40, (350, 20), blue)    
        
        pygame.display.update()    
        clock.tick( 60 )
        
