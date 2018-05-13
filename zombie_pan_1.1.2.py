import pygame
import time
import random
import re


pygame.init()

pygame.mixer.music.load('assets/Little Swans Game.ogg')
pygame.display.set_icon( pygame.image.load('assets/icon_zombie.png')) 
pygame.mixer.pre_init(frequency=44100, size=-32, channels=2, buffer=4096)
sound_bullet = pygame.mixer.Sound(file = 'assets/single_water_drop.ogg')
sound_bullet.set_volume(0.5)
sound_col = pygame.mixer.Sound(file = 'assets/comical_liquid_gel_splat.ogg')
sound_col.set_volume(0.5)
sound_err = pygame.mixer.Sound(file = 'assets/327736__distillerystudio__error-03.ogg')
sound_err.set_volume(0.5)
sound_hel = pygame.mixer.Sound(file = 'assets/helicopter.ogg')
sound_hel.set_volume(0.2)
sound_loser = pygame.mixer.Sound(file = 'assets/113988__kastenfrosch__verloren.ogg')
sound_hel.set_volume(0.5)
sound_winer = pygame.mixer.Sound(file = 'assets/270528littlerobotsoundfactoryjingle-win-00.ogg')
sound_winer.set_volume(0.5)

display_width = 800
display_height = 600

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
map_settings = [ "", 0, "assets/map1.jpg", 0]

clock = pygame.time.Clock()
#start engines 
engineExit = False
gameExit = False
menuExit = False
infoExit = False
mapExit = False
adjExit = False

music_enabled = True
sound_enabled = True

total = 15 #default total number of zombies to appear

class Sprite:
    
    def __init__(self, img, x, y, velx, vely, scalef ):
        self.x = x
        self.y = y
        self.u = velx
        self.v = vely
        self.surface = pygame.image.load (img)
        self.w = self.surface.get_rect().size[0]
        self.h = self.surface.get_rect().size[1] 
        self.scale = scalef
        w = int (float(self.w * scalef))
        h = int(float(self.h * scalef))
        self.surface = pygame.transform.scale(self.surface, (w,h ))
        self.w = self.surface.get_rect().size[0]
        self.h = self.surface.get_rect().size[1] 
        

class Sprite2(pygame.sprite.Sprite):
        
    def __init__(self, image_file, x, y, w, h, u, v):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)      
        self.image = pygame.transform.scale(self.image, (w, h))            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.u = u
        self.v = v
        self.file = image_file

