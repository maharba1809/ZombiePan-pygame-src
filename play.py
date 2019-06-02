
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



class AddScreen(gen.Xscreen):
    def __init__(self):
        gen.Xscreen.__init__(self)

    def run(self):
        imp.reload(sp)

        if device.audio.sound_enabled: device.audio.sound_hel.play()

        background = sp.Sprite2(var.map_settings[2], 0, 0, df.display_width, df.display_height, 0, 0)
        var.map_gap = var.map_settings[1]

        info_winer = sp.Sprite2(var.assetsDir + 'enabled.png', df.display_width * 0.5 - 40, df.display_height * 0.5 - 40, 80, 80, 0,
                                0)
        info_loser = sp.Sprite2(var.assetsDir + 'disabled.png', df.display_width * 0.5 - 40, df.display_height * 0.5 - 40, 80, 80, 0,
                                0)

        horde = sp.Horde()
        horde.new_horde()
        hel = sp.Asprite()
        hel.load_images()
        weapon = sp.Weapon(hel.rect.x, hel.rect.y)

        experience = 0
        respawn = 0
        killed = 0
        shelter = 100
        bullets = []
        uinert = 0.5 * hel.u
        damage = 0
        while not self.stopEngine:
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
                        pauseScreen.run()

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

            for enemy in horde.enemies:
                enemy.animate()
                if enemy.lived:
                    damage += enemy.damage/50000

                # Collision detection
                if len(weapon.magazine)>0:
                    for bullet in weapon.magazine:
                        # print(bullet)
                        if enemy.rect.colliderect(bullet.rect):
                            if enemy.lived:
                                if device.audio.sound_enabled: device.audio.sound_col.play()
                                killed += 1
                                experience += 1
                                enemy.lived = False  # changes status
                                # enemy.col = True  # collision flag
                                # enemy.index = 0  # restarts frame
                                print('killed:', killed)
                                weapon.magazine.remove(bullet)
                                # horde.enemies.remove(enemy)
                            #del bullet1


            # control
            # killed = 10000
            # print(damage,'damage')
            if killed >= var.total or damage>1:
                self.stopEngine = True
                self.draw_selected((0, df.display_height * 0.5 + 50), (df.display_width, 30), 100, df.white)
                self.message_display('Target:' + str(int(shelter)) + "%", "monospace", 30,
                                (df.display_width * 0.5 - 100, df.display_height * 0.5 + 50), df.violet)

                if damage < 1:
                    self.draw_sprite2(info_winer)
                    if device.audio.sound_enabled: device.audio.sound_winer.play()

                    # print(var.map_settings[2])
                    pygame.display.update()
                    time.sleep(4)
                    if re.search("map14", var.map_settings[2], flags=0):
                        finalScreen = final.AddScreen()
                        finalScreen.run()
                else:
                    self.draw_sprite2(info_loser)
                    if device.audio.sound_enabled: device.audio.sound_loser.play()
                    pygame.display.update()
                    time.sleep(4)


            self.draw_selected((0, 0), (df.display_width, 20), 100, df.white)
            self.message_display('Enemies:' + str(var.total - killed), "monospace", 20, (0, 0), df.orange)
            self.message_display('Exp:' + str(experience), "monospace", 20, (200, 0), df.violet)
            self.message_display('Shelter:' + str(int(shelter)) + "%", "monospace", 20, (400, 0), df.red)

            pygame.display.update()
            var.clock.tick(50)
