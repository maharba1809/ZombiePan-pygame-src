
import pygame
import var
import device
print('Loading Xscreen')

class Xscreen():
    def __init__(self):


        self.stopEngine = False

        print('generic screen created')
        device.audio.play_music()

    def draw_sprite2(self, sprite):
        var.gameDisplay.blit(sprite.image, (sprite.rect.x, sprite.rect.y))


    def message_display(self, text, typefont, size, center, color):
        myfont = pygame.font.SysFont(typefont, size)
        label = myfont.render(text, 1, color)
        var.gameDisplay.blit(label, center)


    def draw_selected(self, pos, dim, alpha, color):
        s = pygame.Surface(dim)
        s.set_alpha(alpha)
        s.fill(color)
        var.gameDisplay.blit(s, pos)

    def run(self):
        while not self.stopEngine:
            print('running empty engine')
            self.stopEngine = True

