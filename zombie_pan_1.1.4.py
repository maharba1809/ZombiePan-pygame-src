import pygame
import time
import random
import re
import os
import os.path
import sprites as sp
#import pause as pse
#import functions as f
#defined as globals
import var

assetsDir = var.assetsDir
import end_engine as ee

#check if folder exists
if not os.path.isdir(assetsDir):
    print ("No folder assets was found", assetsDir)
    pygame.quit()
    quit()


pygame.init()
#audio definition
pygame.mixer.music.load(assetsDir + 'Little Swans Game.ogg')
pygame.display.set_icon( pygame.image.load(assetsDir + 'icon_zombie.png')) 
pygame.mixer.pre_init(frequency=44100, size=-32, channels=2, buffer=4096)
sound_bullet = pygame.mixer.Sound(file = assetsDir + 'single_water_drop.ogg')
sound_bullet.set_volume(0.5)
sound_col = pygame.mixer.Sound(file = assetsDir + 'comical_liquid_gel_splat.ogg')
sound_col.set_volume(0.5)
sound_err = pygame.mixer.Sound(file = assetsDir + '327736__distillerystudio__error-03.ogg')
sound_err.set_volume(0.5)
sound_hel = pygame.mixer.Sound(file = assetsDir + 'helicopter.ogg')
sound_hel.set_volume(0.2)
sound_loser = pygame.mixer.Sound(file = assetsDir + '113988__kastenfrosch__verloren.ogg')
sound_hel.set_volume(0.5)
sound_winer = pygame.mixer.Sound(file = assetsDir + '270528littlerobotsoundfactoryjingle-win-00.ogg')
sound_winer.set_volume(0.5)

#display dimensions
display_width = 800
display_height = 600

#colors
black = ( 0, 0, 0 )
white = ( 255, 255, 255 )
red = ( 255 , 0, 0 )
blue = ( 0,191,255 )
orange = (255,69,0)
gold = (255,215,0)
green = (124,252,0)
violet = (138,43,226)
gray = (112,128,144)

gameDisplay = pygame.display.set_mode( (  display_width, display_height ) )
pygame.display.set_caption('Zombie Pan')
#mapas settings NULL, gap map, name, level
map_settings = [ "", 0,assetsDir + "map1.jpg", 0]

clock = pygame.time.Clock()

#engine flags
engineExit = False
gameExit = False
menuExit = False
infoExit = False
mapExit = False
adjExit = False
#default audio options
music_enabled = True
sound_enabled = True

#default number of zombies
total = 15



def draw_selected(pos, dim, alpha, color, gameDisplay ):
    s = pygame.Surface(dim)  
    s.set_alpha(alpha)
    s.fill(color)                            
    gameDisplay.blit(s, pos)    
        
def draw_sprite( sprite ):
     gameDisplay.blit( sprite.surface, (sprite.x, sprite.y ))
     
     
def draw_sprite2( sprite ):
     gameDisplay.blit( sprite.image, (sprite.rect.x, sprite.rect.y ))
    
def message_display(text, typefont, size, center,color):
    myfont = pygame.font.SysFont(typefont, size )
    label = myfont.render(text, 1, color)    
    gameDisplay.blit(label,center)
    
    #time.sleep(2)
       
   

def play_music():
    
    if music_enabled:
        pygame.mixer.stop()
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
    else:
        pygame.mixer.music.pause()
    
#---------------------------------------------------------------------------------------    
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------    
#---------------------------------------------------------------------------------------

