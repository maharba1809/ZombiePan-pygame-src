
import sprites as sp
import defaults as df
import pygame
import re
import time
import generic as gen
import var
import play
import imp
import device

print('Loading map')

class AddScreen(gen.Xscreen):
    def __init__(self):
        gen.Xscreen.__init__(self)
        self.background_file = var.assetsDir + 'maps_board.jpg'
        self.buy_file = var.assetsDir + 'buy_yes.png'
        self.background_file = var.assetsDir + 'maps_board.jpg'


        self.map1_file = var.assetsDir + 'icon_map1.png'
        self.map2_file = var.assetsDir + 'icon_map2.png'
        self.map3_file = var.assetsDir + 'icon_map3.png'
        self.map4_file = var.assetsDir + 'icon_map4.png'
        self.map5_file = var.assetsDir + 'icon_map5.png'
        self.map6_file = var.assetsDir + 'icon_map6.png'
        self.map7_file = var.assetsDir + 'icon_map7.png'
        self.map8_file = var.assetsDir + 'icon_map8.png'
        self.map9_file = var.assetsDir + 'icon_map9.png'
        self.map10_file = var.assetsDir + 'icon_map10.png'
        self.map11_file = var.assetsDir + 'icon_map11.png'
        self.map12_file = var.assetsDir + 'icon_map12.png'
        self.map13_file = var.assetsDir + 'icon_map13.png'
        self.map14_file = var.assetsDir + 'icon_map14.png'
        self.exit_file = var.assetsDir + 'Button_exit.png'

        print('map screen created')


    def run(self):
        print('running maps')

        mapsback = sp.Sprite2(self.background_file, 0, 0, df.display_width, df.display_height, 0, 0)
        if not len(device.stats.maps)>0:
            maps = []
            maps.append(sp.Imap(self.map1_file, 150, 50, 1, 20, False, 20))
            maps.append(sp.Imap(self.map2_file, 300, 50, 2, 20, True, 30))
            maps.append(sp.Imap(self.map3_file, 450, 50, 3, 20, True, 40))
            maps.append(sp.Imap(self.map4_file, 600, 50, 4, 20, True, 50))
            maps.append(sp.Imap(self.map5_file, 150, 150, 5, 20, True, 55))
            maps.append(sp.Imap(self.map6_file, 300, 150, 6, 20, True, 60))
            maps.append(sp.Imap(self.map7_file, 450, 150, 7, 20, True, 65))
            maps.append(sp.Imap(self.map8_file, 600, 150, 8, 20, True, 70))
            maps.append(sp.Imap(self.map9_file, 150, 250, 9, 20, True, 75))
            maps.append(sp.Imap(self.map10_file, 300, 250, 10, 20, True, 80))
            maps.append(sp.Imap(self.map11_file, 450, 250, 11, 20, True, 85))
            maps.append(sp.Imap(self.map12_file, 600, 250, 12, 20, True, 90))
            maps.append(sp.Imap(self.map13_file, 150, 350, 13, 20, True, 95))
            maps.append(sp.Imap(self.map14_file, 300, 350, 14, 20, True, 100))
            # maps.append(sp.Imap(self.map14_file, 300, 350, 14, 20, False, 1))
            for m in maps:
                m.hover_text = m.file
                # m.rect.w = 50
                # m.rect.h = 50

        else:
            maps = device.stats.maps
        button_back = sp.Button(self.exit_file, 400, 450)

        total_time = 0
        while not self.stopEngine:
            time_start = pygame.time.get_ticks()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    print('Exit maps')
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print('S')

            var.gameDisplay.fill(df.white)
            self.draw_sprite2(mapsback)

            if button_back.onClick(pygame.mouse):
                self.stopEngine = True

            for m in maps:
                if m.onClick(pygame.mouse):

                    device.stats.level = m.level
                    m.get_map_name()
                    device.stats.map_name = m.filename

                    if not m.blocked:
                        imp.reload(play)
                        playScreen = play.AddScreen(m)

                        time.sleep(0.5)
                        playScreen.run()
                        if device.stats.winner:
                            index = device.stats.level
                            if index > 0:
                                if index < len(maps):
                                    print('unblocking the next map')
                                    maps[index].blocked =False
                                    device.stats.maps = maps
                    else:
                        m.hover_text = "Map is blocked!"
                        print('map Blocked:',m.filename)

                m.draw_block()
            pygame.display.update()

            var.clock.tick(var.fps)

        print('Leaving Map screen')