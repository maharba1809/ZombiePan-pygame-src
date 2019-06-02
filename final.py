import sprites as sp
import pygame
import var
import random

import generic as gen
import defaults as df
import device

print('Loading final')
class AddScreen(gen.Xscreen):
    def __init__(self):
        gen.Xscreen.__init__(self)
        print('final screen created')


    def run(self):

        background = sp.Sprite2(var.assetsDir + 'end.jpg', 0, 0, df.display_width, df.display_height, 0, 0)

        filesRun = [var.assetsDir + 'Run1.png', var.assetsDir + 'Run2.png', var.assetsDir + 'Run3.png', var.assetsDir + 'Run4.png',
                    var.assetsDir + 'Run5.png', var.assetsDir + 'Run6.png']
        height = 77 * 1
        width = 70 * 1
        filesRunSize = (height, width)
        filesDead = [var.assetsDir + 'Dead1.png', var.assetsDir + 'Dead2.png', var.assetsDir + 'Dead3.png', var.assetsDir + 'Dead4.png',
                     var.assetsDir + 'Dead5.png', var.assetsDir + 'Dead6.png', var.assetsDir + 'Dead7.png', var.assetsDir + 'Dead8.png']
        filesDeadSize = (96, 77)
        files = [filesRun, filesRunSize, filesDead, filesDeadSize]

        group_enemies = []
        group_enemies.append(sp.Sprite3(files, 0, df.display_height - 20 - height - 20, 5.0, 0))
        group_enemies.append(sp.Sprite3(files, 0, df.display_height - 20 - height + 0, 9.0, 0))
        group_enemies.append(sp.Sprite3(files, 0, df.display_height - 20 - height + 10, 8.0, 0))
        group_enemies.append(sp.Sprite3(files, 0, df.display_height - 20 - height - 20, 8.0, 0))
        group_enemies.append(sp.Sprite3(files, 0, df.display_height - 20 - height + 0, 5.0, 0))
        group_enemies.append(sp.Sprite3(files, 0, df.display_height - 20 - height + 15, 4.0, 0))
        group_enemies.append(sp.Sprite3(files, 0, df.display_height - 20 - height - 20, 3.0, 0))
        group_enemies.append(sp.Sprite3(files, 0, df.display_height - 20 - height + 10, 2.0, 0))
        group_enemies.append(sp.Sprite3(files, 0, df.display_height - 20 - height + 15, 3.0, 0))
        group_enemies.append(sp.Sprite3(files, 0, df.display_height - 20 - height + 15, 3.0, 0))

        # KEnemy----------------------------------------------------------------------------------------------------------
        filename = ['kz1.png', 'kz2.png', 'kz3.png', 'kz4.png', 'kz5.png', 'kz6.png', 'kz7.png', 'kz8.png', 'kz9.png',
                    'kz10.png']
        filesRun = []
        for i in filename:
            filesRun.append(var.assetsDir + i)

        filename = ['zd1.png', 'zd2.png', 'zd3.png', 'zd4.png', 'zd5.png', 'zd6.png', 'zd7.png', 'zd8.png', 'zd9.png',
                    'zd10.png']
        filesDead = []
        for i in filename:
            filesDead.append(var.assetsDir + i)

        filesRunSize = (70, 77)
        filesDeadSize = (70, 77)

        files = [filesRun, filesRunSize, filesDead, filesDeadSize]

        y0 = df.display_height - var.map_gap - filesRunSize[1]
        group_enemies.append(sp.Sprite3(files, 0, y0 + 10, 2, 0))

        y0 = df.display_height - var.map_gap - filesRunSize[1]
        group_enemies.append(sp.Sprite3(files, 0, y0 - 10, 3, 0))

        y0 = df.display_height - var.map_gap - filesRunSize[1]
        group_enemies.append(sp.Sprite3(files, 0, y0 - 10, 4, 0))

        y0 = df.display_height - var.map_gap - filesRunSize[1]
        group_enemies.append(sp.Sprite3(files, 0, y0 - 10, 5, 0))

        while not self.stopEngine:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.stopEngine = True

            var.gameDisplay.fill(df.black)
            self.draw_sprite2(background)

            for enemy in group_enemies:
                if enemy.rect.x == 0:
                    enemy.rect.x += 2
                    mood = 1.5 + random.random()
                    # enemy.u = enemy.u * mood
                    # if enemy.u > 5:
                    #    enemy.u = 2.0
                    # if enemy.u < 1:
                    #    enemy.u = 2.0

                if enemy.rect.x > df.display_width:
                    enemy.rect.x = 0
                else:
                    self.draw_sprite2(enemy)
                    enemy.update()
                    enemy.rect.x += enemy.u
                    enemy.rect.y += enemy.v

            self.draw_selected((0, 20), (df.display_width, 40), 100, df.white)
            self.message_display('Thanks.. Danke... Gracias', "monospace", 40, (35, 20), df.blue)

            pygame.display.update()
            var.clock.tick(var.fps)

