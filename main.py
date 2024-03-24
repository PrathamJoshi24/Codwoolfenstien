
import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *


class Game:
    def __init__(self):
        pg.init()
        #self.weap = [double_pistol(self)]
        pg.mouse.set_visible(False)
        self.new_start = False
        self.screen = pg.display.set_mode(RES,pg.SCALED|pg.FULLSCREEN)
        pg.event.set_grab(True)
        self.clock = pg.time.Clock()
        self.wep = [singlePistol,double_pistol,MINIGUN,revolver,ak_47]
        self.delta_time =1
        self.global_trigger = False
        self.lev = 0
        self.levell = 1
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.new_game()
        self.mapV = False
        self.countwep = -1
      
        
    def level(self):
      
        self.file = open("levcodbyproppy.txt", "r+")
        self.lev = self.file.read()
        
        if not self.new_start:
          self.lev = self.lev.split(" ")
          self.lev = int(self.lev[-1])
          self.new_start = False
        else:
          self.lev = 0
          

        self.lev += 1
        self.file.write(f" {self.lev}")
        self.file.close()
        self.levell = self.lev
        return self.lev
        
    def new_game(self):
        
          
        self.levell = self.lev
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = double_pistol(self)
        #self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        #pg.mixer.music.play(-1)
        #self.le = self.level()
        

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        if self.mapV:
            self.screen.fill('black')
            self.map.draw()
            self.player.draw()
            self.object_renderer.draw_level(26)
        else:
            self.object_renderer.draw()
            self.weapon.draw()
        

    def check_events(self):
          kc = pg.key.get_pressed()
          if kc[pg.K_BACKSLASH]:
            self.new_start = True
            self.new_game()
            
          if kc[pg.K_UP]:
            if self.countwep < (len(self.wep)-1):
              self.countwep +=1
            else:
              self.countwep = 0
              
            self.weapon = self.wep[self.countwep](self)

          elif kc[pg.K_DOWN]:
            self.countwep -=1
            self.weapon = self.wep[self.countwep](self)
          
          if kc[pg.K_m]:
            self.mapV = not self.mapV
          
     
          self.global_trigger = False
          for event in pg.event.get():
              if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                  pg.quit()
                  sys.exit()
              elif event.type == self.global_event:
                  self.global_trigger = True
              self.player.single_fire_event(event)
  
    def run(self):
        while True:
            #v.cutscene1(self.screen)
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()