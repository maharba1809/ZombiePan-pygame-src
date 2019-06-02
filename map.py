
import sprites as sp
import defaults as df
import pygame
import re
import time
import generic as gen
import var
import play
import imp

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
        maps = []
        maps.append(sp.Sprite2(self.map1_file, 150, 50, 60, 60, 0, 0))
        maps.append(sp.Sprite2(self.map2_file, 300, 50, 60, 60, 0, 0))
        maps.append(sp.Sprite2(self.map3_file, 450, 50, 60, 60, 0, 0))
        maps.append(sp.Sprite2(self.map4_file, 600, 50, 60, 60, 0, 0))
        maps.append(sp.Sprite2(self.map5_file, 150, 150, 60, 60, 0, 0))
        maps.append(sp.Sprite2(self.map6_file, 300, 150, 60, 60, 0, 0))
        maps.append(sp.Sprite2(self.map7_file, 450, 150, 60, 60, 0, 0))
        maps.append(sp.Sprite2(self.map8_file, 600, 150, 60, 60, 0, 0))
        maps.append(sp.Sprite2(self.map9_file, 150, 250, 60, 60, 0, 0))
        maps.append(sp.Sprite2(self.map10_file, 300, 250, 60, 60, 0, 0))
        maps.append(sp.Sprite2(self.map11_file, 450, 250, 60, 60, 0, 0))
        maps.append(sp.Sprite2(self.map12_file, 600, 250, 60, 60, 0, 0))
        maps.append(sp.Sprite2(self.map13_file, 150, 350, 60, 60, 0, 0))
        maps.append(sp.Sprite2(self.map14_file, 300, 350, 60, 60, 0, 0))
        maps.append(sp.Sprite2(self.exit_file, 150, 500, 60, 60, 0, 0))


        while not self.stopEngine:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print('S')


            var.gameDisplay.fill(df.white)
            self.draw_sprite2(mapsback)
            for m in maps:
                self.draw_sprite2(m)

                if (m.rect.collidepoint(pygame.mouse.get_pos()) == 1):

                    s = pygame.Surface((m.rect.w, m.rect.h))
                    s.set_alpha(50)
                    s.fill((255, 255, 255))
                    var.gameDisplay.blit(s, (m.rect.x, m.rect.y))

                    if re.search("exit", m.file, flags=0):
                        self.draw_selected((m.rect.x + m.rect.w + 10, m.rect.y + m.rect.h * 0.5 - 15), (df.display_width, 20), 100,
                                      df.white)
                        self.message_display("Return Main Menu /Zuruck/Atras", "monospace", 20,
                                        (m.rect.x + m.rect.w + 10, m.rect.y + m.rect.h * 0.5 - 15), df.red)
                    else:
                        self.message_display('Select a Map/Auswählen/Selecciona/', "monospace", 30, (100, 0), df.orange)
                        s = pygame.Surface((df.display_width, 20))
                        s.set_alpha(100)
                        s.fill(df.white)
                        var.gameDisplay.blit(s, (0, 570))
                        self.message_display(m.file, "monospace", 20, (150, 570), df.red)
                    if pygame.mouse.get_pressed()[0]:

                        if re.search("exit", m.file, flags=0):
                            self.stopEngine = True
                            # engineExit = True
                            # menuExit = False

                        else:
                            map_name = m.file.split("_", 1)[1]
                            map_name = map_name.split(".", 1)[0]
                            map_settings = []
                            map_settings.append(m.file)
                            map_settings.append(df.display_height * 0.08)
                            map_settings.append(var.assetsDir + "" + map_name + ".jpg")

                            self.message_display(m.file, "monospace", 20, (150, 570), df.blue)
                            self.message_display("Loading/Laden/Cargando " + map_settings[2], "monospace", 20, (100, 420),
                                            df.violet)
                            pygame.display.update()


                            if (maps.index(m) == 0): var.total = 10
                            if (maps.index(m) == 1): var.total = 12
                            if (maps.index(m) == 2): var.total = 14
                            if (maps.index(m) == 3): var.total = 16
                            if (maps.index(m) == 4): var.total = 17
                            if (maps.index(m) == 5): var.total = 18
                            if (maps.index(m) == 6): var.total = 19
                            if (maps.index(m) == 7): var.total = 20
                            if (maps.index(m) == 8): var.total = 23
                            if (maps.index(m) == 9): var.total = 26
                            if (maps.index(m) == 10): var.total = 29
                            if (maps.index(m) == 11): var.total = 31
                            if (maps.index(m) == 12): var.total = 35
                            if (maps.index(m) == 13): var.total = 45
                            var.map_settings = map_settings
                            imp.reload(play)
                            playScreen = play.AddScreen()
                            time.sleep(0.5)
                            # playScreen.stopEngine=False
                            playScreen.run()
            pygame.display.update()

            var.clock.tick(20)
