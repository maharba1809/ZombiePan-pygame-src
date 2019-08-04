
import sprites as sp
import defaults as df
import pygame
import re
import time
import generic as gen
import var
import device
import final
import random
import pause
import imp
import datetime
import zombies as zmb
import text as txg


class AddScreen(gen.Xscreen):
    def __init__(self, map):
        gen.Xscreen.__init__(self)
        self.map = map
        device.audio.music_theme = var.assetsDir + 'sounds/Little Swans Game.ogg'
        device.audio.play_music()
        self.zombie_txt_pos = (0,0)
        self.exp_txt_pos = (df.display_width*0.2, 0)
        self.life_txt_pos = (df.display_width*0.3, 0)
        self.map_txt_pos = (df.display_width*0.5, 0)
        self.time_txt_pos = (df.display_width*0.6, 0)
        self.bullet_txt_pos = (df.display_width*0.8, 0)
        self.display_text_pos = (df.display_width * 0.5 - 100, df.display_height * 0.5 + 50)

        self.font1 = txg.TextGame()
        self.font1.font_size = 30
        self.font1.color = df.violet
        self.font1.set_font()

    def run(self):
        imp.reload(sp)
        imp.reload(final)
        imp.reload(zmb)

        print('\n')
        if device.audio.sound_enabled: device.audio.sound_hel.play()

        background = sp.Sprite2(self.map.filename, 0, 0, df.display_width, df.display_height, 0, 0)

        info_winer = sp.Sprite2(var.assetsDir + 'enabled.png', df.display_width * 0.5 - 40, df.display_height * 0.5 - 40, 80, 80, 0,
                                0)
        info_loser = sp.Sprite2(var.assetsDir + 'disabled.png', df.display_width * 0.5 - 40, df.display_height * 0.5 - 40, 80, 80, 0,
                                0)

        horde = zmb.Horde()
        horde.map_gap = self.map.gap
        horde.limit = self.map.total
        horde.update()
        device.stats.total = self.map.total

        hel = sp.Asprite()
        hel.load_images()

        weapon = sp.Weapon(hel.rect.x, hel.rect.y)
        weapon.bullet_available = device.stats.bullet_available
        bullets = []
        uinert = 0.5 * hel.u

        device.stats.new_level()
        total_time = 0

        home = sp.House()
        home.load_images()
        home.gap = self.map.gap
        home.set_position()

        while not self.stopEngine:
            time_start = pygame.time.get_ticks()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        hel.u = -5
                    if event.key == pygame.K_RIGHT:
                        hel.u = 6
                    if event.key == pygame.K_UP:
                        hel.v = -8*0.5
                    if event.key == pygame.K_DOWN:
                        hel.v = 9

                    if event.key == pygame.K_SPACE:
                        weapon.get_loc(hel)
                        weapon.shoot_bullet()


                    if event.key == pygame.K_ESCAPE:
                        pauseScreen = pause.AddScreen()
                        time.sleep(0.1)
                        time_pause = pygame.time.get_ticks()
                        pauseScreen.run()
                        dt_pause = pygame.time.get_ticks()  - time_pause
                        time_start += dt_pause
                        if pauseScreen.stopPlay:
                            self.stopEngine = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        hel.u = 0
                        hel.v = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        hel.u = 0
                        hel.v = 0

            var.gameDisplay.fill(df.black)
            self.draw_sprite2(background)

            # self.draw_sprite2(hel)
            hel.animate()  # callls animation defs
            # print('helicopter animate time:', pygame.time.get_ticks() - time_start)
            home.animate() #call home animation
            weapon.moveBullets()
            # print('move bullets time:', pygame.time.get_ticks() - time_start)

            horde.enemy_control(total_time)
            # print( home.rect.collidelist(horde.enemies))
            # print('rengine')

            for enemy in horde.enemies:

                if enemy.dead:
                    horde.enemies.remove(enemy)
                    continue

                enemy.animate()

                if enemy.rect.colliderect(home.rect):
                    enemy.preattack = True
                    enemy.running = False
                        # enemy.rect.x -=5
                    if device.stats.life <= 0:
                        break
                    if device.audio.sound_enabled:
                        device.audio.sound_glass_break.play()

                # Collision detection
                if len(weapon.magazine)>0:
                    for bullet in weapon.magazine:
                        if enemy.rect.colliderect(bullet.rect):

                            if device.audio.sound_enabled:
                                if not pygame.mixer.get_busy():
                                    device.audio.sound_col.play()

                            if enemy.alive:
                                enemy.descrease_life()
                                if not enemy.alive:
                                    device.stats.add_kill()
                                    df.dead_time = datetime.datetime.now()

                                weapon.magazine.remove(bullet)
            # print('Horde check time:',pygame.time.get_ticks() - time_start)
            if device.stats.end_level():
                self.stopEngine = True
                # self.draw_selected((0, df.display_height * 0.5 + 50), (df.display_width, 30), 100, df.white)
                if device.stats.damage !=0:
                    display_text = 'Damage:' + str(int(device.stats.damage))+ '% :('

                else:
                    display_text = 'Perfect!:)'
                self.message_display(display_text, self.display_text_pos)

                if device.stats.life > 0:
                    self.draw_sprite2(info_winer)
                    if device.audio.sound_enabled: device.audio.sound_winer.play()

                    # print(var.map_settings[2])
                    pygame.display.update()
                    time.sleep(2)
                    # if re.search("map14", var.map_settings[2], flags=0):
                    if device.stats.level == 14:
                        finalScreen = final.AddScreen()
                        finalScreen.run()

                    device.stats.winner = True
                    device.stats.bullet_available = weapon.bullet_available + 25

                else:
                    self.draw_sprite2(info_loser)
                    if device.audio.sound_enabled: device.audio.sound_loser.play()
                    pygame.display.update()
                    time.sleep(3)
                    device.stats.winner = False
                #check point
            # print('control time:', pygame.time.get_ticks() - time_start)
            self.sent_msg(weapon, total_time)
            pygame.display.update()
            # print('1',pygame.time.get_ticks() - time_start)
            dt = pygame.time.get_ticks() - time_start
            # print('end loop',total_time, dt, time_start, pygame.time.get_ticks())
            # print('loop time:', pygame.time.get_ticks() - time_start)
            total_time += dt

    def sent_msg(self, weapon,total_time):
        self.draw_selected((0, 0), (df.display_width, 40), 90, df.white)
        self.font1.color = df.green
        self.message_display('Zombies:' + str(device.stats.total - device.stats.killed),  self.zombie_txt_pos)
        self.font1.color = df.blue
        self.message_display('Exp:' + str(int(device.stats.experience)), self.exp_txt_pos)
        self.font1.color = df.white
        self.message_display('Life:' + str(int(device.stats.life)) + "%", self.life_txt_pos)
        self.font1.color = df.orange
        self.message_display('Map:' + str(device.stats.level),self.map_txt_pos)
        self.font1.color = df.gold
        self.message_display('Time:' + str(round(total_time, 1)), self.time_txt_pos)
        self.font1.color = df.black
        self.message_display('Bullets:' + str(weapon.bullet_available), self.bullet_txt_pos)
        self.font1.color = df.red