def pause_loop():
    global engineExit
    global menuExit
    pauseExit = False
    global assetsDir    
    print(engineExit)
    mapsback = sp.Sprite2(assetsDir + 'maps_board.jpg', 0, 0, display_width, display_height, 0, 0)
    btns = []    
    btns.append( sp.Sprite2(assetsDir + "Button_play.png", display_width * 0.5 - 100, display_height * 0.5 - 100, 80, 80, 0, 0))
    btns.append( sp.Sprite2(assetsDir + "Buttonmenu.png", btns[0].rect.x, btns[0].rect.y + btns[0].rect.h + 10, 80, 80, 0, 0))
    btns.append( sp.Sprite2(assetsDir + "Button_cancel.png",  btns[1].rect.x, btns[1].rect.y + btns[1].rect.h + 10, 80, 80, 0, 0))
    
    while not pauseExit:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:                                
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pauseExit = True
        
        gameDisplay.fill( black )
        draw_sprite2(mapsback)
        for m in btns:
            draw_sprite2(m)
            
            if (m.rect.collidepoint(pygame.mouse.get_pos()) == 1):
                               
                draw_selected((m.rect.x + m.rect.w + 10, m.rect.y + m.rect.h*0.5 - 10), (display_width, 30), 100, white, gameDisplay )
                if re.search("play", m.file, flags=0):
                    
                    message_display( "Play" ,"monospace", 30, (m.rect.x + m.rect.w + 10, m.rect.y + m.rect.h*0.5 - 10), black) 
                if re.search("menu", m.file, flags=0):                    
                    message_display( "Main Menu" ,"monospace", 30, (m.rect.x + m.rect.w + 10, m.rect.y + m.rect.h*0.5 - 10), gray) 
                if re.search("cancel", m.file, flags=0):
                    message_display( "Exit Game" ,"monospace", 30, (m.rect.x + m.rect.w + 10, m.rect.y + m.rect.h*0.5 -10), red)                                 
                
                if pygame.mouse.get_pressed()[0]:
                    if re.search("play", m.file, flags=0):
                        pauseExit = True
                    
                    if re.search("menu", m.file, flags=0):
                        engineExit = True
                        pauseExit = True
                        menuExit = False
                        
                    if re.search("cancel", m.file, flags=0):
                        pygame.quit()
                        quit()
        draw_selected((0, btns[0].rect.y - btns[0].rect.h - 5), (display_width,30), 100, white,gameDisplay )
        message_display("Pause", "monospace", 30, (btns[0].rect.x, btns[0].rect.y - btns[0].rect.h - 5), gold) 
        
        pygame.display.update()
        

    
#---------------------------------------------------------------------------------------    
#---------------------------------------------------------------------------------------
#main engine loop where the game starts running
#

