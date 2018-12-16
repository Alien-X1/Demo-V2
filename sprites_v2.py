# sprite classes for game
# i used some ideas from CodePylet https://www.youtube.com/watch?v=osDofIdja6s&t=1038s
# i also borrowed pretty much all of this from kids can code - thanks!
# on acceleration https://www.khanacademy.org/science/physics/one-dimensional-motion/kinematic-formulas/v/average-velocity-for-constant-acceleration 
# on vectors: https://www.youtube.com/watch?v=ml4NSzCQobk 


import pygame as pg
from pygame.sprite import Sprite
from random import randint
from settings_v2 import *

vec = pg.math.Vector2

class Player(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = p_stand_mask
        self.rect = self.image.get_rect()
        self.rect.center = (x * PIX + PIX / 2, y * PIX)
        self.pos = (x * PIX + PIX / 2, y * PIX)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.collide_g = False
        self.max_jumps = 1
        self.max_vel = PLAYER_MAX_VEL
        self.jump_vel = PLAYER_JUMP_VEL
        self.jumps = 0
    # Init PLayer and give basic attributes

    def update(self):
        self.acc = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.vel.x > -self.max_vel:
            self.acc.x =  -ACCELERATION
        if keys[pg.K_RIGHT] and self.vel.x < self.max_vel:
            self.acc.x = ACCELERATION
        self.jump()
        self.gravity()
        self.friction()
        self.edge()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        if self.vel.x > 0 and self.collide_g == True:
            if self.image != p_walk_right_mask_1:
                self.image = p_walk_right_mask_1
            elif self.image != p_walk_right_mask_2:
                self.image = p_walk_right_mask_2
        if self.vel.x < 0 and self.collide_g == True:
            if self.image != p_walk_left_mask_1:
                self.image = p_walk_left_mask_1
            elif self.image != p_walk_left_mask_2:
                self.image = p_walk_left_mask_2
        print(self.pos)
    # Update Method to update position and running image
    
    def jump(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and (self.collide_g == True or self.jumps < self.max_jumps) and self.vel.y >= 0:
            self.jumps += 1
            self.vel.y -= self.jump_vel
            self.collide_g = False
            if self.vel.x > 0:
                self.image = p_jump_right_mask
            if self.vel.x < 0:
                self.image = p_jump_left_mask
    
        if self.collide_g == True :
            self.jumps = 0
            if self.vel.x == 0:
                self.image = p_stand_mask
    # Jump method

    def gravity(self):
        if self.collide_g == False and self.vel.y < 15:
            self.acc.y = GRAVITY
    # Gravity

    def collision(self):
        if self.pos.y >= HEIGHT - 20:
            self.collide = True
    # unused basic collision detection
    
    def edge(self):
        if self.pos[0] < 15:
            self.vel.x = 0
            self.pos.x = 15
        # elif self.pos.x > WIDTH + 15:
        #     self.pos.x = -15
    # Creates an impassible edge on the righthand side of the map
    
    def friction(self):
        keys = pg.key.get_pressed()
        if self.vel.x > 0 and not (keys[pg.K_LEFT] or keys[pg.K_RIGHT]):
            self.acc.x = -FRICTION

        elif self.vel.x < 0 and not (keys[pg.K_RIGHT] or keys[pg.K_LEFT]):
            self.acc.x = FRICTION
    # Friction to stop the player when the keys are released

class Baddie(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = b_masks[randint(0,1)]
        self.rect = self.image.get_rect()
        self.rect.center = (x * PIX + PIX / 2, y * PIX)
        self.pos = (x * PIX + PIX / 2, y * PIX)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.collide_g = False

    def update(self):
        self.gravity()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
    # Update method to update position on the map and also gravity
    
    def gravity(self):
        if self.collide_g == False and self.vel.y < 15:
            self.acc.y = GRAVITY
    # Gravity for the Baddies

class Immovable(Sprite):
    def __init__(self, x, y, i):
        Sprite.__init__(self)
        self.image = i
        self.rect = self.image.get_rect()
        self.rect.center = (x * PIX + PIX / 2, y * PIX)
        self.pos = (x * PIX + PIX / 2, y * PIX)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
    # Init method to apply basic attributes to the Immovable

    def update(self):
        self.acc = vec(0, 0)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midtop = self.pos
        # print(str(self.image)+" "+str(self.pos))
        # Update method to update position on the map

class Trap(Sprite):
    def __init__(self, x, y, i):
        Sprite.__init__(self)
        self.image = i
        self.rect = self.image.get_rect()
        self.rect.center = (x * PIX + PIX / 2, y * PIX)
        self.pos = (x * PIX + PIX / 2, y * PIX)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
    # Init method to apply basic attributes to the Trap

    def update(self):
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midtop = self.pos
    # Update method for moving the trap around the map

class Powerup(Sprite):
    def __init__(self, x, y, t):
        Sprite.__init__(self)
        self.image = pow_mask
        self.rect = self.image.get_rect()
        self.rect.center = (x * PIX + PIX / 2, y * PIX)
        self.pos = (x * PIX + PIX / 2, y * PIX)
        self.type = t
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
    # Init method to apply basic attributes to the Powerup

    def update(self):
        self.acc = vec(0, 0)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midtop = self.pos
        # Update method to update position on the map

class Hidden(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = h_mask
        self.rect = self.image.get_rect()
        self.rect.center = (x * PIX + PIX / 2, y * PIX)
        self.pos = (x * PIX + PIX / 2, y * PIX)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
    # Init method to apply basic attributes to the Hidden platform

    def update(self):
        self.acc = vec(0, 0)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midtop = self.pos
        # Update method to update position on the map

class Flag(Sprite):
    def __init__(self, x, y, i):
        Sprite.__init__(self)
        self.image = f_mask
        self.rect = self.image.get_rect()
        self.rect.center = (x * PIX + PIX / 2, y * PIX)
        self.pos = (x * PIX + PIX / 2, y * PIX)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.reality = i
    # Init method to apply basic attributes to the Flag

    def update(self):
        self.acc = vec(0, 0)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midtop = self.pos
        # Update method to update position on the map

class Flagpole(Sprite):
    def __init__(self, x, y, i):
        Sprite.__init__(self)
        self.image = pg.Surface((6,PIX))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x * PIX + 27, y * PIX)
        self.pos = (x * PIX + 27, y * PIX)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.reality = i
    # Init method to apply basic attributes to the Flagpole
        
    def update(self):
        self.acc = vec(0, 0)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midtop = self.pos
        # Update method to update position on the map