class Sprite3(pygame.sprite.Sprite):

    def __init__(self, files, x, y, u, v):
        super(Sprite3, self).__init__()
			        
		#loads lived , dead images
        self.imagesRun = self.load_images([files[0],files[1]])
        self.imagesDead = self.load_images([files[2],files[3]])
        self.files = files                        
        self.index = 0
        self.image = self.imagesRun[self.index]
        self.rect = pygame.Rect(x, y, 10, 10)
        self.u = u
        self.v = v
        self.lived = True#declares status
        self.uDefault = u
        #files[0] images list names
        #files [1] images size tupla

	#load images surfaces from filesDead
    def load_images(self, files):
        imageList = []
        for item in files[0]:
            images = pygame.image.load(item)
            imageList.append( pygame.transform.scale( images, files[1]))
        return (imageList)

    #animation def changes frames 
    def update(self):
        self.index += 1
        if  self.lived:#lived animation - Run
            if self.index >= len(self.imagesRun):
                self.index = 0
            self.image = self.imagesRun[self.index]
            self.rect.w = self.files[1][0]
            self.rect.h = self.files[1][1]
            
        else:#dead animation
            self.u = 0            
            if self.index >= len(self.imagesDead):
                self.lived = True
                self.u = self.uDefault
                self.rect.x = 0
            else:
                self.image = self.imagesDead[self.index]            
                self.rect.w = self.files[3][0]
                self.rect.h = self.files[3][1]



    
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
    
    
def pause_loop():
    global engineExit
    global menuExit
    pauseExit = False
        
    mapsback = Sprite2('assets/maps_board.jpg', 0, 0, display_width, display_height, 0, 0)
    btns = []    
    btns.append( Sprite2("assets/Button_play.png", display_width * 0.5 - 100, display_height * 0.5 - 100, 80, 80, 0, 0))
    btns.append( Sprite2("assets/Buttonmenu.png", btns[0].rect.x, btns[0].rect.y + btns[0].rect.h + 10, 80, 80, 0, 0))
    btns.append( Sprite2("assets/Button_cancel.png",  btns[1].rect.x, btns[1].rect.y + btns[1].rect.h + 10, 80, 80, 0, 0))
    
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
#---------------------------------------------------------------------------------------    
#---------------------------------------------------------------------------------------
def end():
    global engineExit
    endExit = False
    pygame.mixer.music.load('assets/Little Swans Game.ogg')
    play_music()
    background =  Sprite2( 'assets/end.jpg', 0, 0, display_width, display_height, 0, 0)

    filesRun = ['assets/Run1.png', 'assets/Run2.png', 'assets/Run3.png', 'assets/Run4.png', 'assets/Run5.png', 'assets/Run6.png']
    filesRunSize =  (70,77)
    filesDead = ['assets/Dead1.png', 'assets/Dead2.png', 'assets/Dead3.png', 'assets/Dead4.png', 'assets/Dead5.png', 'assets/Dead6.png', 'assets/Dead7.png','assets/Dead8.png']
    files = [filesRun,filesRunSize,filesDead,filesDeadSize]

    group_enemies=[]
    group_enemies.append( Sprite3(files, 0, display_height - 20 - 77 - 20, 2.0, 0))
    group_enemies.append( Sprite3(files, 0, display_height - 20 - 77 + 0,  2.0, 0))
    group_enemies.append( Sprite3(files, 0, display_height - 20 - 77 + 20, 2.0, 0))
    group_enemies.append( Sprite3(files, 0, display_height - 20 - 77 - 20, 2.0, 0))
    group_enemies.append( Sprite3(files, 0, display_height - 20 - 77 + 0,  2.0, 0))
    group_enemies.append( Sprite3(files, 0, display_height - 20 - 77 + 20, 2.0, 0))
    group_enemies.append( Sprite3(files, 0, display_height - 20 - 77 - 20, 2.0, 0))
    group_enemies.append( Sprite3(files, 0, display_height - 20 - 77 + 0,  2.0, 0))
    group_enemies.append( Sprite3(files, 0, display_height - 20 - 77 + 20, 2.0, 0))
    
    
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
        draw_sprite2( background )        
        
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
                draw_sprite2(enemy)
                enemy.update()
                enemy.rect.x += enemy.u 
                enemy.rect.y += enemy.v
             
        
        draw_selected((0, 20), (display_width,40), 100, white, gameDisplay )
        message_display('Thanks', "monospace", 40, (350, 20), blue)    
        
        pygame.display.update()    
        clock.tick( 60 )
        
    
    
#---------------------------------------------------------------------------------------    
#---------------------------------------------------------------------------------------



