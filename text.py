
print('Loading text game')
import defaults as df
import var as var
import pygame as pyg

class TextGame():
    def __init__(self,):
        self.font_type = ""
        self.font_size = 20
        self.center = (0,0)
        self.path = "assets/fonts/horrendo.ttf"
        self.color =  df.white
        self.text = 'New text'

    def set_font(self):
        self.font = pyg.font.Font(self.path, self.font_size)

    def display_text(self, text):
        self.text = text
        label = self.font.render(self.text, 1, self.color)
        var.gameDisplay.blit(label, self.center)
