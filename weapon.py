from sprite_object import *


class double_pistol(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/weapon/double_pistol/0.png', scale=2, animation_time=150):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.reloading = False
        self.num_images = len(self.images)
        self.shotsInGun = 2
        self.shot = 0
        self.frame_counter = 0
        self.damage = 100

    
    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[2]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0
                    self.shot = self.shot + 1
      
       #   self.animate_reload()
      #    self.shot = 0
          
    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
        self.check_animation_time()
        self.animate_shot()

class singlePistol(double_pistol):
  def __init__(self, game, path='resources/sprites/weapon/single_pistol/0.png', scale=1.5, animation_time=100):
    super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
    self.images = deque(
        [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
         for img in self.images])
    self.weapon_pos = (HALF_WIDTH - self.images[0].get_width()//6 , HEIGHT - self.images[0].get_height())
    self.reloading = False
    self.num_images = len(self.images)
    self.frame_counter = 0
    self.damage = 50

class ak_47(double_pistol):
  def __init__(self, game, path='resources/sprites/weapon/AK_47/0.png', scale=2, animation_time=50):
    super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
    self.images = deque(
      [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
       for img in self.images])
    self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 6, HEIGHT - self.images[0].get_height())
    self.reloading = False
    self.num_images = len(self.images)
    self.frame_counter = 0
    self.damage = 60

class revolver(double_pistol):
  def __init__(self, game, path='resources/sprites/weapon/REVOLVER/0.png', scale=2, animation_time=200):
    super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
    self.images = deque(
      [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
       for img in self.images])
    self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
    self.reloading = False
    self.num_images = len(self.images)
    self.frame_counter = 0
    self.damage = 100

class RIFLE(double_pistol):
  def __init__(self, game, path='resources/sprites/weapon/RIFLE/0.png', scale=2, animation_time=200):
    super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
    self.images = deque(
      [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
       for img in self.images])
    self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
    self.reloading = False
    self.num_images = len(self.images)
    self.frame_counter = 0
    self.damage = 150

class SHOTGUN(double_pistol):
  def __init__(self, game, path='resources/sprites/weapon/SHOTGUN/SHSSA0.png', scale=2, animation_time=200):
    super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
    self.images = deque(
      [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
       for img in self.images])
    self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
    self.reloading = False
    self.num_images = len(self.images)
    self.frame_counter = 0
    self.damage = 200

class SMG(double_pistol):
  def __init__(self, game, path='resources/sprites/weapon/SMG/0.png', scale=2, animation_time=200):
    super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
    self.images = deque(
      [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
       for img in self.images])
    self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
    self.reloading = False
    self.num_images = len(self.images)
    self.frame_counter = 0
    self.damage = 60

class SUPERSHOTGUN(double_pistol):
  def __init__(self, game, path='resources/sprites/weapon/SUPERSHOTGUN/0.png', scale=2, animation_time=200):
    super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
    self.images = deque(
      [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
       for img in self.images])
    self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
    self.reloading = False
    self.num_images = len(self.images)
    self.frame_counter = 0
    self.damage = 200

class MINIGUN(double_pistol):
  def __init__(self, game, path='resources/sprites/weapon/MINIGUN/CHAEA0.png', scale=2, animation_time=50):
    super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
    self.images = deque(
      [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
       for img in self.images])
    self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
    self.reloading = False
    self.num_images = len(self.images)
    self.frame_counter = 0
    self.damage = 50

class MACHINEGUN(double_pistol):
  def __init__(self, game, path='MACHINEGUN/MGN1A0.png', scale=2, animation_time=100):
    super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
    self.images = deque(
      [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
       for img in self.images])
    self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
    self.reloading = False
    self.num_images = len(self.images)
    self.frame_counter = 0
    self.damage = 50