def engine_loop():
    
    global engineExit 
    global menuExit
    global mapExit
    
    pygame.mixer.music.load('assets/helicopter.ogg')
    play_music()
    #print('engine started')
    
    background =  Sprite2( map_settings[2], 0, 0, display_width, display_height, 0, 0)
    map_gap = map_settings[1]

    info_winer = Sprite2('assets/enabled.png', display_width*0.5 - 40, display_height*0.5 - 40, 80, 80, 0, 0)
    info_loser = Sprite2('assets/disabled.png', display_width*0.5 - 40, display_height*0.5 - 40, 80, 80, 0, 0)
    
    filesRun = ['assets/Run1.png', 'assets/Run2.png', 'assets/Run3.png', 'assets/Run4.png', 'assets/Run5.png', 'assets/Run6.png']
    filesRunSize =  (70,77)
    filesDead = ['assets/Dead1.png', 'assets/Dead2.png', 'assets/Dead3.png', 'assets/Dead4.png', 'assets/Dead5.png', 'assets/Dead6.png', 'assets/Dead7.png','assets/Dead8.png']
    filesDeadSize = (96,77)
    files = [filesRun,filesRunSize,filesDead,filesDeadSize]

    group_enemies=[]
    group_enemies.append( Sprite3(files, 0, display_height - map_gap - 77 - 10, 2.0, 0))
    group_enemies.append( Sprite3(files, 0, display_height - map_gap - 77 + 0,  2.0, 0))
    group_enemies.append( Sprite3(files, 0, display_height - map_gap - 77 + 10, 2.0, 0))
    
    filesHel = ['assets/helicopter1.png', 'assets/helicopter2.png', 'assets/helicopter3.png', 'assets/helicopter4.png']    
    filesHelSize = (210,62)
    files = [filesHel, filesHelSize, filesHel, filesHelSize] #meandwhile no destructed helicpter is available
    hel = Sprite3(files, 0, 20, 2, 0)

    bullet1 = Sprite2('assets/bullet1.png', hel.rect.x, 0, 12, 18, 0, 0 )
    
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
            if enemy.rect.x == 0 :
                respawn += 1    # counter
                enemy.rect.x += 2 # pushes at the begining
                mood = 1.5 + random.random() # random velocity       
                enemy.u = enemy.u * mood 
                if enemy.u > 5: # limit velocity         
                    enemy.u = 2.0
                if enemy.u < 1:          
                    enemy.u = 2.0                
            #outside of window
            if enemy.rect.x > display_width:
                enemy.rect.x = 0
                if sound_enabled: sound_err.play()                        
                killed += 1
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
                    enemy.index = 0 #restarts frame
                
                 
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
        
        
        draw_selected((0, 0), (display_width,20), 100, white,gameDisplay )
        message_display('Enemies:' + str(total - respawn), "monospace", 20, (0, 0), orange)    
        message_display('Exp:' + str(experience), "monospace", 20, (200, 0), violet)
        message_display('Shelter:' + str(int(shelter)) + "%" ,"monospace", 20, (400, 0), red)

        #control
        if killed >= total or shelter < 0:
            
            engineExit = True
            menuExit = True
            mapExit = False
            
            draw_selected( (0, display_height*0.5+50), (display_width,30), 100, white,gameDisplay )
            message_display('Shelter:' + str(int(shelter)) + "%" ,"monospace", 30, (display_width*0.5-100, display_height*0.5+50), violet)
            if shelter > 0 :                
                draw_sprite2(info_winer)
                if sound_enabled: sound_winer.play()
                
                  
                if re.search("map14", map_settings[2], flags=0):
                    time.sleep(1)                
                    end()
            else:
                draw_sprite2(info_loser)
                if sound_enabled: sound_loser.play()
            pygame.display.update()
            time.sleep(4)
        
        pygame.display.update()    
        clock.tick( 60 )
        
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

