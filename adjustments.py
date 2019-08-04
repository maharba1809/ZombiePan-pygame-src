print('loading Adjustments')
import sprites as sp
import defaults as df
import pygame
import re
import time
import generic as gen
import var
import device
import buttons as btns

class AddScreen(gen.Xscreen):
    def __init__(self):
        gen.Xscreen.__init__(self)


        self.background_file = var.assetsDir + 'backgrounds/maps_table.jpg'

        self.enable_file = var.assetsDir + 'enabled.png'
        self.disable_file = var.assetsDir + 'disabled.png'

        self.buy_file = var.assetsDir + 'buy_yes.png'
        self.back_txt = "Return/ Zuruck/ Atras"
        self.music_enable_txt = "Enabled/ Aktiviert/ Activado"
        self.music_disable_txt = "Disabled/ Deaktiviert/ Desactivado"
        self.sound_disable_txt = "Disabled/ Deactiviert/ Desactivado"
        self.sound_enable_txt = "Enabled/ Deactiviert/ Desactivado"
        self.opt_txt = "Settings/ Auswahlen/ Configuracion"
        self.music_txt = "Music/ Musik/ Musica"
        self.sound_txt = "Sounds/ Klänge/ Sonidos"

        self.text_info_y = df.display_height*0.8
        self.header_position = (df.display_width * 0.1, 0)
        self.font1.path = "assets/fonts/horrendo.ttf"
        self.font1.font_size = 40
        self.font1.set_font()
        self.button_size = 50
        self.music_text_x = df.display_width * 0.1
        self.music_text_y = df.display_height * 0.2
        self.sound_text_x = df.display_width * 0.1
        self.sound_text_y = df.display_height * 0.3

        self.music_button_x = df.display_width * 0.7
        self.music_button_y = self.music_text_y
        self.music_button2_x = df.display_width * 0.8
        self.music_button2_y = self.music_text_y

        self.sound_button_x = df.display_width * 0.7
        self.sound_button_y = self.sound_text_y
        self.sound_button2_x = df.display_width * 0.8
        self.sound_button2_y = self.sound_text_y

        self.exit_button_x = df.display_width * 0.5 - 100 * 0.5
        self.exit_button_y = df.display_height * 0.8


    def run(self):
        mapsback = sp.Sprite2(self.background_file, 0, 0, df.display_width, df.display_height, 0, 0)
        btnEnableMusic = btns.Button(self.enable_file, self.music_button_x, self.music_button_y, self.button_size, self.button_size)
        btnDisableMusic = btns.Button(self.disable_file, self.music_button2_x, self.music_button2_y, self.button_size,self.button_size)
        btnEnableSound = btns.Button(self.enable_file, self.sound_button_x, self.sound_button_y, self.button_size,self.button_size)
        btnDisableSound = btns.Button(self.disable_file, self.sound_button2_x, self.sound_button2_y, self.button_size,self.button_size)
        exitBtn = btns.Button(self.buy_file, self.exit_button_x, self.exit_button_y, 100, 100)

        btnEnableMusic.shadow_h = 50
        btnDisableMusic.shadow_h = 50
        btnEnableSound.shadow_h = 50
        btnEnableSound.shadow_h = 50
        exitBtn.shadow_h = 50

        btnDisableMusic.hover_text = self.music_disable_txt
        btnEnableMusic.hover_text = self.music_enable_txt
        btnDisableSound.hover_text = self.sound_disable_txt
        btnEnableSound.hover_text = self.sound_enable_txt
        exitBtn.hover_text = self.back_txt

        while not self.stopEngine:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            var.gameDisplay.fill(df.white)
            self.draw_sprite2(mapsback)

            if exitBtn.onClick(pygame.mouse):
                self.stopEngine = True
                time.sleep(1)

            if btnDisableMusic.onClick(pygame.mouse):
                device.audio.music_enabled = False
                device.audio.play_music()
                time.sleep(1)

            if btnEnableMusic.onClick(pygame.mouse):
                device.audio.music_enabled = True
                device.audio.play_music()
                time.sleep(1)

            if btnDisableSound.onClick(pygame.mouse):
                device.audio.sound_enabled = False
                device.audio.play_music()
                time.sleep(1)

            if btnEnableSound.onClick(pygame.mouse):
                device.audio.sound_enabled = True
                device.audio.play_music()
                time.sleep(1)


            self.message_display(self.opt_txt,self.header_position )
            self.message_display(self.music_txt, (self.music_text_x, self.music_text_y))
            self.message_display(self.sound_txt,  (self.sound_text_x, self.sound_text_y))

            pygame.display.update()
            var.clock.tick(20)
