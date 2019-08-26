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
        self.font1.color = df.orange
        self.font1.font_size = 40
        self.font1.set_font()



    def run(self):
        # background = sp.Sprite2(v, 0, 0, df.display_width, df.display_height, 0, 0)

        mapsback = sp.Sprite2()
        mapsback.file = var.assetsDir + 'backgrounds/end.jpg'
        mapsback.w = df.display_width
        mapsback.h = df.display_height
        mapsback.set_image()
        mapsback.rect.x = 0
        mapsback.rect.y = 0

        total_time = 0
        #
        # horde = zmb.Horde()
        # horde.map_gap = 10
        # horde.limit = 200
        # # horde.update()
        horde = zmb.Horde()
        horde.map_gap = 10
        horde.limit = 100
        horde.born()

        # for i in range(1, horde.limit + 1):
        #     horde.time_to_born.append(i * 100)
        #
        dt = 50
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
            self.draw_sprite2(mapsback)


            for enemy in horde.enemies:
                enemy.animate(dt)
                # print(enemy.rect.x)


            self.draw_selected((35,0), (df.display_width, 50), 100, df.white)
            self.message_display('Thanks.. Danke... Gracias', (35, 20))
            dt = pygame.time.get_ticks() - time_start

            pygame.display.update()
            # var.clock.tick(var.fps)
            total_time += dt

