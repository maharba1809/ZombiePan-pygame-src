import pygame
import os
import defaults as df
import var
import device
import random
import time
class Sprite:
    #first try to defina image  as sprite - obsolete but some obj still need it
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
    #class to define simple image as sprite
    def __init__(self, image_file, x, y, w, h, u, v):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        # print(image_file)
        self.image = pygame.transform.scale(self.image, (w, h))            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.u = u
        self.v = v
        self.file = image_file
        print('created sprite from:',image_file)

class Sprite3(pygame.sprite.Sprite):
#generic class to create a sprite with animation properties, Run&Dead
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
        self.alive = True#declares status
        self.uDefault = u
        self.col = False
        #files[0] images list names
        #files [1] images size tupla

	#load images surfaces from filesDead
    def load_images(self, files):
        imageList = []
        for item in files[0]:
            if not os.path.exists(item):
                print('***No file exists:' + item)
                pygame.quit()
                quit()
            
            images = pygame.image.load(item)
            imageList.append( pygame.transform.scale( images, files[1]))
                
        return (imageList)

    #animation def changes frames 
    def update(self):
        self.index += 1
        if self.alive:#lived animation - Run
            if self.index >= len(self.imagesRun):
                self.index = 0
            self.image = self.imagesRun[self.index]
            self.rect.w = self.files[1][0]
            self.rect.h = self.files[1][1]

        else:#dead animation
            self.u = 0
            if self.index >= len(self.imagesDead):
                self.alive = True
                self.u = self.uDefault
                self.rect.x = 0
            else:
                self.image = self.imagesDead[self.index]            
                self.rect.w = self.files[3][0]
                self.rect.h = self.files[3][1]

    def physics(self):
        if self.rect.x + self.rect.w >= df.display_width:
            if self.u > 0:
                self.rect.x -= self.u
                self.u = -self.u
                if device.audio.sound_enabled:
                    device.audio.sound_hel.play()


        if self.rect.x < 0:
            if self.u < 0:
                self.rect.x -= self.u
                self.u = -self.u
                if device.audio.sound_enabled:
                    device.audio.sound_hel.play()

class AddBullet(Sprite2):
    def __init__(self,x,y):
        self.image_file = var.assetsDir + 'bullet1.png'
        w = 12
        h = 18
        u = 0
        v = 15
        Sprite2.__init__(self,self.image_file,x,y, w, h, u, v)

        # newbullet = self.Sprite2(var.assetsDir + 'bullet1.png', xb, yb, 12, 18, hel.u, 9)

class Weapon():
    def __init__(self,x,y):
        self.magazine = []
        self.limit = 5
        self.x = 0
        self.y = 0
        self.uinert = 0
        self.bullet_available = 0
        # self.shoot_count = 0

    def shoot_bullet(self):
        if  self.bullet_available>0:
            new_bullet = AddBullet(self.x,self.y)
            new_bullet.u = self.uinert
            if len(self.magazine) < self.limit:
                self.magazine.append(new_bullet)
                # self.shoot_count += 1
                self.bullet_available -=1
                if device.audio.sound_enabled:
                    device.audio.sound_bullet.play()
            else:
                print('Weapon overload')
        else:
            print('No Bullets')

    def get_loc(self,hel):
        self.x = hel.rect.x + hel.rect.w * 0.7
        self.y = hel.rect.y + hel.rect.h * 0.9
        self.uinert = hel.u*0.85

    def moveBullets(self):
        # print(len(self.magazine))
        if len(self.magazine)>0:
            # print(self.magazine)

            for bullet in self.magazine:
                # print(bullet.rect.x, bullet.u)
                # bullet.u = self.uinert
                bullet.rect.x += bullet.u
                bullet.rect.y += bullet.v

                if bullet.rect.y > df.display_height:
                    # del bullet1
                    self.magazine.remove(bullet)
                else:
                    var.gameDisplay.blit(bullet.image, (bullet.rect.x, bullet.rect.y))


class Asprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.files_run = []
        self.files_run = [var.assetsDir + 'helicopter1.png']
        self.files_run.append(var.assetsDir + 'helicopter2.png')
        self.files_run.append(var.assetsDir + 'helicopter3.png')
        self.files_run.append(var.assetsDir + 'helicopter4.png')
        self.files_dead = []
        self.fileSizeDead = []
        self.fileSizeRun = (210, 62)

        self.index = 0
        self.image = pygame.image.load(self.files_run[0])
        self.rect = self.image.get_rect()

        self.u = 0
        self.v = 0
        self.alive = True  # declares status
        self.uDefault = 9
        self.col = False
        self.imagesRun = []
        self.imagesDead = []
        self.imagesAttack = []
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20
        self.rect.w = 0
        self.rect.h = 0
        self.sound = device.audio.sound_hel


    def load_images(self):
        for item in self.files_run:
            images = pygame.image.load(item)
            self.imagesRun.append(pygame.transform.scale(images, self.fileSizeRun))

        if self.files_dead:
            for item in self.files_dead:
                images = pygame.image.load(item)
                self.imagesDead.append(pygame.transform.scale(images, self.fileSizeDead))


    def animate(self):
        if self.alive:  # lived animation - Run
            if self.files_run:
                if self.index < len(self.files_run):
                    self.image = self.imagesRun[self.index]
                    self.index += 1
                else:
                    self.index = 0
                if self.rect.w != self.fileSizeRun[0]:self.rect.w = self.fileSizeRun[0]
                if self.rect.h != self.fileSizeRun[1]:self.rect.h = self.fileSizeRun[1]

        else:
            if self.u!=0:
                self.index = 0
                self.u = 0
            # print(self.files_dead,len(self.files_dead),self.index,'index')
            if self.files_dead:
                if self.index < len(self.files_dead):
                    self.image = self.imagesDead[self.index]
                    self.index += 1
                # else:
                #     self.index = 0
                #     self.col = True

                if self.rect.w != self.fileSizeDead[0]: self.rect.w = self.fileSizeDead[0]
                if self.rect.h != self.fileSizeDead[0]: self.rect.h = self.fileSizeDead[1]
        self.move()
        self.draw()

    def move(self):
        # print(self.u)
        if self.rect.x + self.rect.w >= df.display_width:
            if self.u > 0:
                self.rect.x -= self.u
                self.u = -self.u
                if device.audio.sound_enabled: self.sound.play()

        if self.rect.x < 0:
            if self.u < 0:
                self.rect.x -= self.u
                self.u = -self.u
                if device.audio.sound_enabled: self.sound.play()
        self.rect.x += self.u
        self.rect.y += self.v

    def draw(self):
        var.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))

class House (Asprite):
    def __init__(self):
        Asprite.__init__(self)
        asset_path = var.assetsDir + "/house"

        file_name = ['casa1.png', 'casa2.png', 'casa3.png', 'casa4.png', 'casa5.png', 'casa6.png', 'casa7.png', 'casa8.png', 'casa9.png',
                     'casa10.png','casa11.png']
        self.files_run = [asset_path + '/' + e for e in file_name]
        self.fileSizeRun = (300, 250)

        # file_name = ['casa1.png']
        # self.files_dead = [asset_path + '/' + e for e in file_name]
        # self.fileSizeDead = (300, 250)

        self.rect.w = self.fileSizeRun[0]
        self.rect.h = self.fileSizeRun[1]
        self.rect.x = df.display_width - self.rect.w
        self.rect.y = df.display_height - self.rect.h - 20
        self.u = 0
        self.y = 0

    def animate(self):
        if device.stats.life >90: self.index =0
        elif device.stats.life >80: self.index =1
        elif device.stats.life >70: self.index =2
        elif device.stats.life >60: self.index =3
        elif device.stats.life >50: self.index =4
        elif device.stats.life >40: self.index =5
        elif device.stats.life >30: self.index =6
        elif device.stats.life >20: self.index =7
        elif device.stats.life >10: self.index =8
        elif device.stats.life >5: self.index =9
        else: self.index = 10
        self.image = self.imagesRun[self.index]
        self.draw()




