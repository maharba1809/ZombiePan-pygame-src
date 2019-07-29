import sprites as sp
import pygame
import var
import random
import time
import generic as gen
import defaults as df
import device
import zombies as zmb
print('Loading final')
class AddScreen(gen.Xscreen):
    def __init__(self):
        gen.Xscreen.__init__(self)
        print('final screen created')
        self.font = pygame.font.Font("assets/fonts/horrendo.ttf", 40)


    def run(self):

        background = sp.Sprite2(var.assetsDir + 'backgrounds/end.jpg', 0, 0, df.display_width, df.display_height, 0, 0)
        total_time = 0

        horde = zmb.Horde()
        horde.map_gap = 10
        horde.limit = 200
        horde.update()

        for i in range(1, horde.limit + 1):
            horde.time_to_born.append(i * 100)


        while not self.stopEngine:
            time_start = pygame.time.get_ticks()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.stopEngine = True
            var.gameDisplay.fill(df.black)
            self.draw_sprite2(background)

            horde.enemy_control(total_time)
            for enemy in horde.enemies:
                enemy.animate()
                # print(enemy.rect.x)


            self.draw_selected((0, 20), (df.display_width, 40), 100, df.white)
            self.message_display('Thanks.. Danke... Gracias', "monospace", 40, (35, 20), df.red)
            dt = pygame.time.get_ticks() - time_start
            total_time += dt
            pygame.display.update()
            var.clock.tick(var.fps)


