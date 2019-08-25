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
        self.fileSizeRun = (75, 77)

        file_name = ['Dead1.png','Dead2.png','Dead3.png','Dead4.png','Dead5.png','Dead6.png','Dead7.png','Dead8.png']
        self.files_dead = [asset_path + '/' + e for e in file_name]
        self.fileSizeDead = (96, 77)

        file_name =['attack_1.png', 'attack_2.png', 'attack_3.png', 'attack_4.png', 'attack_5.png']
        self.files_attack = [asset_path + '/' + e for e in file_name]
        self.fileSizeAttack = (52, 77)

        self.startHit = False
        self.attack_delay = 15 #fps
        self.attack_count = 0
        self.damage_rate = 2
        self.endHit = False
        self.preattack = False
        self.running = True
        self.index = 0
        self.dead = False
        self.life = 100
        self.dead_rate = 50
        self.loop_index = 0
        self.fps = 2


    def load_images(self):
        print('\n')
        for item in self.files_run:
            print('loading file', item)
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
            self.imagesAttack.append(pygame.transform.scale(images, self.fileSizeAttack))



    def animate_preattack(self):
        # print('preattack')
        self.image = self.imagesAttack[0]
        # print("delay ", self.attack_count)
        if self.attack_count < self.attack_delay:
            # print('idle')
            self.image = self.imagesAttack[0]
            self.attack_count += 1
        else:
            self.startHit = True  # trigger hit
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
            self.startHit = False
            self.running = True
            self.endHit = True
            # print('under attacking!')
            if device.audio.sound_enabled: device.audio.sound_attack.play()
            # device.stats.add_damage(self.damage_rate)


        if self.rect.w != self.fileSizeAttack[0]: self.rect.w = self.fileSizeAttack[0]
        if self.rect.h != self.fileSizeAttack[1]: self.rect.h = self.fileSizeAttack[1]

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
        else:
            self.dead = True

        if self.rect.w != self.fileSizeDead[0]: self.rect.w = self.fileSizeDead[0]
        if self.rect.h != self.fileSizeDead[0]: self.rect.h = self.fileSizeDead[1]

    def animate(self, dt):
        if self.alive:  # lived animation - Run
            
            if self.running:
                if self.loop_index > self.fps:
                    self.animate_run()
                    self.loop_index = 0
                else:
                    self.loop_index += 1
                
                self.move(dt)

            if self.preattack:
                if self.loop_index > self.fps:
                    self.animate_preattack()
                    self.loop_index = 0
                else:
                    self.loop_index += 1

            if self.startHit:
                #if self.loop_index > self.fps:
                    self.animate_hit()
                    #self.loop_index = 0
                #else:
                    #self.loop_index += 4
            
        else:
            if self.loop_index > self.fps:
                self.animate_death()
                self.loop_index = 0
            else:
                self.loop_index += 1
                
        var.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))

    def move(self,dt):
        # print(self.u)
        if self.rect.x + self.rect.w >= df.display_width:
            if self.u > 0:
                self.rect.x -= self.u
                self.u = -self.u
                if device.audio.sound_enabled: device.audio.sound_bullet.play()

        # if self.rect.x < 0:
        #     if self.u < 0:
        #         self.rect.x -= self.u
        #         self.u = -self.u
        #         if device.audio.sound_enabled: device.audio.sound_bullet.play()
        self.rect.x += self.u * dt / 10
        self.rect.y += self.v * dt / 10
        # print(self.rect.x)

    def descrease_life(self):
        self.life -= self.dead_rate
        if self.life <=0:
            self.alive = False

class ChildEnemy(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        asset_path = var.assetsDir + "/kid"

        file_name = ['run_01.png','run_02.png','run_03.png','run_04.png','run_05.png','run_06.png','run_07.png','run_08.png','run_09.png','run_10.png']
        self.files_run = [asset_path + '/' + e for e in file_name]
        self.fileSizeRun = (54, 77)

        file_name = ['dead_01.png', 'dead_02.png', 'dead_03.png', 'dead_04.png', 'dead_05.png', 'dead_06.png', 'dead_07.png', 'dead_08.png', 'dead_08.png',
                     'dead_10.png']
        self.files_dead = [asset_path + '/' + e for e in file_name]
        self.fileSizeDead = (81, 77)

        file_name = ['attack_1.png', 'attack_2.png', 'attack_3.png', 'attack_4.png', 'attack_5.png', 'attack_6.png', 'attack_7.png']
        self.files_attack = [asset_path + '/' + e for e in file_name]
        self.fileSizeAttack = (66, 77)

        self.damage_rate = 2
        self.dead_rate = 34

class MariaEnemy(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        asset_path = var.assetsDir + "maria100"

        file_name = ['run_1.png','run_2.png','run_3.png','run_4.png','run_5.png','run_6.png']
        self.files_run = [asset_path + '/' + e for e in file_name]
        self.fileSizeRun = (63, 77)

        file_name = ['dead_1.png', 'dead_2.png', 'dead_3.png', 'dead_4.png', 'dead_5.png', 'dead_6.png', 'dead_7.png', 'dead_8.png']
        self.files_dead = [asset_path + '/' + e for e in file_name]
        self.fileSizeDead = (112, 77)

        file_name = ['attack_1.png', 'attack_2.png', 'attack_3.png', 'attack_4.png', 'attack_5.png', 'attack_6.png']
        self.files_attack = [asset_path + '/' + e for e in file_name]
        self.fileSizeAttack = (57, 77)

        self.damage_rate = 2
        self.dead_rate = 50

class PirateEnemy(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        asset_path = var.assetsDir + "pirat100"

        file_name = ['run_1.png','run_2.png','run_3.png','run_4.png','run_5.png','run_6.png']
        self.files_run = [asset_path + '/' + e for e in file_name]
        self.fileSizeRun = (70, 77)

        file_name = ['dead_1.png', 'dead_2.png', 'dead_3.png', 'dead_4.png', 'dead_5.png', 'dead_6.png', 'dead_7.png', 'dead_8.png']
        self.files_dead = [asset_path + '/' + e for e in file_name]
        self.fileSizeDead = (108, 77)

        file_name = ['attack_1.png', 'attack_2.png', 'attack_3.png', 'attack_4.png', 'attack_5.png', 'attack_6.png']
        self.files_attack = [asset_path + '/' + e for e in file_name]
        self.fileSizeAttack = (50, 76)

        self.damage_rate = 3
        self.dead_rate = 25

class Horde():

    def __init__(self):
        self.enemies = []
        self.limit = 0
        self.count = 0
        self.map_gap = 0
        self.time_to_born = []
        self.umax = 2

    def born(self):

        dx = -df.display_width / self.limit
        x = int(dx)
        # print(self.limit)
        for item in range(0, self.limit):
            random_enemy = int(random.random()*1000)
            if random_enemy % 2 == 0:
                enemy = MariaEnemy()
                enemy.u = 1
            elif random_enemy % 3 == 0:
                enemy = ChildEnemy()
                enemy.u = 2
            elif random_enemy % 5 == 0:
                enemy = PirateEnemy()
                enemy.u = 1.5
            else:
                enemy = Enemy()
                enemy.u = 0.8


            enemy.load_images()
            # print(enemy.rect.h)
            enemy.rect.y = df.display_height - self.map_gap - enemy.rect.h - 10*random.random()
            enemy.rect.x = x
            x += dx
            # print(item)

            self.enemies.append(enemy)

