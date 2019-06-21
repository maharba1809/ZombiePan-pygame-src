import random
import var
import device
import defaults as df
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = []
        self.u = 0
        self.v = 0
        self.alive = True  # declares status
        self.col = False
        self.imagesRun = []
        self.imagesDead = []
        self.imagesAttack = []
        # self.sound = device.audio.sound_hel
        asset_path = var.assetsDir + "/baldy"
        file_name = ['Run1.png','Run2.png','Run3.png','Run4.png','Run5.png','Run6.png']
        self.files_run = [asset_path + '/' + e for e in file_name]
        self.fileSizeRun = (70, 77)

        file_name = ['Dead1.png','Dead2.png','Dead3.png','Dead4.png','Dead5.png','Dead6.png','Dead7.png','Dead8.png']
        self.files_dead = [asset_path + '/' + e for e in file_name]
        self.fileSizeDead = (96, 77)

        file_name =['Attack1.png','Attack2.png','Attack3.png','Attack4.png','Attack5.png']
        self.files_attack = [asset_path + '/' + e for e in file_name]
        self.size_attack = (50, 77)

        self.hit = False
        self.attack_delay = 30 #fps
        self.attack_count = 0
        self.damage_rate = 4
        self.hitting = False
        self.preattack = False
        self.running = True
        self.index = 0

    def load_images(self):
        print('\n')
        for item in self.files_run:
            print('loading file',item)
            images = pygame.image.load(item)
            self.imagesRun.append(pygame.transform.scale(images, self.fileSizeRun))

        self.image = self.imagesRun[0]
        self.rect = self.image.get_rect()
        self.rect.w = self.fileSizeRun[0]
        self.rect.h = self.fileSizeRun[1]


        for item in self.files_dead:
            print('loading file', item)
            images = pygame.image.load(item)
            self.imagesDead.append(pygame.transform.scale(images, self.fileSizeDead))


        for item in self.files_attack:
            print('loading file', item)
            images = pygame.image.load(item)
            self.imagesAttack.append(pygame.transform.scale(images, self.size_attack))



    def animate_preattack(self):
        # print('preattack')
        self.image = self.imagesAttack[0]
        # print("delay ", self.attack_count)
        if self.attack_count < self.attack_delay:
            # print('idle')
            self.image = self.imagesAttack[0]
            self.attack_count += 1
        else:
            self.hit = True  # trigger hit
            self.attack_count = 0  # return new attack
            self.preattack = False



    def animate_hit(self):
        # print('hitting')
        # hitting animation

        if self.index < len(self.files_attack):
            self.image = self.imagesAttack[self.index]
            self.index += 1
        else:
            # stops hitting animation
            self.index = 0
            self.hit = False
            self.running = True
            # print('under attacking!')
            if device.audio.sound_enabled:
                device.audio.sound_attack.play()
            device.stats.add_damage(self.damage_rate)


        if self.rect.w != self.size_attack[0]: self.rect.w = self.size_attack[0]
        if self.rect.h != self.size_attack[1]: self.rect.h = self.size_attack[1]

    def animate_run(self):
        # print('running')
        if self.index < len(self.files_run):
            self.image = self.imagesRun[self.index]
            self.index += 1
            # print(self.index, len(self.files_run))

        else:
            self.index = 0
        # print(self.index)

            # stops running animation
        if self.rect.w != self.fileSizeRun[0]: self.rect.w = self.fileSizeRun[0]
        if self.rect.h != self.fileSizeRun[1]: self.rect.h = self.fileSizeRun[1]

    def animate_death(self):
        # print('dead')
        if self.u != 0:
            self.index = 0
            self.u = 0
            # print(self.files_dead,len(self.files_dead),self.index,'index')
        if self.index < len(self.files_dead):
            self.image = self.imagesDead[self.index]
            self.index += 1
        # else:
            #     self.index = 0
            #     self.col = True
        if self.rect.w != self.fileSizeDead[0]: self.rect.w = self.fileSizeDead[0]
        if self.rect.h != self.fileSizeDead[0]: self.rect.h = self.fileSizeDead[1]

    def animate(self):
        if self.alive:  # lived animation - Run

            if self.running:
                self.animate_run()
                self.move()

            if self.preattack:
                self.animate_preattack()

            if self.hit:
                self.animate_hit()

        else:
            self.animate_death()

        var.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        # print(self.u)
        if self.rect.x + self.rect.w >= df.display_width:
            if self.u > 0:
                self.rect.x -= self.u
                self.u = -self.u
                if device.audio.sound_enabled: device.audio.sound_bullet.play()

        if self.rect.x < 0:
            if self.u < 0:
                self.rect.x -= self.u
                self.u = -self.u
                if device.audio.sound_enabled: device.audio.sound_bullet.play()
        self.rect.x += self.u
        self.rect.y += self.v


class ChildEnemy(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        asset_path = var.assetsDir + "/kid"

        file_name = ['kz1.png','kz2.png','kz3.png','kz4.png','kz5.png','kz6.png','kz7.png','kz8.png','kz9.png','kz10.png']
        self.files_run = [asset_path + '/' + e for e in file_name]
        self.fileSizeRun = (70, 77)

        file_name = ['zd1.png', 'zd2.png', 'zd3.png', 'zd4.png', 'zd5.png', 'zd6.png', 'zd7.png', 'zd8.png', 'zd9.png',
                     'zd10.png']
        self.files_dead = [asset_path + '/' + e for e in file_name]
        self.fileSizeDead = (70, 77)

        file_name = ['Attack (1).png', 'Attack (2).png', 'Attack (3).png', 'Attack (4).png', 'Attack (5).png', 'Attack (6).png', 'Attack (7).png', 'Attack (8).png']
        self.files_attack = [asset_path + '/' + e for e in file_name]
        self.size_attack = (60, 77)

        self.damage_rate = 2

class Horde():

    def __init__(self):
        self.enemies = []
        self.limit = 0
        self.count = 0
        self.map_gap = 0
        self.time_to_born = []
        self.umax = 2

    def new_enemy(self):
        if self.count < self.limit:
            if int(random.random()*100) % 2 ==0:
                enemy = Enemy()
                # print('New bald zombie')
            else:
                enemy = ChildEnemy()
                # print('New kid zombie')
            # enemy2 = ChildEnemy()
            self.count += 1
            enemy.load_images()
            # print(enemy.rect.h)
            enemy.rect.y =  df.display_height - self.map_gap - enemy.rect.h - 20*random.random()
            # enemy.rect.y =  df.display_height - self.map_gap - 77*random.random()

            enemy.u = 3*(1+random.random())
            # print(enemy.u)

            self.enemies.append(enemy)


    def enemy_control(self,t0):
        if self.time_to_born:
            if t0 >= self.time_to_born[0]:
                self.new_enemy()
                del self.time_to_born[0]



    def update(self):
        for i in range(1,self.limit+1):
            self.time_to_born.append(i*500)
        # print('ttb:',self.time_to_born)
