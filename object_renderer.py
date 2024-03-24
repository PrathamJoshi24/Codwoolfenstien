import pygame as pg
from settings import *
import main


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        #if self.game.door == True:
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('resources/textures/sky.jpg', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        self.blood_screen = self.get_texture('resources/textures/blood_screen.png', RES)
        self.digit_size = 70
        self.digit_images = [self.get_texture(f'resources/textures/digits/{i}.png', [self.digit_size] * 2)
                             for i in range(11)]
        self.digits = dict(zip(map(str, range(11)), self.digit_images))
        self.game_over_image = self.get_texture('resources/textures/game_over.png', RES)
        self.win_image = self.get_texture('resources/textures/win.png', RES)

    def draw(self):
        self.draw_background()
        self.render_game_objects()
        self.draw_HUD()
        self.draw_player_health()

    def draw_HUD(self):
        self.screen.blit(self.get_texture("resources/hud/0.png", (RES)),(0,0))

    def win(self):
        self.screen.blit(self.win_image, (0, 0))

    def game_over(self):
        self.screen.blit(self.game_over_image, (0, 0))

    def draw_player_health(self):
        health = str(self.game.player.health)
        if int(health) >= 100:
          self.screen.blit(self.get_texture('FC0EVL1.png', (75,75)), (0,80))
        elif int(health) >=200 and int(health) > 100:
          self.screen.blit(self.get_texture('FC0EVL2.png', (75,75)), (0,80))
        elif int(health) >= 300 and int(health) > 200:
          self.screen.blit(self.get_texture('FC0EVL3.png', (75,75)), (0,80))
        elif int(health) >= 400 and int(health) > 300:
          self.screen.blit(self.get_texture('FC0EVL4.png', (75,75)), (0,80))
        elif int(health) <= 500:
          self.screen.blit(self.get_texture('FC0GOD0.png', (75,75)), (0, 80))
        for i, char in enumerate(health):
            self.screen.blit(self.digits[char], (i * self.digit_size, 0))
        self.screen.blit(self.digits['10'], ((i + 1) * self.digit_size, 0))
      
    def draw_level(self, siz):
      self.lel = open("levcodbyproppy.txt","r")
      self.d = self.lel.read()
      self.d = self.d.split(" ")
      self.d = (self.d[-1])
      for i, char in enumerate(self.d):
        self.screen.blit(self.digits[char], (i * self.digit_size,0))
        
    def player_damage(self):
        self.screen.blit(self.blood_screen, (0, 0))

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        # floor
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('resources/textures/1.jpg'),
            2: self.get_texture('resources/textures/2.jpg'),
            3: self.get_texture('resources/textures/3.jpg'),
            4: self.get_texture('resources/textures/4.jpg'),
            5: self.get_texture('resources/textures/5.jpg'),
            6: self.get_texture('resources/textures/6.jpg'),
            7: self.get_texture('resources/textures/7.jpg'),
            8: self.get_texture('resources/textures/8.jpg'),
            9: self.get_texture('resources/textures/9.jpg'),
            10: self.get_texture('resources/textures/10.jpg'),
            11: self.get_texture('resources/textures/11.jpg'),
            12: self.get_texture('resources/textures/12.jpg'),
            13: self.get_texture('resources/textures/13.jpg'),
            14: self.get_texture('resources/textures/14.jpg'),
            15: self.get_texture('resources/textures/15.jpg'),
            16: self.get_texture('resources/textures/16.jpg'),
            17: self.get_texture('resources/textures/17.jpg'),
            18: self.get_texture('resources/textures/18.jpg'),
            19: self.get_texture('resources/textures/19.jpg')
            #True: self.get_texture('resources/textures/19.jpg')
        }