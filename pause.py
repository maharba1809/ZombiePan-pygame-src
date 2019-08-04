import sprites as sp
import pygame
import var
import random
import time
import defaults as df
import generic as gen
import re
import text as txg
import buttons as btns

class AddScreen(gen.Xscreen):
    def __init__(self):
        gen.Xscreen.__init__(self)
        self.stopPlay = False
        # self.font = pygame.font.Font("assets/fonts/horrendo.ttf", 40)
        self.background_file = var.assetsDir + 'backgrounds/maps_table.jpg'

        self.font1 = txg.TextGame()
        self.font1.font_size = 50
        self.font1.color = df.green

        # self.font1.path = "assets/fonts/OpenSans-Light.ttf"
        self.font1.set_font()
        self.button_size = 100

        self.button_play_path = var.assetsDir + "Button_play.png"
        self.button_play_x = df.display_width*0.4
        self.button_play_y = df.display_height*0.5 - self.button_size
        self.button_play_text = 'Play'
        self.play_text_pos = (self.button_play_x + self.button_size * 1.1, self.button_play_y*1.05)

        self.button_can_path = var.assetsDir + "Button_cancel.png"
        self.button_can_x = df.display_width*0.4
        self.button_can_y = self.button_play_y + self.button_size
        self.button_can_text = 'Cancel'
        self.can_text_pos = (self.button_can_x + self.button_size * 1.1, self.button_can_y*1.05)


        self.button_menu_path = var.assetsDir + "Buttonmenu.png"
        self.button_menu_x = df.display_width*0.4
        self.button_menu_y = self.button_can_y + self.button_size
        self.menu_text_pos = (self.button_menu_x + self.button_size * 1.1, self.button_menu_y*1.05)

        self.button_menu_text = 'Maps'
        self.header_pos =  df.display_width*0.1, 0


    def run(self):

        mapsback = sp.Sprite2(self.background_file, 0, 0, df.display_width, df.display_height, 0, 0)

        btnPlay = btns.Button(self.button_play_path, self.button_play_x, self.button_play_y, self.button_size, self.button_size)
        btnCan = btns.Button(self.button_can_path, self.button_can_x, self.button_can_y, self.button_size, self.button_size)
        btnMenu = btns.Button(self.button_menu_path, self.button_menu_x, self.button_menu_y, self.button_size, self.button_size)

        btnPlay.hover_text = self.button_play_text
        btnPlay.font_btn.color = df.green
        btnCan.hover_text = self.button_can_text
        btnCan.font_btn.color = df.red
        btnMenu.hover_text = self.button_menu_text
        btnMenu.font_btn.color = df.blue

        while not self.stopEngine:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.stopEgine = True

            var.gameDisplay.fill(df.black)
            self.draw_sprite2(mapsback)

            if btnPlay.onClick(pygame.mouse):
                self.stopEngine = True
                self.stopPlay = False
                time.sleep(1)

            if btnCan.onClick(pygame.mouse):
                pygame.quit()
                quit()

            if btnMenu.onClick(pygame.mouse):
                self.stopEngine = True
                self.stopPlay = True

            # self.draw_selected((0, btns[0].rect.y - btns[0].rect.h - 5), (df.display_width, 30), 100, df.white)
            self.message_display("Pause", self.header_pos)
            self.font1.color = df.green
            self.message_display(self.button_play_text, self.play_text_pos)
            self.font1.color = df.blue
            self.message_display(self.button_menu_text, self.menu_text_pos)
            self.font1.color = df.red
            self.message_display(self.button_can_text, self.can_text_pos)

            pygame.display.update()
            var.clock.tick(var.fps)