def engine_loop():
    
    global engineExit 
    global menuExit
    global mapExit
    
    
    pygame.mixer.music.load(assetsDir + 'helicopter.ogg')
    play_music()
    #print('engine started')
    
    background =  sp.Sprite2( map_settings[2], 0, 0, display_width, display_height, 0, 0)
    map_gap = map_settings[1]

    info_winer = sp.Sprite2(assetsDir + 'enabled.png', display_width*0.5 - 40, display_height*0.5 - 40, 80, 80, 0, 0)
    info_loser = sp.Sprite2(assetsDir + 'disabled.png', display_width*0.5 - 40, display_height*0.5 - 40, 80, 80, 0, 0)
    
    filesRun = [assetsDir + 'Run1.png', assetsDir + 'Run2.png', assetsDir + 'Run3.png', assetsDir + 'Run4.png', assetsDir + 'Run5.png', assetsDir + 'Run6.png']
    filesRunSize =  (70,77)
    filesDead = [assetsDir + 'Dead1.png', assetsDir + 'Dead2.png', assetsDir + 'Dead3.png', assetsDir + 'Dead4.png', assetsDir + 'Dead5.png', assetsDir + 'Dead6.png', assetsDir + 'Dead7.png',assetsDir + 'Dead8.png']
    filesDeadSize = (96,77)
    files = [filesRun,filesRunSize,filesDead,filesDeadSize]

    group_enemies=[]
    group_enemies.append( sp.Sprite3(files, 0, display_height - map_gap - 77 - 10, 2.0, 0))
    group_enemies.append( sp.Sprite3(files, 0, display_height - map_gap - 77 + 0,  2.0, 0))
    group_enemies.append( sp.Sprite3(files, 0, display_height - map_gap - 77 + 10, 2.0, 0))
    group_enemies.append( sp.Sprite3(files, 0, display_height - map_gap - 77 + 5, 5.0, 0))
    
    
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
    #Helicopter----------------------------------------------------------------------------------------------------------
    
    filesHel = [assetsDir + 'helicopter1.png', assetsDir + 'helicopter2.png', assetsDir + 'helicopter3.png', assetsDir + 'helicopter4.png']    
    filesHelSize = (210,62)
    files = [filesHel, filesHelSize, filesHel, filesHelSize] #meandwhile no destructed helicpter is available
    hel = sp.Sprite3(files, 0, 20, 2, 0)

    bullet1 = sp.Sprite2(assetsDir + 'bullet1.png', hel.rect.x, 0, 12, 18, 0, 0 )
    
    #total = 10
    experience = 0
    respawn = 0
    killed = 0
    shelter = 100  
    
    while not engineExit:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:                
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:        
                        hel.u = -5
                    if event.key == pygame.K_RIGHT:        
                        hel.u = 5
                    if event.key == pygame.K_SPACE:                        
                        bullet1.v = 9
                        ran_key = random.random() 
                    if event.key == pygame.K_ESCAPE:                        
                        pause_loop()
                    if event.key == pygame.K_LEFT and event.key == pygame.K_RIGHT:
                        hel.u = 0
                    
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and event.key == pygame.K_RIGHT:
                    helu = 0
            
        
        gameDisplay.fill( black )
        draw_sprite2( background )
       
        #helicopter dynamics
        
        if hel.rect.x + hel.rect.w >= display_width:
            if hel.u > 0:        
                hel.rect.x -= hel.u
                hel.u = -hel.u
                                    
        if hel.rect.x < 0:
            if hel.u<0:
                hel.rect.x -= hel.u
                hel.u = -hel.u
           
            
        draw_sprite2(hel)            
        hel.update() # callls animation def
        hel.rect.x += hel.u
        
        #enemy dynamics
        
        for enemy in group_enemies:
                        
            if enemy.col:
                respawn += 1    # counter
                print('respawn '+str(respawn))                
                enemy.rect.x += 2 # pushes at the begining
                mood = 1.5 + random.random() # random velocity       
                enemy.u = enemy.u * mood 
                if enemy.u > 5: # limit velocity         
                    enemy.u = 4.0
                if enemy.u < 1:
                    enemy.u = 2.0
                enemy.col = False
                            
            #outside of window
            if enemy.rect.x > display_width:
                enemy.rect.x = 0                
                if sound_enabled: sound_err.play()                        
                #killed += 1
                shelter -= 10
            else:             
                #calculates dynamics   
                draw_sprite2(enemy)
                enemy.update()
                enemy.rect.x += enemy.u 
                enemy.rect.y += enemy.v
                
            #Collision detection
            if enemy.rect.colliderect(bullet1.rect):
                if enemy.lived:           
                    if sound_enabled:sound_col.play()
                    bullet1.v = 0  # stops bullet as a flag for restart below
                    killed += 1
                    experience += 1
                    enemy.lived = False # changes status
                    enemy.col = True # collision flag
                    enemy.index = 0 #restarts frame
                    print('killed:',killed)
                    
                
              
        #bullet dynamics
        if bullet1.v == 0:
            bullet1.rect.x = hel.rect.x + hel.rect.w * 0.5
            bullet1.rect.y = hel.rect.y + hel.rect.h * 0.9
            uinert = hel.u
        else:
            bullet1.u = 0.8 * uinert            
            bullet1.rect.x += bullet1.u            
            bullet1.rect.y += bullet1.v 
            
        if bullet1.rect.y > display_height:
            bullet1.v = 0
              
        draw_sprite2( bullet1 )               
        
        #control
        #killed = 10000
        if killed >= total or shelter <= 0:
            
            engineExit = True
            menuExit = True
            mapExit = False
            
            draw_selected( (0, display_height*0.5+50), (display_width,30), 100, white,gameDisplay )
            message_display('Shelter:' + str(int(shelter)) + "%" ,"monospace", 30, (display_width*0.5-100, display_height*0.5+50), violet)
            if shelter > 0 :                
                draw_sprite2(info_winer)
                if sound_enabled: sound_winer.play()
                
                print(map_settings[2])
                if re.search("map14", map_settings[2], flags=0):
                    time.sleep(1)                
                    ee.end()
            else:
                draw_sprite2(info_loser)
                if sound_enabled: sound_loser.play()
            pygame.display.update()
            time.sleep(4)

        draw_selected((0, 0), (display_width,20), 100, white,gameDisplay )
        message_display('Enemies:' + str(total -    killed), "monospace", 20, (0, 0), orange)    
        message_display('Exp:' + str(experience), "monospace", 20, (200, 0), violet)
        message_display('Shelter:' + str(int(shelter)) + "%" ,"monospace", 20, (400, 0), red)

        pygame.display.update()
        clock.tick( 50 )
        
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

