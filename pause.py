import sprites as sp
import pygame
import var
import random
import time
import defaults as df
import generic as gen
import re



class AddScreen(gen.Xscreen):
    def __init__(self):
        gen.Xscreen.__init__(self)
        self.stopPlay = False


    def run(self):


        mapsback = sp.Sprite2(var.assetsDir + 'maps_board.jpg', 0, 0, df.display_width, df.display_height, 0, 0)
        btns = []
        btns.append(
            sp.Sprite2(var.assetsDir + "Button_play.png", df.display_width * 0.5 - 100, df.display_height * 0.5 - 100, 80, 80,
                       0, 0))
        btns.append(
            sp.Sprite2(var.assetsDir + "Buttonmenu.png", btns[0].rect.x, btns[0].rect.y + btns[0].rect.h + 10, 80, 80,
                       0, 0))
        btns.append(
            sp.Sprite2(var.assetsDir + "Button_cancel.png", btns[1].rect.x, btns[1].rect.y + btns[1].rect.h + 10, 80,
                       80, 0, 0))

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
            for m in btns:
                self.draw_sprite2(m)

                if (m.rect.collidepoint(pygame.mouse.get_pos()) == 1):

                    self.draw_selected((m.rect.x + m.rect.w + 10, m.rect.y + m.rect.h * 0.5 - 10), (df.display_width, 30),
                                  100, df.white)
                    if re.search("play", m.file, flags=0):
                        self.message_display("Play", "monospace", 30,
                                        (m.rect.x + m.rect.w + 10, m.rect.y + m.rect.h * 0.5 - 10), df.black)
                    if re.search("menu", m.file, flags=0):
                        self.message_display("Maps", "monospace", 30,
                                        (m.rect.x + m.rect.w + 10, m.rect.y + m.rect.h * 0.5 - 10), df.black)
                    if re.search("cancel", m.file, flags=0):
                        self.message_display("Exit Game", "monospace", 30,
                                        (m.rect.x + m.rect.w + 10, m.rect.y + m.rect.h * 0.5 - 10), df.black)

                    if pygame.mouse.get_pressed()[0]:
                        if re.search("play", m.file, flags=0):
                            self.stopEngine = True
                            self.stopPlay = False
                        if re.search("menu", m.file, flags=0):
                            self.stopEngine = True
                            self.stopPlay = True
                        if re.search("cancel", m.file, flags=0):
                            pygame.quit()
                            quit()
            self.draw_selected((0, btns[0].rect.y - btns[0].rect.h - 5), (df.display_width, 30), 100, df.white)
            self.message_display("Pause", "monospace", 30, (btns[0].rect.x, btns[0].rect.y - btns[0].rect.h - 5), df.gold)

            pygame.display.update()
