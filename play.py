
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




class AddScreen(gen.Xscreen):
    def __init__(self, map):
        gen.Xscreen.__init__(self)
        self.map = map

    def run(self):
        imp.reload(sp)
        imp.reload(final)

        print('\n')
        if device.audio.sound_enabled: device.audio.sound_hel.play()

        background = sp.Sprite2(self.map.filename, 0, 0, df.display_width, df.display_height, 0, 0)

        info_winer = sp.Sprite2(var.assetsDir + 'enabled.png', df.display_width * 0.5 - 40, df.display_height * 0.5 - 40, 80, 80, 0,
                                0)
        info_loser = sp.Sprite2(var.assetsDir + 'disabled.png', df.display_width * 0.5 - 40, df.display_height * 0.5 - 40, 80, 80, 0,
                                0)

        horde = sp.Horde()
        horde.map_gap = self.map.gap
        horde.limit = self.map.total
        horde.update()
        device.stats.total = self.map.total
        # horde.new_enemy()
        hel = sp.Asprite()
        hel.load_images()
        weapon = sp.Weapon(hel.rect.x, hel.rect.y)
        weapon.bullet_available = device.stats.bullet_available
        bullets = []
        uinert = 0.5 * hel.u

        device.stats.new_level()
        total_time = 0

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
                        hel.u = 5

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
                    if event.key == pygame.K_LEFT and event.key == pygame.K_RIGHT:
                        hel.u = 0

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and event.key == pygame.K_RIGHT:
                        hel.u = 0

            var.gameDisplay.fill(df.black)
            self.draw_sprite2(background)

            weapon.moveBullets()
            # self.draw_sprite2(hel)
            hel.animate()  # callls animation defs

            # if hel.rect.x>0.5*df.display_width:
            horde.enemy_control(total_time)


            for enemy in horde.enemies:
                enemy.animate()
                if enemy.destroy() and enemy.alive:
                    device.stats.add_damage()
                    if device.stats.life <= 0:
                        break

                # Collision detection
                if len(weapon.magazine)>0:
                    for bullet in weapon.magazine:
                        # print(bullet)
                        if enemy.rect.colliderect(bullet.rect):
                            if enemy.alive:
                                if device.audio.sound_enabled: device.audio.sound_col.play()
                                device.stats.add_kill()
                                enemy.alive = False  # changes statsus
                                weapon.magazine.remove(bullet)
                                df.dead_time = datetime.datetime.now()

            # control
            # killed = 10000
            # print(damage,'damage')
            if  device.stats.end_level():
                self.stopEngine = True
                self.draw_selected((0, df.display_height * 0.5 + 50), (df.display_width, 30), 100, df.white)
                if device.stats.damage !=0:
                    display_text = 'Damage:' + str(int(device.stats.damage*100))+ '% :('

                else:
                    display_text = 'Perfect!:)'
                self.message_display(display_text, "monospace", 30,
                                (df.display_width * 0.5 - 100, df.display_height * 0.5 + 50), df.violet)

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
                    device.stats.bullet_available = weapon.bullet_available + 10

                else:
                    self.draw_sprite2(info_loser)
                    if device.audio.sound_enabled: device.audio.sound_loser.play()
                    pygame.display.update()
                    time.sleep(4)
                    device.stats.winner = False
                #check point


            var.clock.tick(var.fps)
            dt = pygame.time.get_ticks() - time_start
            # print(total_time,dt,time_start, pygame.time.get_ticks())

            total_time += dt


            self.draw_selected((0, 0), (df.display_width, 20), 50, df.white)
            self.message_display('Enemies:' + str(device.stats.total - device.stats.killed), "monospace", 20, (0, 0), df.orange)
            self.message_display('Exp:' + str(int(device.stats.experience)), "monospace", 20, (150, 0), df.violet)
            self.message_display('Life:' + str(int(device.stats.life)) + "%", "monospace", 20, (250, 0), df.orange)
            self.message_display('Map:' + str(device.stats.level), "monospace", 20, (400, 0), df.orange)
            self.message_display('Time:' + str(round(total_time,1)), "monospace", 20, (500, 0), df.red)
            self.message_display('Bullets:' + str(weapon.bullet_available), "monospace", 20, (650,  0), df.violet)

            pygame.display.update()



