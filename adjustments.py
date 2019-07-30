print('loading Adjustments')
import sprites as sp
import defaults as df
import pygame
import re
import time
import generic as gen
import var
import device


class AddScreen(gen.Xscreen):
    def __init__(self):
        gen.Xscreen.__init__(self)


        self.background_file = var.assetsDir + 'maps_board.jpg'

        self.enable_file = var.assetsDir + 'enabled.png'
        self.disable_file = var.assetsDir + 'disabled.png'

        self.buy_file = var.assetsDir + 'buy_yes.png'
        self.back_txt = "Return/Zuruck/Atras"
        self.music_enable_txt = "Music Enabled/Aktiviert/Activado"
        self.music_disable_txt = "Music Disabled/Deaktiviert/Desactivado"
        self.sound_disable_txt = "Sound Disabled/Deactiviert/Desactivado"
        self.sound_enable_txt = "Sound Enabled/Deactiviert/Desactivado"
        self.opt_txt = "Options/Auswählen/Opciones"
        self.music_txt = "Music/Musik/Musica"
        self.sound_txt = "Sounds/Klänge/Sonidos"
        print('Adjustments screen created')
        self.font_size = 40
        self.font = pygame.font.Font("assets/fonts/horrendo.ttf", self.font_size)
        self.text_info_y = df.display_height*0.9


    def run(self):


        mapsback = sp.Sprite2(self.background_file, 0, 0, df.display_width, df.display_height, 0, 0)
        btn = []

        if device.audio.music_enabled:
            btn.append(sp.Sprite2(self.enable_file, df.display_width*0.7, 200, 50, 50, 0, 0))
        else:
            btn.append(sp.Sprite2(self.disable_file,  df.display_width*0.7, 200, 50, 50, 0, 0))

        if device.audio.sound_enabled:
            btn.append(sp.Sprite2(self.enable_file,  df.display_width*0.7, 300, 50, 50, 0, 0))
        else:
            btn.append(sp.Sprite2(self.disable_file,  df.display_width*0.7, 300, 50, 50, 0, 0))

        btn.append(sp.Sprite2(self.buy_file,  df.display_width*0.5,  df.display_height*0.7, 100, 100, 0, 0))

        while not self.stopEngine:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            var.gameDisplay.fill(df.white)
            self.draw_sprite2(mapsback)

            for m in btn:
                self.draw_sprite2(m)

                if (m.rect.collidepoint(pygame.mouse.get_pos()) == 1):

                    s = pygame.Surface((m.rect.w, m.rect.h))
                    s.set_alpha(50)
                    s.fill((255, 255, 255))
                    var.gameDisplay.blit(s, (m.rect.x, m.rect.y))
                    if re.search("yes", m.file, flags=0):
                        self.draw_selected((0, self.text_info_y), (df.display_width, self.font_size), 100, df.white)
                        self.message_display(self.back_txt, "monospace", 20, (df.display_height*0.4, self.text_info_y), df.black)

                        if pygame.mouse.get_pressed()[0]:
                            self.stopEngine = True
                            # self.menuExit = False

            if btn[0].rect.collidepoint(pygame.mouse.get_pos()) == 1:
                self.draw_selected((0, self.text_info_y), (df.display_width, self.font_size), 100, df.white)
                if device.audio.music_enabled:
                    self.message_display(self.music_enable_txt , "monospace", 20, (100, self.text_info_y), df.black)
                else:
                    self.message_display(self.music_disable_txt, "monospace", 20, (100, self.text_info_y), df.black)

                if pygame.mouse.get_pressed()[0]:
                    if device.audio.music_enabled:
                        device.audio.music_enabled = False
                        # btn.append(sp.Sprite2(self.disable_file, 500, 100, 50, 50, 0, 0))
                        btn.append(sp.Sprite2(self.disable_file, df.display_width * 0.7, 200, 50, 50, 0, 0))
                        print('adj:music disabled')

                    else:
                        device.audio.music_enabled = True
                        # btn.append(sp.Sprite2(self.enable_file, 500, 100, 50, 50, 0, 0))
                        btn.append(sp.Sprite2(self.enable_file, df.display_width * 0.7, 200, 50, 50, 0, 0))
                        print('adj:music enabled')

                    time.sleep(0.5)
                    device.audio.play_music()
            if btn[1].rect.collidepoint(pygame.mouse.get_pos()) == 1:
                self.draw_selected((0, self.text_info_y), (df.display_width, self.font_size), 100, df.white)
                if device.audio.sound_enabled:
                    self.message_display(self.sound_enable_txt, "monospace", 20, (100, self.text_info_y), df.black)
                else:
                    self.message_display(self.sound_disable_txt, "monospace", 20, (100, self.text_info_y), df.black)

                if pygame.mouse.get_pressed()[0]:
                    if device.audio.sound_enabled:
                        device.audio.sound_enabled = False
                        # btn.append(sp.Sprite2(self.disable_file, 500, 200, 50, 50, 0, 0))
                        btn.append(sp.Sprite2(self.disable_file, df.display_width * 0.7, 300, 50, 50, 0, 0))
                        print('adj:sound disabled')
                    else:
                        device.audio.sound_enabled = True
                        # btn.append(sp.Sprite2(self.enable_file, 500, 200, 50, 50, 0, 0))
                        btn.append(sp.Sprite2(self.enable_file, df.display_width * 0.7, 300, 50, 50, 0, 0))
                        print('adj:sound enabled')

                    time.sleep(0.5)
                    device.audio.play_music()

            self.message_display(self.opt_txt, "monospace", 40, (50, 100), df.black)
            self.message_display(self.music_txt, "monospace", 30, (50, 200), df.white)
            self.message_display(self.sound_txt, "monospace", 30, (50, 300), df.white)

            pygame.display.update()
            var.clock.tick(20)
