import pygame
import var
import datetime
import defaults as df
import os
print('Loading Sound and Video')
version = '1.1.6'

class AddWin():
    def _init_(self):
        pygame.init()
        pygame.display.set_caption('Zombie Pan '+ version)


class AddSound(AddWin):
    def __init__(self):
        AddWin._init_(self)
        pygame.mixer.pre_init(frequency=44100, size=-32, channels=2, buffer=4096)
        pygame.init()
        assetsDir = var.assetsDir
        if not os.path.isfile(assetsDir + 'comical_liquid_gel_splat.ogg'):
            print('ERROR No Sound exist in ', assetsDir + 'comical_liquid_gel_splat.ogg')
        else:
            print('file exists')
        self.sound_col = pygame.mixer.Sound(file=assetsDir + 'comical_liquid_gel_splat.ogg')
        self.sound_col.set_volume(0.5)
        self.sound_err = pygame.mixer.Sound(file=assetsDir + '327736__distillerystudio__error-03.ogg')
        self.sound_err.set_volume(0.5)
        self.sound_hel = pygame.mixer.Sound(file=assetsDir + 'helicopter.ogg')
        self.sound_hel.set_volume(0.5)
        self.sound_loser = pygame.mixer.Sound(file=assetsDir + '113988__kastenfrosch__verloren.ogg')
        self.sound_hel.set_volume(0.5)
        self.sound_winer = pygame.mixer.Sound(file=assetsDir + '270528littlerobotsoundfactoryjingle-win-00.ogg')
        self.sound_winer.set_volume(0.5)
        self.sound_bullet_file = assetsDir + 'MP5 Firing-SoundBible.com-434501860.wav'
        self.sound_bullet = pygame.mixer.Sound(file=self.sound_bullet_file)
        self.sound_bullet.set_volume(0.5)
        self.music_enabled = True
        self.sound_enabled = True
        self.music_theme = var.assetsDir + ""
        self.sound_attack = pygame.mixer.Sound(file=assetsDir + 'Zombie Gets Attacked-SoundBible.com-20348330.wav')
        self.sound_glass_break = pygame.mixer.Sound(file=assetsDir + 'sounds/338692__natemarler__glass-break-small_short.wav')
        print('sound created')


    def play_music(self):

        if self.music_enabled:
            print('device:music enabled')
            if pygame.mixer.music.get_busy():
                pygame.mixer.stop()

            pygame.mixer.music.load(self.music_theme)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.5)

        else:
            print('device:music disabled')
            pygame.mixer.music.pause()
            pygame.mixer.music.stop()


class Ranking():
    def __init__(self):

        self.experience = 0
        self.respawn = 0
        self.killed = 0
        self.shelter = 100
        self.damage = 0
        self.level = 0
        self.life = 100
        self.damage = 0
        print('instance of Ranking')
        self.map_name = ''
        self.map = ''
        self.total = 0
        self.winner = False
        self.maps = []
        self.default_bullets_avaiable = 100
        self.bullet_available = self.default_bullets_avaiable
        self.dead_player = False


    def add_damage(self, damage_rate):

        self.damage += damage_rate
        self.life -= damage_rate
        # print('Damage', round(self.damage, 0), int(self.life))

    def add_kill(self):
        self.killed += 1
        self.experience += 1

    def new_level(self):
        self.killed = 0
        self.damage = 0
        if self.life <= 0:
            self.life = 100

    def end_level(self):
        if self.dead_player:
            print('End Level', round(self.damage, 1), int(self.life))
            self.dead_player = False #to start gaing as a alive player
            return True

        if self.killed == self.total:
            if datetime.datetime.now() - df.dead_time > datetime.timedelta(seconds=df.delay):
                return True
            return False

        return False

stats = Ranking()
audio = AddSound()
