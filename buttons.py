import sprites as sp
import defaults as df
import var as var
import pygame
import time
import text as txg

class Button(sp.Sprite2):

    def __init__(self, filename, x, y, w, h):
       
        sp.Sprite2.__init__(self, filename, x, y, w, h, 0, 0)
        self.hover_text = 'Back / Zurück/ Atras'
        self.click_text = 'Loading/ Laden/ Caragando'
        # self.font =  "monospace"
        # self.font_size = 30
        self.txt_w = df.display_width
        self.txt_h = 30
        self.txt_x = df.display_width*0.1
        self.txt_y = df.display_height - self.txt_h*2
        self.txt_color= df.gray
        self.hover_color = df.white
        self.click_color = df.red
        self.shadow_w = df.display_width
        self.shadow_h = 50
        self.shadow_x = 0
        self.shadow_y = self.txt_y
        self.shadow_color = df.white
        self.index = 0
        self.highlighted = False
        self.clicked = False
        self.max_frame = 10
        self.animating = False
        self.txt_x_d = self.txt_x
        self.txt_y_d = self.txt_y

        self.shadow_x_d = self.shadow_x
        self.shadow_y_d = self.shadow_y
        self.shadow_color = df.white

        self.font_btn = txg.TextGame()
        self.font_btn.font_size = 50
        self.font_btn.set_font()
        self.font_btn.center = (self.txt_x, self.txt_y)
        self.font_btn.color = df.white

        # self.font = pygame.font.Font("assets/fonts/horrendo.ttf", self.font_size)

    def draw_sprite2(self):
        var.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))

    def highlight(self, color):
        s = pygame.Surface((self.rect.w, self.rect.h))
        s.set_alpha(50)
        s.fill(color)
        pygame.draw.rect(var.gameDisplay, color, [self.rect.x, self.rect.y, self.rect.w, 1])
        pygame.draw.rect(var.gameDisplay, color, [self.rect.x, self.rect.y, 1, self.rect.h])
        pygame.draw.rect(var.gameDisplay, color, [self.rect.x, self.rect.y + self.rect.h, self.rect.w, 1])
        pygame.draw.rect(var.gameDisplay, color, [self.rect.x+self.rect.w, self.rect.y, 1, self.rect.h])
        var.gameDisplay.blit(s, (self.rect.x, self.rect.y))


    def new_shadow(self, color):
        s = pygame.Surface((self.txt_w, self.shadow_h))
        s.set_alpha(50)
        s.fill(color)
        var.gameDisplay.blit(s, (self.shadow_x, self.shadow_y))

    def new_msg(self, text):
        self.new_shadow(self.shadow_color)
        self.font_btn.display_text(text)
        # myfont = pygame.font.SysFont(self.font, self.font_size)
        # label = self.font.render(text, 1, color2)
        # var.gameDisplay.blit(label, (self.txt_x, self.txt_y))


    def onClick(self, mouse):

        if self.rect.collidepoint(mouse.get_pos()) == 1:
            self.highlight(self.hover_color)

            self.new_msg(self.hover_text)
            # self.highlighted = True

            if mouse.get_pressed()[0]:
                self.animating = True
                self.clicked = True
                print('button clicked', self.file)
                self.index = 0
                time.sleep(0.5)
        else:
            self.highlight_color = self.hover_color

        if self.animating:self.animate()

        self.draw_sprite2()
        if self.animating  or not self.clicked:


            return False #continue running
        else:
            self.clicked = False
            return True #clicken event is true

    def animate(self):
        self.index +=1
        if self.index < self.max_frame:
            self.highlight(self.click_color)
            # self.new_msg('Nuevo', self.click_color, self.click_color)
            # self.new_msg(self.hover_text, self.click_color, self.click_color)
            self.txt_x += 100
            #self.txt_y += 1
            self.shadow_x += 100
            #self.shadow_y += 1
            self.animating = True
        else:
            self.animating = False
            self.txt_x = self.txt_x_d
            self.txt_y  = self.txt_y_d
            self.shadow_x = self.shadow_x_d
            self.shadow_y = self.shadow_y_d


class Imap(Button):
    def __init__(self,filename, x, y, level, gap, blocked, total_enemies):
        w = 100
        h = 100
        Button.__init__(self, filename, x, y, w, h)

        self.level = level
        self.blocked = blocked
        self.total = total_enemies
        self.gap = gap
        self.map_name = ""
        self.filename  = ""
        self.bfilename = var.assetsDir + "icons8-lock-100.png"
        self.lockpad = sp.Sprite2(self.bfilename, x, y, int(w*0.5), int(h*0.5), 0, 0)
        self.hover_text = 'Level ' + str(level) + '   /   ' + str(total_enemies) + ' Zombies'
        self.font_btn.color = df.red



    def set_map(self):
        if self.level ==1 :
            self.map_name = 'classic_city.jpg'
            self.gap = df.display_height * 0.1437
        if self.level ==2 :
            self.map_name = 'china.jpg'
            self.gap = df.display_height * 0.181
        if self.level ==3 :
            self.map_name = 'parallax background for nature tileset.jpg'
            self.gap = df.display_height * 0.195
        if self.level ==4 :
            self.map_name = 'forest.jpg'
            self.gap = df.display_height * 0.0762
        if self.level ==5 :
            self.map_name = 'classic1.jpg'
            self.gap = df.display_height * 0.2063
        if self.level ==6 :
            self.map_name = 'classic2.jpg'
            self.gap = df.display_height * 0.185
        if self.level ==7 :
            self.map_name = 'night_lanterns.jpg'
            self.gap = df.display_height * 0.183
        if self.level ==8 :
            self.map_name = 'night_lanterns.jpg'
            self.gap = df.display_height * 0.18
        if self.level ==9 :
            self.map_name = 'snow1.jpg'
            self.gap = df.display_height * 0.17
        if self.level ==10 :
            self.map_name = 'snow2.jpg'
            self.gap = df.display_height * 0.176
        if self.level ==11 :
            self.map_name = 'horror2.jpg'
            self.gap = df.display_height * 0.195
        if self.level ==12 :
            self.map_name = 'horror1.jpg'
            self.gap = df.display_height * 0.1775
        if self.level ==13 :
            self.map_name = 'volcanoes.jpg'
            self.gap = df.display_height * 0.171
        if self.level ==14 :
            self.map_name = 'volcanoes.jpg'
            self.gap = df.display_height * 0.171


        # self.map_name = self.file.split("_", 1)[1]
        # self.map_name = self.map_name.split(".", 1)[0]
        self.filename = var.assetsDir + "backgrounds/" + self.map_name


    #
    # def highlight_icon(self):
    #     s = pygame.Surface((self.rect.w, self.rect.h))
    #     s.set_alpha(40)
    #     s.fill((255, 255, 255))
    #     var.gameDisplay.blit(s, (self.rect.x, self.rect.y))
    #
    def draw_block(self):
        # var.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))
        if self.blocked:
            var.gameDisplay.blit(self.lockpad.image, (self.rect.x, self.rect.y))