def game_maps():
    
    global mapExit 
    global menuExit
    global map_settings
    global engineExit
    global total
    
    #pygame.mixer.music.load(assetsDir + 'WelcomeScreen.mp3')
    play_music()
    
    print('engine maps')
    
    mapsback = sp.Sprite2(assetsDir + 'maps_board.jpg', 0, 0, display_width, display_height, 0, 0)
    maps = []
    maps.append( sp.Sprite2(assetsDir + 'icon_map1.png', 150, 50, 60, 60, 0, 0))
    maps.append( sp.Sprite2(assetsDir + 'icon_map2.png', 300, 50, 60, 60, 0, 0))
    maps.append( sp.Sprite2(assetsDir + 'icon_map3.png', 450, 50, 60, 60, 0, 0))
    maps.append( sp.Sprite2(assetsDir + 'icon_map4.png', 600, 50, 60, 60, 0, 0))
    maps.append( sp.Sprite2(assetsDir + 'icon_map5.png', 150, 150, 60, 60, 0, 0))
    maps.append( sp.Sprite2(assetsDir + 'icon_map6.png', 300, 150, 60, 60, 0, 0))
    maps.append( sp.Sprite2(assetsDir + 'icon_map7.png', 450, 150, 60, 60, 0, 0))
    maps.append( sp.Sprite2(assetsDir + 'icon_map8.png', 600, 150, 60, 60, 0, 0))
    maps.append( sp.Sprite2(assetsDir + 'icon_map9.png', 150, 250, 60, 60, 0, 0))
    maps.append( sp.Sprite2(assetsDir + 'icon_map10.png', 300, 250, 60, 60, 0, 0))
    maps.append( sp.Sprite2(assetsDir + 'icon_map11.png', 450, 250, 60, 60, 0, 0))
    maps.append( sp.Sprite2(assetsDir + 'icon_map12.png', 600, 250, 60, 60, 0, 0))
    maps.append( sp.Sprite2(assetsDir + 'icon_map13.png', 150, 350, 60, 60, 0, 0))
    maps.append( sp.Sprite2(assetsDir + 'icon_map14.png', 300, 350, 60, 60, 0, 0))
    maps.append( sp.Sprite2(assetsDir + 'Button_exit.png', 150, 500, 60, 60, 0, 0))
    
    while not mapExit:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                
                pygame.quit()
                quit()
                            
            if event.type == pygame.KEYDOWN:                    
                if event.key == pygame.K_SPACE:
                    print('S')
                        
        gameDisplay.fill( white )  
        draw_sprite2(mapsback)
        for m in maps:
            draw_sprite2(m)
            
            if (m.rect.collidepoint(pygame.mouse.get_pos()) == 1):
                
                s = pygame.Surface((m.rect.w, m.rect.h))
                s.set_alpha(50)
                s.fill((255,255,255))
                gameDisplay.blit(s, (m.rect.x, m.rect.y))
                
                if re.search("exit", m.file, flags=0):
                    draw_selected( (m.rect.x + m.rect.w + 10, m.rect.y + m.rect.h*0.5 - 15), (display_width,20), 100, white,gameDisplay )
                    message_display( "Return Main Menu /Zuruck/Atras" ,"monospace", 20, (m.rect.x + m.rect.w + 10, m.rect.y + m.rect.h*0.5 - 15), red) 
                else:
                    message_display('Select a Map/Auswählen/Selecciona/' ,"monospace", 30, (100, 0 ), orange)
                    s = pygame.Surface((display_width,20))  
                    s.set_alpha(100)
                    s.fill(white)    
                    gameDisplay.blit(s, (0,570))                    
                    message_display( m.file ,"monospace", 20, (150, 570), red)     
                if pygame.mouse.get_pressed()[0]:
                    
                    if re.search("exit", m.file, flags=0):
                        mapExit = True
                        engineExit = True
                        menuExit = False
                        
                    else:
                        map_name = m.file.split("_",1)[1]
                        map_name = map_name.split(".",1)[0]
                        map_settings = []
                        map_settings.append(m.file)                    
                        map_settings.append(display_height * 0.08)
                        map_settings.append(assetsDir + "" + map_name + ".jpg")
                        
                                        
                        
                        message_display( m.file ,"monospace", 20, (150, 570), blue)   
                        message_display( "Loading/Laden/Cargando " + map_settings[2] ,"monospace", 20, (100,420 ), violet)                   
                        pygame.display.update()
                        mapExit = True
                        engineExit = False
                        menuExit = False                        
                        if(maps.index(m)==0):total = 10
                        if(maps.index(m)==1):total = 12
                        if(maps.index(m)==2):total = 14
                        if(maps.index(m)==3):total = 16
                        if(maps.index(m)==4):total = 17
                        if(maps.index(m)==5):total = 18
                        if(maps.index(m)==6):total = 19
                        if(maps.index(m)==7):total = 20
                        if(maps.index(m)==8):total = 23
                        if(maps.index(m)==9):total = 26
                        if(maps.index(m)==10):total = 29
                        if(maps.index(m)==11):total = 31
                        if(maps.index(m)==12):total = 35
                        if(maps.index(m)==13):total = 45
                        time.sleep(0.5) 
                    
                
        
        
        pygame.display.update()
        
        clock.tick(20)
    

