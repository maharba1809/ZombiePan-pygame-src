
import sprites as sp
import defaults as df
import pygame
import re
import time
import generic as gen
import var
import info
import adjustments
import map
import imp

print('Loading Menu')
class AddScreen(gen.Xscreen):
    def __init__(self):
         gen.Xscreen.__init__(self)
         self.backfile = var.assetsDir + 'main_back.jpg'
         self.play_file = var.assetsDir + 'play_red.png'
         self.menu_file = var.assetsDir + 'Buttonmenu.png'
         self.adj_file = var.assetsDir + 'Button_adj.png'
         self.cancel_file = var.assetsDir + 'Button_cancel.png'
         self.play_txt = "Play/Spielen/Jugar"
         self.menu_txt = "Info/Auskunft/Info"
         self.cancel_text = "Exit/Ausgang/Salir"
         self.adj_txt = "Options/Wahl/Opciones"
         print('menu screen created')

    def run(self):


        mapsback = sp.Sprite2(self.backfile, 0, 0,df.display_width , df.display_height, 0, 0)
        btn = []
        btn.append( sp.Sprite2(self.play_file, 150, 450, 70, 70, 0, 0))
        btn.append( sp.Sprite2(self.menu_file, 300, 450, 70, 70, 0, 0))
        btn.append( sp.Sprite2(self.adj_file, 450, 450, 70, 70, 0, 0))
        btn.append( sp.Sprite2(self.cancel_file, 600, 450, 70, 70, 0, 0))

        while not self.stopEngine:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.stopEngine = True

            var.gameDisplay.fill( df.white )
            # var.gameDisplay.blit(mapsback.surface, (mapsback.x, mapsback.y))
            self.draw_sprite2(mapsback)

            for m in btn:
                self.draw_sprite2(m)

                if (m.rect.collidepoint(pygame.mouse.get_pos()) == 1):
                    self.draw_selected( (0, 550), (df.display_width,40), 100, df.white )

                    if re.search("play", m.file, flags=0):
                        self.message_display( self.play_txt ,"monospace", 40, (150, 550), (255,69,0))
                    if re.search("menu", m.file, flags=0):
                        self.message_display( self.menu_txt ,"monospace", 40, (150, 550), (47,79,79))
                    if re.search("cancel", m.file, flags=0):
                        self.message_display( self.cancel_text ,"monospace", 40, (150, 550), (138,43,226))
                    if re.search("adj", m.file, flags=0):
                        self.message_display( self.adj_txt ,"monospace", 40, (150, 550), (255,0,0))

                    if pygame.mouse.get_pressed()[0]:

                        if re.search("play", m.file, flags=0):
                            mapsScreen = map.AddScreen()
                            # time.sleep(0.5)
                            mapsScreen.run()


                        if re.search("menu", m.file, flags=0):
                            imp.reload(adjustments)
                            infoScreen = info.AddScreen()
                            # time.sleep(0.5)
                            infoScreen.run()


                        if re.search("cancel", m.file, flags=0):
                            pygame.quit()
                            quit()

                        if re.search("adj", m.file, flags=0):
                            adjScreen = adjustments.AddScreen()
                            time.sleep(0.5)
                            adjScreen.run()



            pygame.display.update()
            var.clock.tick(20)