def game_maps():
    
    global mapExit 
    global menuExit
    global map_settings
    global engineExit
    global total
    
    #pygame.mixer.music.load('assets/WelcomeScreen.mp3')
    play_music()
    
    print('engine maps')
    
    mapsback = Sprite2('assets/maps_board.jpg', 0, 0, display_width, display_height, 0, 0)
    maps = []
    maps.append( Sprite2('assets/icon_map1.png', 150, 50, 60, 60, 0, 0))
    maps.append( Sprite2('assets/icon_map2.png', 300, 50, 60, 60, 0, 0))
    maps.append( Sprite2('assets/icon_map3.png', 450, 50, 60, 60, 0, 0))
    maps.append( Sprite2('assets/icon_map4.png', 600, 50, 60, 60, 0, 0))
    maps.append( Sprite2('assets/icon_map5.png', 150, 150, 60, 60, 0, 0))
    maps.append( Sprite2('assets/icon_map6.png', 300, 150, 60, 60, 0, 0))
    maps.append( Sprite2('assets/icon_map7.png', 450, 150, 60, 60, 0, 0))
    maps.append( Sprite2('assets/icon_map8.png', 600, 150, 60, 60, 0, 0))
    maps.append( Sprite2('assets/icon_map9.png', 150, 250, 60, 60, 0, 0))
    maps.append( Sprite2('assets/icon_map10.png', 300, 250, 60, 60, 0, 0))
    maps.append( Sprite2('assets/icon_map11.png', 450, 250, 60, 60, 0, 0))
    maps.append( Sprite2('assets/icon_map12.png', 600, 250, 60, 60, 0, 0))
    maps.append( Sprite2('assets/icon_map13.png', 150, 350, 60, 60, 0, 0))
    maps.append( Sprite2('assets/icon_map14.png', 300, 350, 60, 60, 0, 0))
    maps.append( Sprite2('assets/Button_exit.png', 150, 500, 60, 60, 0, 0))
    
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
                    message_display( "Return Main Menu" ,"monospace", 20, (m.rect.x + m.rect.w + 10, m.rect.y + m.rect.h*0.5 - 15), red) 
                else:
                    message_display('Select a Map' ,"monospace", 30, (100, 0 ), orange)
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
                        map_settings.append("assets/" + map_name + ".jpg")
                        
                                        
                        
                        message_display( m.file ,"monospace", 20, (150, 570), blue)   
                        message_display( "loading " + map_settings[2] ,"monospace", 20, (100,420 ), violet)                   
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
                        if(maps.index(m)==13):total = 40
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
    
    pygame.mixer.music.load('assets/Little Swans Game.ogg')
    play_music()
    
    mapsback = Sprite2('assets/main_back.jpg', 0, 0, display_width, display_height, 0, 0)
    btn = []
    btn.append( Sprite2('assets/play_red.png', 150, 450, 70, 70, 0, 0))
    btn.append( Sprite2('assets/Buttonmenu.png', 300, 450, 70, 70, 0, 0))
    btn.append( Sprite2('assets/Button_adj.png', 450, 450, 70, 70, 0, 0))
    btn.append( Sprite2('assets/Button_cancel.png', 600, 450, 70, 70, 0, 0))
    
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
                    message_display( "Play" ,"monospace", 40, (150, 550), (255,69,0)) 
                if re.search("menu", m.file, flags=0):
                    message_display( "Info" ,"monospace", 40, (150, 550), (47,79,79)) 
                if re.search("cancel", m.file, flags=0):
                    message_display( "Exit" ,"monospace", 40, (150, 550), (138,43,226)) 
                if re.search("adj", m.file, flags=0):
                    message_display( "Options" ,"monospace", 40, (150, 550), (255,0,0)) 
                                                
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
    
    mapsback = Sprite2('assets/maps_board.jpg', 0, 0, display_width, display_height, 0, 0)
    btn = []
 
    if music_enabled:     
        btn.append( Sprite2('assets/enabled.png', 250, 100, 50, 50, 0, 0))
    else:
        btn.append( Sprite2('assets/disabled.png', 250, 100, 50, 50, 0, 0))
    
    if sound_enabled:
        btn.append( Sprite2('assets/enabled.png', 250, 200, 50, 50, 0, 0))
    else:
        btn.append( Sprite2('assets/disabled.png', 250, 200, 50, 50, 0, 0))
        
    btn.append( Sprite2('assets/buy_yes.png', 50, 480, 60, 60, 0, 0))
    
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
                    message_display( "Return to Main Menu" ,"monospace", 20, (50, 550), green) 
                    
                    if pygame.mouse.get_pressed()[0]:                                              
                        adjExit = True
                        menuExit = False
                                            
        
        if btn[0].rect.collidepoint(pygame.mouse.get_pos()) == 1:
            draw_selected( (0, 550), (display_width,20), 100, white,gameDisplay )
            if music_enabled :                 
                message_display( "Music Enabled" ,"monospace", 20, (100, 550), green) 
            else: message_display( "Music Disabled" ,"monospace", 20, (100, 550), red)
            
            if pygame.mouse.get_pressed()[0]:
                if music_enabled: 
                    music_enabled = False
                    btn.append( Sprite2('assets/disabled.png', 250, 100, 50, 50, 0, 0))                                       
                else: 
                    music_enabled = True
                    btn.append( Sprite2('assets/enabled.png', 250, 100, 50, 50, 0, 0))
                time.sleep(1)
                play_music()
                
        if btn[1].rect.collidepoint(pygame.mouse.get_pos()) == 1:
            draw_selected( (0, 550), (display_width,20), 100, white,gameDisplay )
            if sound_enabled :  message_display( "Sound Enabled" ,"monospace", 20, (100, 550), green) 
            else: message_display( "Sound Disabled" ,"monospace", 20, (100, 550), red)
            
            if pygame.mouse.get_pressed()[0]:
                if sound_enabled: 
                    sound_enabled = False
                    btn.append( Sprite2('assets/disabled.png', 250, 200, 50, 50, 0, 0))
                    
                else: 
                    sound_enabled = True
                    btn.append( Sprite2('assets/enabled.png', 250, 200, 50, 50, 0, 0))
                time.sleep(1)
                play_music()
                    
                        
                                   
        message_display( "Options" ,"monospace", 40, (50, 0), orange)
        message_display( "Music" ,"monospace", 30, (50, 100), white)
        message_display( "Sounds" ,"monospace", 30, (50, 200), white)
        
        
        pygame.display.update()
        clock.tick(20)
    