class Button(Sprite2):
    def __init__(self,filename,x,y):
        w = 70
        h = 70
        Sprite2.__init__(self, filename, x, y, w, h, 0, 0)
        self.hover_text = 'Back /Zurück/Atras'
        self.click_text = 'Loading/ Laden/ Caragando'
        self.font =  "monospace"
        self.font_size = 30
        self.txt_w = df.display_width
        self.txt_h = 30
        self.txt_x = 100
        self.txt_y = df.display_height - self.txt_h*2
        self.txt_color= df.gray
        self.hover_color = df.white
        self.click_color = df.red
        self.shadow_w = df.display_width
        self.shadow_h = df.display_width
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

    def draw_sprite2(self):
        var.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))

    def highlight(self,color):
        s = pygame.Surface((self.rect.w, self.rect.h))
        s.set_alpha(50)
        s.fill(color)
        pygame.draw.rect(var.gameDisplay, color, [self.rect.x, self.rect.y, self.rect.w, 1])
        pygame.draw.rect(var.gameDisplay, color, [self.rect.x, self.rect.y, 1, self.rect.h])
        pygame.draw.rect(var.gameDisplay, color, [self.rect.x, self.rect.y + self.rect.h, self.rect.w, 1])
        pygame.draw.rect(var.gameDisplay, color, [self.rect.x+self.rect.w, self.rect.y, 1, self.rect.h])
        var.gameDisplay.blit(s, (self.rect.x, self.rect.y))


    def new_shadow(self,color):
        s = pygame.Surface((self.txt_w, self.txt_h))
        s.set_alpha(50)
        s.fill(color)
        var.gameDisplay.blit(s, (self.shadow_x, self.shadow_y))

    def new_msg(self,text,color1, color2):
        self.new_shadow(color1)
        myfont = pygame.font.SysFont(self.font, self.font_size)
        label = myfont.render(text, 1, color2)
        var.gameDisplay.blit(label, (self.txt_x, self.txt_y))

    def onClick(self,mouse):

        if self.rect.collidepoint(mouse.get_pos()) == 1:
            self.highlight(self.hover_color)
            self.new_msg(self.hover_text, self.hover_color, self.txt_color)
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
            return False


    def update(self):
        for i in range(1,self.limit+1):
            self.time_to_born.append(i*1000)
        # print('ttb:',self.time_to_born)


class Button(Sprite2):
    def __init__(self,filename,x,y):
        w = 70
        h = 70
        Sprite2.__init__(self, filename, x, y, w, h, 0, 0)
        self.hover_text = 'Back /Zurück/Atras'
        self.click_text = 'Loading/ Laden/ Caragando'
        self.font =  "monospace"
        self.font_size = 30
        self.txt_w = df.display_width
        self.txt_h = 30
        self.txt_x = 100
        self.txt_y = df.display_height - self.txt_h*2
        self.txt_color= df.gray
        self.hover_color = df.white
        self.click_color = df.red
        self.shadow_w = df.display_width
        self.shadow_h = df.display_width
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

    def draw_sprite2(self):
        var.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))

    def highlight(self,color):
        s = pygame.Surface((self.rect.w, self.rect.h))
        s.set_alpha(50)
        s.fill(color)
        pygame.draw.rect(var.gameDisplay, color, [self.rect.x, self.rect.y, self.rect.w, 1])
        pygame.draw.rect(var.gameDisplay, color, [self.rect.x, self.rect.y, 1, self.rect.h])
        pygame.draw.rect(var.gameDisplay, color, [self.rect.x, self.rect.y + self.rect.h, self.rect.w, 1])
        pygame.draw.rect(var.gameDisplay, color, [self.rect.x+self.rect.w, self.rect.y, 1, self.rect.h])
        var.gameDisplay.blit(s, (self.rect.x, self.rect.y))


    def new_shadow(self,color):
        s = pygame.Surface((self.txt_w, self.txt_h))
        s.set_alpha(50)
        s.fill(color)
        var.gameDisplay.blit(s, (self.shadow_x, self.shadow_y))

    def new_msg(self,text,color1, color2):
        self.new_shadow(color1)
        myfont = pygame.font.SysFont(self.font, self.font_size)
        label = myfont.render(text, 1, color2)
        var.gameDisplay.blit(label, (self.txt_x, self.txt_y))

    def onClick(self,mouse):

        if self.rect.collidepoint(mouse.get_pos()) == 1:
            self.highlight(self.hover_color)
            self.new_msg(self.hover_text, self.hover_color, self.txt_color)
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
            self.new_msg(self.hover_text, self.click_color, self.click_color)
            self.txt_x += 4
            self.txt_y += 1
            self.shadow_x += 4
            self.shadow_y += 1
            self.animating = True
        else:
            self.animating = False
            self.txt_x = self.txt_x_d
            self.txt_y  = self.txt_y_d
            self.shadow_x = self.shadow_x_d
            self.shadow_y = self.shadow_y_d



class Imap(Button):
    def __init__(self,filename, x, y, level, gap, blocked, total_enemies):
        w = 60
        h = 60
        Button.__init__(self, filename, x, y)

        self.level = level
        self.blocked = blocked
        self.gap = gap
        self.total = total_enemies

        self.map_name = ""
        self.filename  = ""
        self.bfilename = var.assetsDir + "icons8-lock-100.png"
        self.lockpad = Sprite2(self.bfilename, x, y, int(w*0.5), int(h*0.5), 0, 0)

    def get_map_name(self):
        self.map_name = self.file.split("_", 1)[1]
        self.map_name = self.map_name.split(".", 1)[0]
        self.filename = var.assetsDir + "" + self.map_name + ".jpg"
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
