import pygame
import var

print('Loading Sound and Video')

class AddWin():
    def _init_(self):
        pygame.init()
        pygame.display.set_caption('Zombie Pan 1.1.5')


class AddSound(AddWin):
    def __init__(self):
        AddWin._init_(self)
        pygame.mixer.pre_init(frequency=44100, size=-32, channels=2, buffer=4096)
        pygame.init()
        assetsDir = var.assetsDir

        self.sound_col = pygame.mixer.Sound(file = assetsDir + 'comical_liquid_gel_splat.ogg')
        self.sound_col.set_volume(0.5)
        self.sound_err = pygame.mixer.Sound(file = assetsDir + '327736__distillerystudio__error-03.ogg')
        self.sound_err.set_volume(0.5)
        self.sound_hel = pygame.mixer.Sound(file = assetsDir + 'helicopter.ogg')
        self.sound_hel.set_volume(0.2)
        self.sound_loser = pygame.mixer.Sound(file = assetsDir + '113988__kastenfrosch__verloren.ogg')
        self.sound_hel.set_volume(0.5)
        self.sound_winer = pygame.mixer.Sound(file = assetsDir + '270528littlerobotsoundfactoryjingle-win-00.ogg')
        self.sound_winer.set_volume(0.5)
        self.sound_bullet_file = assetsDir + 'single_water_drop.ogg'
        self.sound_bullet = pygame.mixer.Sound(file=self.sound_bullet_file)
        self.sound_bullet.set_volume(0.5)
        self.music_enabled = True
        self.sound_enabled = True
        self.music_theme = var.assetsDir + 'Little Swans Game.ogg'

        print('sound created')


    def play_music(self):

        if self.music_enabled:
            print('device:music enabled')
            if not pygame.mixer.music.get_busy():

                pygame.mixer.stop()
                pygame.mixer.music.load(self.music_theme)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.5)
            else:
                print('device:  music is busy')
        else:
            print('device:music disabled')
            pygame.mixer.music.pause()
            pygame.mixer.music.stop()

audio = AddSound()