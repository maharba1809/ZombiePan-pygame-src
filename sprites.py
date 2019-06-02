import pygame
import os
import defaults as df
import var
import device
import random
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
        self.lived = True#declares status
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
        if self.lived:#lived animation - Run
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

    def physics(self):
        if self.rect.x + self.rect.w >= df.display_width:
            if self.u > 0:
                self.rect.x -= self.u
                self.u = -self.u
                if device.audio.sound_enabled: device.audio.sound_hel.play()


        if self.rect.x < 0:
            if self.u < 0:
                self.rect.x -= self.u
                self.u = -self.u
                if device.audio.sound_enabled: device.audio.sound_hel.play()

class AddBullet(Sprite2):
    def __init__(self,x,y):
        self.image_file = var.assetsDir + 'bullet1.png'
        w = 12
        h = 18
        u = 0
        v = 9
        Sprite2.__init__(self,self.image_file,x,y, w, h, u, v)

        # newbullet = self.Sprite2(var.assetsDir + 'bullet1.png', xb, yb, 12, 18, hel.u, 9)

class Weapon():
    def __init__(self,x,y):
        self.magazine = []
        self.limit = 5
        self.x = 0
        self.y = 0
        self.uinert = 0

    def shoot_bullet(self):
        new_bullet = AddBullet(self.x,self.y)
        if len(self.magazine) < self.limit:
            self.magazine.append(new_bullet)
        else:
            print('Weapon overload')

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
                bullet.u = self.uinert
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
        # self.rect = pygame.Rect(x, y, 10, 10)
        self.rect = self.image.get_rect()

        self.u = 2
        self.v = 0
        self.lived = True  # declares status
        self.uDefault = 9
        self.col = False
        self.imagesRun = []
        self.imagesDead = []
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 10
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
        if self.lived:  # lived animation - Run
            if self.files_run:
                if self.index < len(self.files_run):
                    self.image = self.imagesRun[self.index]
                    self.index += 1
                else:
                    self.index = 0
                if self.rect.w !=  self.fileSizeRun[0]:self.rect.w = self.fileSizeRun[0]
                if self.rect.h !=  self.fileSizeRun[1]:self.rect.h = self.fileSizeRun[1]

        else:
            if self.u!=0:
                self.index = 0
                self.u = 0
            # print(self.files_dead,len(self.files_dead),self.index,'index')
            if self.files_dead:
                if self.index < len(self.files_dead):
                    self.image = self.imagesDead[self.index]
                    self.index += 1
                else:
                    self.index == 0
                    self.col = True
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

class Enemy(Asprite):
    def __init__(self):
        Asprite.__init__(self)
        self.files_run = []
        self.files_run.append(var.assetsDir + 'Run1.png')
        self.files_run.append(var.assetsDir + 'Run2.png')
        self.files_run.append(var.assetsDir + 'Run3.png')
        self.files_run.append(var.assetsDir + 'Run4.png')
        self.files_run.append(var.assetsDir + 'Run5.png')
        self.files_run.append(var.assetsDir + 'Run6.png')
        self.fileSizeRun = (70, 77)
        self.files_dead = []
        self.files_dead.append(var.assetsDir + 'Dead1.png')
        self.files_dead.append(var.assetsDir + 'Dead2.png')
        self.files_dead.append(var.assetsDir + 'Dead3.png')
        self.files_dead.append(var.assetsDir + 'Dead4.png')
        self.files_dead.append(var.assetsDir + 'Dead5.png')
        self.files_dead.append(var.assetsDir + 'Dead6.png')
        self.files_dead.append(var.assetsDir + 'Dead7.png')
        self.files_dead.append(var.assetsDir + 'Dead8.png')
        self.fileSizeDead = (96, 77)

        self.damage = 0

    def move(self):
        # print(self.u)
        if self.rect.x + self.rect.w >= df.display_width:
            # self.u = 0
            self.rect.x = self.rect.x - self.u*4
            # print(self.rect.x)
            # if device.audio.sound_enabled: self.sound.play()
            self.damage = self.damage +1

        self.rect.x += self.u
        self.rect.y += self.v


class ChildEnemy(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.files_run = []
        self.files_run.append(var.assetsDir + 'kz1.png')
        self.files_run.append(var.assetsDir + 'kz2.png')
        self.files_run.append(var.assetsDir + 'kz3.png')
        self.files_run.append(var.assetsDir + 'kz4.png')
        self.files_run.append(var.assetsDir + 'kz5.png')
        self.files_run.append(var.assetsDir + 'kz6.png')
        self.files_run.append(var.assetsDir + 'kz7.png')
        self.files_run.append(var.assetsDir + 'kz8.png')
        self.files_run.append(var.assetsDir + 'kz9.png')
        self.files_run.append(var.assetsDir + 'kz10.png')
        self.fileSizeRun = (70, 77)
        self.files_dead = []
        self.files_dead.append(var.assetsDir + 'zd1.png')
        self.files_dead.append(var.assetsDir + 'zd2.png')
        self.files_dead.append(var.assetsDir + 'zd3.png')
        self.files_dead.append(var.assetsDir + 'zd4.png')
        self.files_dead.append(var.assetsDir + 'zd5.png')
        self.files_dead.append(var.assetsDir + 'zd6.png')
        self.files_dead.append(var.assetsDir + 'zd7.png')
        self.files_dead.append(var.assetsDir + 'zd8.png')
        self.files_dead.append(var.assetsDir + 'zd9.png')
        self.files_dead.append(var.assetsDir + 'zd10.png')
        self.fileSizeDead = (70, 77)


class Horde():
    def __init__(self):
        self.enemies = []
        self.limit = var.total

    def new_horde(self):
        for i in range(0, self.limit):
            if i % 2:
                enemy = Enemy()
            else:
                enemy = ChildEnemy()
             # print(enemy.files_run)
            enemy.load_images()
            enemy.rect.y =  df.display_height - var.map_gap - 77*random.random()

            enemy.u = 2 +random.random()*2
            if len(self.enemies)>0:
                while abs (enemy.u -self.enemies[-1].u) <0.5:
                    enemy.u = 2 + random.random()*2
                    # print(enemy.u)

            self.enemies.append(enemy)