#------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
def game_menu():
    
    global menuExit
    global infoExit
    global engineExit
    global mapExit
    global adjExit
    
    pygame.mixer.music.load(assetsDir + 'Little Swans Game.ogg')
    play_music()
    
    mapsback = sp.Sprite2(assetsDir + 'main_back.jpg', 0, 0, display_width, display_height, 0, 0)
    btn = []
    btn.append( sp.Sprite2(assetsDir + 'play_red.png', 150, 450, 70, 70, 0, 0))
    btn.append( sp.Sprite2(assetsDir + 'Buttonmenu.png', 300, 450, 70, 70, 0, 0))
    btn.append( sp.Sprite2(assetsDir + 'Button_adj.png', 450, 450, 70, 70, 0, 0))
    btn.append( sp.Sprite2(assetsDir + 'Button_cancel.png', 600, 450, 70, 70, 0, 0))
    
    while not menuExit:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:                
                
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:                    
                if event.key == pygame.K_RETURN:
                    menuExit = True
                    
        gameDisplay.fill( white )  
        draw_sprite2(mapsback)
                       
        for m in btn:
            draw_sprite2(m)
            
            if (m.rect.collidepoint(pygame.mouse.get_pos()) == 1):
                draw_selected( (0, 550), (display_width,40), 100, white,gameDisplay )
                
                if re.search("play", m.file, flags=0):
                    message_display( "Play/Spielen/Jugar" ,"monospace", 40, (150, 550), (255,69,0)) 
                if re.search("menu", m.file, flags=0):
                    message_display( "Info/Auskunft/Info" ,"monospace", 40, (150, 550), (47,79,79)) 
                if re.search("cancel", m.file, flags=0):
                    message_display( "Exit/Ausgang/Salir" ,"monospace", 40, (150, 550), (138,43,226)) 
                if re.search("adj", m.file, flags=0):
                    message_display( "Options/Wahl/Opciones" ,"monospace", 40, (150, 550), (255,0,0)) 
                                                
                if pygame.mouse.get_pressed()[0]:
                                                           
                    
                    if re.search("play", m.file, flags=0):
                        menuExit = True
                        mapExit = False
                        time.sleep(0.1) 

                    if re.search("menu", m.file, flags=0):
                        infoExit = False
                        info_loop()
                        
                    
                    if re.search("cancel", m.file, flags=0):
                        
                        pygame.quit()
                        quit()
                
                    if re.search("adj", m.file, flags=0):
                        adjExit = False
                        adjustments()
                        
                        
        pygame.display.update()        
        clock.tick(20)

# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
def adjustments():
    global menuExit 
    global adjExit
    global music_enabled
    global sound_enabled
    
    mapsback = sp.Sprite2(assetsDir + 'maps_board.jpg', 0, 0, display_width, display_height, 0, 0)
    btn = []
 
    if music_enabled:     
        btn.append( sp.Sprite2(assetsDir + 'enabled.png', 250, 100, 50, 50, 0, 0))
    else:
        btn.append( sp.Sprite2(assetsDir + 'disabled.png', 250, 100, 50, 50, 0, 0))
    
    if sound_enabled:
        btn.append( sp.Sprite2(assetsDir + 'enabled.png', 250, 200, 50, 50, 0, 0))
    else:
        btn.append( sp.Sprite2(assetsDir + 'disabled.png', 250, 200, 50, 50, 0, 0))
        
    btn.append( sp.Sprite2(assetsDir + 'buy_yes.png', 50, 480, 60, 60, 0, 0))
    
    while not adjExit:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:                
                
                pygame.quit()
                quit()
                        
        gameDisplay.fill( white )  
        draw_sprite2(mapsback)
                       
        for m in btn:
            draw_sprite2(m)
            
            if (m.rect.collidepoint(pygame.mouse.get_pos()) == 1):
                
                s = pygame.Surface((m.rect.w, m.rect.h))
                s.set_alpha(50)
                s.fill((255,255,255))
                gameDisplay.blit(s, (m.rect.x, m.rect.y))
                if re.search("yes", m.file, flags=0):
                    draw_selected( (0, 550), (display_width,20), 100, white,gameDisplay )
                    message_display( "Return/Zuruck/Atras" ,"monospace", 20, (50, 550), green) 
                    
                    if pygame.mouse.get_pressed()[0]:                                              
                        adjExit = True
                        menuExit = False
                                            
        
        if btn[0].rect.collidepoint(pygame.mouse.get_pos()) == 1:
            draw_selected( (0, 550), (display_width,20), 100, white,gameDisplay )
            if music_enabled :                 
                message_display( "Music Enabled/Aktiviert/Activado" ,"monospace", 20, (100, 550), green) 
            else: message_display( "Music Disabled/Deaktiviert/Desactivado" ,"monospace", 20, (100, 550), red)
            
            if pygame.mouse.get_pressed()[0]:
                if music_enabled: 
                    music_enabled = False
                    btn.append( sp.Sprite2(assetsDir + 'disabled.png', 250, 100, 50, 50, 0, 0))                                       
                else: 
                    music_enabled = True
                    btn.append( sp.Sprite2(assetsDir + 'enabled.png', 250, 100, 50, 50, 0, 0))
                time.sleep(1)
                play_music()
                
        if btn[1].rect.collidepoint(pygame.mouse.get_pos()) == 1:
            draw_selected( (0, 550), (display_width,20), 100, white,gameDisplay )
            if sound_enabled :  message_display( "Sound Enabled/Aktiviert/Desactivado" ,"monospace", 20, (100, 550), green) 
            else: message_display( "Sound Disabled/Deactiviert/Desactivado" ,"monospace", 20, (100, 550), red)
            
            if pygame.mouse.get_pressed()[0]:
                if sound_enabled: 
                    sound_enabled = False
                    btn.append( sp.Sprite2(assetsDir + 'disabled.png', 250, 200, 50, 50, 0, 0))
                    
                else: 
                    sound_enabled = True
                    btn.append( sp.Sprite2(assetsDir + 'enabled.png', 250, 200, 50, 50, 0, 0))
                time.sleep(1)
                play_music()
                    
                        
                                   
        message_display( "Options/Auswählen/Opciones" ,"monospace", 40, (50, 0), orange)
        message_display( "Music/Musik/Musica" ,"monospace", 30, (50, 100), white)
        message_display( "Sounds/Klänge/Sonidos" ,"monospace", 30, (50, 200), white)
        
        
        pygame.display.update()
        clock.tick(20)
    
