import pygame
assetsDir = 'assets/'
music_enabled = True
display_width = 800
display_height = 600
map_gap = display_height * 0.08
gameDisplay = pygame.display.set_mode( (  display_width, display_height ) )

black = ( 0, 0, 0 )
white = ( 255, 255, 255 )
red = ( 255 , 0, 0 )
blue = ( 0,191,255 )
orange = (255,69,0)
gold = (255,215,0)
green = (124,252,0)
violet = (138,43,226)
gray = (112,128,144)



def play_music():
    
    if music_enabled:
        pygame.mixer.stop()
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
    else:
        pygame.mixer.music.pause()

     
def draw_sprite2( sprite ):
     gameDisplay.blit( sprite.image, (sprite.rect.x, sprite.rect.y ))


def draw_selected(pos, dim, alpha, color, gameDisplay ):
    s = pygame.Surface(dim)  
    s.set_alpha(alpha)
    s.fill(color)                            
    gameDisplay.blit(s, pos)    
    
   
def message_display(text, typefont, size, center,color):
    myfont = pygame.font.SysFont(typefont, size )
    label = myfont.render(text, 1, color)    
    gameDisplay.blit(label,center)

        
