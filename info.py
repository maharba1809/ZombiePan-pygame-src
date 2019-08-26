print('Loading Info')
import sprites as sp
import defaults as df
import pygame
import re
import time
import generic as gen
import var
import device
import text as txg
import buttons as btns

class AddScreen(gen.Xscreen):
    def __init__(self):
        gen.Xscreen.__init__(self)
        self.version = df.version
        self.background_file = var.assetsDir + 'backgrounds/maps_table.jpg'
        self.buy_file = var.assetsDir + 'buy_yes.png'
        print('info screen created')
        # self.font = pygame.font.Font("assets/fonts/horrendo.ttf", 20)
        self.font1.font_size = 30
        self.font1.set_font()

    def run(self):

        mapsback = sp.Sprite2()
        mapsback.file = self.background_file
        mapsback.w = df.display_width
        mapsback.h = df.display_height
        mapsback.set_image()
        mapsback.rect.x = 0
        mapsback.rect.y = 0

        exitBtn = btns.Button(self.buy_file, df.display_width * 0.5 - 50, df.display_height * 0.8, 100, 100)

        while not self.stopEngine:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    device.audio.sound_bullet.play
                    pygame.quit()
                    quit()

            var.gameDisplay.fill(df.white)
            self.draw_sprite2(mapsback)

            if exitBtn.onClick(pygame.mouse):
                # if re.search("yes", exitBtn.file, flags=0):
                    self.stopEngine = True
                    time.sleep(1)


            yt = 10
            text = 'Zombie Pan beta'+ self.version
            self.font1.color = df.green
            self.message_display(text, (50, yt))

            yt += 60
            text = 'Independent Video Game created and designed by nordik14@gmail.com'
            self.font1.color = df.green
            self.message_display(text, (50, yt))

            yt += 60
            text = "Free distirbution of this product under GPL is allowed"
            self.font1.color = df.orange
            self.message_display(text, (50, yt))

            text = 'Free Assets obtained from GameArt2D:'
            self.font1.color = df.orange
            yt += 60
            self.message_display(text, (50, yt))

            yt += 60
            text = 'Zombie Pan available in Google Playstore!'
            self.font1.color = df.blue
            self.message_display(text, (50, yt))

            yt += 50
            text = 'Other products: Brick Infest, Vozarron, Ñulingua aprende español '
            self.font1.color = df.white
            self.message_display(text, (50, yt))

            yt += 50
            # draw_selected( (0, 380), (display_width,80), yt, black, gameDisplay )
            text = 'Support this video game for future updates'
            self.font1.color = df.violet
            self.message_display(text, (50, yt))

            yt += 70
            text = 'unterstütze dieses Videospiel für zukünftige Updates'
            self.font1.color = df.gold
            self.message_display(text, (50, yt))

            yt += 70
            text = 'Apoya este Juego con Donaciones '
            self.font1.color = df.red
            self.message_display(text, (50, yt))

            yt += 70
            self.draw_selected((0, yt), (df.display_width, 30), 40, df.red)
            self.font1.color = df.red
            text = 'Feedback, donations: nordik14@gmail.com'
            self.message_display(text, (50, yt))

            pygame.display.update()
            var.clock.tick(20)