def info_loop():
    global infoExit 
    
    
    pygame.mixer.music.load(assetsDir + 'Little Swans Game.ogg')
    
    play_music()
    
    mapsback = sp.Sprite2(assetsDir + 'maps_board.jpg', 0, 0, display_width, display_height, 0, 0)
    btn = []
    btn.append( sp.Sprite2(assetsDir + 'buy_yes.png', 100, 450, 90, 90, 0, 0))
        
    while not infoExit:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:                
                sound_bullet.play
                pygame.quit()
                quit()
                        
        gameDisplay.fill( white )  
        draw_sprite2(mapsback)
                       
        for m in btn:
            draw_sprite2(m)
            
            if (m.rect.collidepoint(pygame.mouse.get_pos()) == 1):
                
                s = pygame.Surface((m.rect.w, m.rect.h))
                s.set_alpha(50)
                s.fill((255,255,255))
                            
                if re.search("yes", m.file, flags=0):
                    draw_selected( (0, 550), (display_width,20), 100, white,gameDisplay )
                    message_display( "Done/Geschafft/Hecho" ,"monospace", 20, (100, 550), (255,69,0)) 
                
                
                gameDisplay.blit(s, (m.rect.x, m.rect.y))  
                
                if pygame.mouse.get_pressed()[0]:                                                           
                    if re.search("yes", m.file, flags=0):
                        infoExit = True
                        time.sleep(1) 
        yt = 10
        text = 'Zombie Pan beta 1.1.4 '
        message_display( text ,"monospace", 30, (50, yt), gray)
        yt+=40
        text = 'Independent Video Game created and designed by nordik14@gmail.com'        
        message_display( text ,"monospace", 20, (50, yt), gray)                                 
        yt+=20
        text = "Free distirbution of this product under GPL is allowed"
        message_display( text ,"monospace", 20, (50, yt), gray)                                     
        text = 'Free Assets obtained from GameArt2D:'
        yt+=20
        message_display( text ,"monospace", 20, (50, yt), blue)
        text = 'Free distibution'
        yt+=20
        message_display( text ,"monospace", 20, (50, yt), blue)
        text = 'Licenced distribution '
        yt+=20
        message_display( text ,"monospace", 20, (50, yt), blue)        
        yt+=20
        text = 'Original design'
        message_display( text ,"monospace", 20, (50, yt), blue)                                            
        yt+=20                
        text = 'Zombie Pan available in Google Playstore!'
        message_display( text ,"monospace", 20, (50, yt), green)
        yt+=20
        text = 'Other products: Brick Infest, Vozarron, Ñulingua aprende español '
        message_display( text ,"monospace", 15, (50, yt), green)        
        yt+=20
        #draw_selected( (0, 380), (display_width,80), yt, black, gameDisplay )
        text = 'Support this video game for future updates'
        message_display( text ,"monospace", 25, (50, yt), red)
        yt+=50
        text = 'unterstütze dieses Videospiel für zukünftige Updates'
        message_display( text ,"monospace", 25, (50, yt), red)
        yt+=50
        text = 'Apoya este Juego con Donaciones '
        message_display( text ,"monospace", 25, (50, yt), red)
        yt+=50        
        draw_selected( (0, yt), (display_width,20), 100, gold, gameDisplay )
        text = 'Feedback, donations: nordik14@gmail.com'
        message_display( text ,"monospace", 20, (50, yt), black)
        
        pygame.display.update()        
        clock.tick(20)
        
# -----------------------------------------------------------------------    
    

while not gameExit:
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:                
            sound_bullet.play
            pygame.quit()
            quit()
    game_menu ()
    game_maps()
    engine_loop()