def info_loop():
    global infoExit 
    
    
    pygame.mixer.music.load('assets/Little Swans Game.ogg')
    
    play_music()
    
    mapsback = Sprite2('assets/maps_board.jpg', 0, 0, display_width, display_height, 0, 0)
    btn = []
    btn.append( Sprite2('assets/buy_yes.png', 100, 450, 90, 90, 0, 0))
        
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
                    message_display( "Done" ,"monospace", 20, (100, 550), (255,69,0)) 
                
                
                gameDisplay.blit(s, (m.rect.x, m.rect.y))  
                
                if pygame.mouse.get_pressed()[0]:                                                           
                    if re.search("yes", m.file, flags=0):
                        infoExit = True
                        time.sleep(1) 
        
        text = 'Zombie Pan beta 1.1 '
        message_display( text ,"monospace", 20, (50, 100), gray)
        
        text = 'Independent Video Game created and designed by nordik'        
        message_display( text ,"monospace", 20, (50, 150), gray)                         
        
        text = "Free distirbution of this product under GPL allowed"
        message_display( text ,"monospace", 20, (50, 200), gray)                             
        
        text = 'Assets obtained from:'
        message_display( text ,"monospace", 20, (50, 250), blue)
        text = 'Free distibution'
        message_display( text ,"monospace", 20, (50, 280), blue)
        text = 'Licenced distribution '
        message_display( text ,"monospace", 20, (50, 300), blue)
        text = 'Original design'
        message_display( text ,"monospace", 20, (50, 320), blue)
                                            
                        
        text = 'Zombie Pan available in Google Playstore!'
        message_display( text ,"monospace", 20, (50, 340), green)
        
        text = 'Other products: Brick Infest, Vozarron '
        message_display( text ,"monospace", 15, (50, 360), green)        
        
        draw_selected( (0, 380), (display_width,50), 110, black, gameDisplay )
        text = 'Support this video game for future updates '
        message_display( text ,"monospace", 25, (50, 380), green)
        
        draw_selected( (0, 410), (display_width,20), 100, gold, gameDisplay )
        text = 'Feedback, donations: nordik14@gmail.com'
        message_display( text ,"monospace", 20, (50, 410), black)
        
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

