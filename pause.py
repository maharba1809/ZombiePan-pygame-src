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
import adjustments
import imp

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
        self.button_play_x = df.display_width*0.1
        self.button_play_y = df.display_height*0.3 - self.button_size
        self.button_play_text = 'Resume / Weitermachen / Continuar'
        self.play_text_pos = (self.button_play_x + self.button_size * 1.1, self.button_play_y*1.05)

        self.button_menu_path = var.assetsDir + "Buttonmenu.png"
        self.button_menu_x = df.display_width * 0.1
        self.button_menu_y = self.button_play_y + self.button_size
        self.menu_text_pos = (self.button_menu_x + self.button_size * 1.1, self.button_menu_y * 1.05)
        self.button_menu_text = 'Maps/ Maps / Mapas'
        self.header_pos = df.display_width * 0.1, 0

        self.adj_file = var.assetsDir + 'Button_adj.png'
        self.button_opt_x = df.display_width * 0.1
        self.button_opt_y = self.button_menu_y + self.button_size
        self.opt_text_pos = (self.button_opt_x + self.button_size * 1.1, self.button_opt_y * 1.05)
        self.button_opt_text = 'Options/ Option / Opciones'

        self.button_can_path = var.assetsDir + "Button_cancel.png"
        self.button_can_x = df.display_width*0.1
        self.button_can_y = self.button_opt_y + self.button_size
        self.button_can_text = 'Exit/ Ausgang / Salida'
        self.can_text_pos = (self.button_can_x + self.button_size * 1.1, self.button_can_y*1.05)

    def run(self):

        mapsback = sp.Sprite2()
        mapsback.file = self.background_file
        mapsback.w = df.display_width
        mapsback.h = df.display_height
        mapsback.set_image()
        mapsback.rect.x = 0
        mapsback.rect.y = 0

        btnPlay = btns.Button(self.button_play_path, self.button_play_x, self.button_play_y, self.button_size, self.button_size)
        btnCan = btns.Button(self.button_can_path, self.button_can_x, self.button_can_y, self.button_size, self.button_size)
        btnMenu = btns.Button(self.button_menu_path, self.button_menu_x, self.button_menu_y, self.button_size, self.button_size)
        btnSettings = btns.Button(self.adj_file, self.button_opt_x, self.button_opt_y,  self.button_size, self.button_size)
        btnSettings.hover_text = "Settings / Option/ Opciones"

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

            if btnMenu.onClick(pygame.mouse):
                self.stopEngine = True
                self.stopPlay = True

            if btnSettings.onClick(pygame.mouse):
                imp.reload(adjustments)
                adjScreen = adjustments.AddScreen()
                time.sleep(0.5)
                adjScreen.run()

            if btnCan.onClick(pygame.mouse):
                pygame.quit()
                quit()

            # self.draw_selected((0, btns[0].rect.y - btns[0].rect.h - 5), (df.display_width, 30), 100, df.white)
            self.message_display("Pause", self.header_pos)
            self.font1.color = df.green
            self.message_display(self.button_play_text, self.play_text_pos)
            self.font1.color = df.blue
            self.message_display(self.button_menu_text, self.menu_text_pos)
            self.font1.color = df.red
            self.message_display(self.button_can_text, self.can_text_pos)
            self.font1.color = df.violet
            self.message_display(self.button_opt_text, self.opt_text_pos)

            pygame.display.update()
            var.clock.tick(var.fps)
