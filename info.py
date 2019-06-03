
import sprites as sp
import defaults as df
import pygame
import re
import time
import generic as gen
import var
import device

print('Loading Info')

class AddScreen(gen.Xscreen):
    def __init__(self):
        gen.Xscreen.__init__(self)
        self.background_file = var.assetsDir + 'maps_board.jpg'
        self.buy_file = var.assetsDir + 'buy_yes.png'
        print('info screen created')

    def run(self):


        mapsback = sp.Sprite2(self.background_file, 0, 0, df.display_width, df.display_height, 0, 0)
        btn = []
        btn.append(sp.Sprite2(self.buy_file, 100, 450, 90, 90, 0, 0))

        while not self.stopEngine:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    device.audio.sound_bullet.play
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

                    if re.search("yes", m.file, flags=0):
                        self.draw_selected((0, 550), (df.display_width, 20), 100, df.white)
                        self.message_display("Done/Geschafft/Hecho", "monospace", 20, (100, 550), (255, 69, 0))

                    var.gameDisplay.blit(s, (m.rect.x, m.rect.y))

                    if pygame.mouse.get_pressed()[0]:
                        if re.search("yes", m.file, flags=0):
                            self.stopEngine = True
                            time.sleep(1)
            yt = 10
            text = 'Zombie Pan beta 1.1.5 '
            self.message_display(text, "monospace", 30, (50, yt), df.gray)
            yt += 40
            text = 'Independent Video Game created and designed by nordik14@gmail.com'
            self.message_display(text, "monospace", 20, (50, yt), df.gray)
            yt += 20
            text = "Free distirbution of this product under GPL is allowed"
            self.message_display(text, "monospace", 20, (50, yt), df.gray)
            text = 'Free Assets obtained from GameArt2D:'
            yt += 20
            self.message_display(text, "monospace", 20, (50, yt), df.blue)
            text = 'Free distibution'
            yt += 20
            self.message_display(text, "monospace", 20, (50, yt), df.blue)
            text = 'Licenced distribution '
            yt += 20
            self.message_display(text, "monospace", 20, (50, yt), df.blue)
            yt += 20
            text = 'Original design'
            self.message_display(text, "monospace", 20, (50, yt), df.blue)
            yt += 20
            text = 'Zombie Pan available in Google Playstore!'
            self.message_display(text, "monospace", 20, (50, yt), df.green)
            yt += 20
            text = 'Other products: Brick Infest, Vozarron, Ñulingua aprende español '
            self.message_display(text, "monospace", 15, (50, yt), df.green)
            yt += 20
            # draw_selected( (0, 380), (display_width,80), yt, black, gameDisplay )
            text = 'Support this video game for future updates'
            self.message_display(text, "monospace", 25, (50, yt), df.red)
            yt += 50
            text = 'unterstütze dieses Videospiel für zukünftige Updates'
            self.message_display(text, "monospace", 25, (50, yt), df.red)
            yt += 50
            text = 'Apoya este Juego con Donaciones '
            self.message_display(text, "monospace", 25, (50, yt), df.red)
            yt += 50
            self.draw_selected((0, yt), (df.display_width, 20), 100, df.gold)
            text = 'Feedback, donations: nordik14@gmail.com'
            self.message_display(text, "monospace", 20, (50, yt), df.black)

            pygame.display.update()
            var.clock.tick(20)

