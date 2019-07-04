
import os
script_path = os.path.dirname(os.path.realpath( __file__ ))
print('wd',script_path)
os.chdir(script_path)
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
         self.menu_txt = "Info/Angabe/Info"
         self.cancel_text = "Exit/Ausgang/Salir"
         self.adj_txt = "Options/Wahl/Opciones"
         print('menu screen created')

    def run(self):
        mapsback = sp.Sprite2(self.backfile, 0, 0,df.display_width , df.display_height, 0, 0)
        btn = []

        genBtn = sp.Button(self.play_file, 150, 450)
        genBtn.hover_text = self.play_txt
        btn.append( genBtn)


        genBtn = sp.Button(self.menu_file, 300, 450 )
        genBtn.hover_text = self.menu_txt
        btn.append(genBtn)

        genBtn = sp.Button(self.adj_file, 450, 450)
        genBtn.hover_text = self.adj_txt
        btn.append(genBtn)

        genBtn = sp.Button(self.cancel_file, 600, 450)
        genBtn.hover_text = self.cancel_text
        btn.append(genBtn)

        while not self.stopEngine:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:                    
                    self.stopEngine = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.stopEngine = True

            var.gameDisplay.fill( df.white )
            self.draw_sprite2(mapsback)

            for m in btn:
                if m.onClick(pygame.mouse):
                    if re.search("play", m.file, flags=0):
                        mapsScreen = map.AddScreen()
                        mapsScreen.run()

                    if re.search("menu", m.file, flags=0):
                        imp.reload(adjustments)
                        infoScreen = info.AddScreen()
                        infoScreen.run()

                    if re.search("cancel", m.file, flags=0):
                        self.stopEngine = True
                        break

                    if re.search("adj", m.file, flags=0):
                        adjScreen = adjustments.AddScreen()
                        time.sleep(0.5)
                        adjScreen.run()

            pygame.display.update()
            var.clock.tick(var.fps)
