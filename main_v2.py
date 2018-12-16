# This file was created by Cal
''' Sources:
KidsCanCode  Chris Bradfield
    jumpy and shmup
Robert Chien
Mikey and Harrison
Mr.Cozort
'''


'''
=========================Gameplay=========================
Hidden blocks to access otherwise out of game areas
Trapped blocks to drop and kill you unexpectedly
Powerups that give effects (random or otherwise)
=========================Cosmetic=========================
===========================Bugs===========================
======================Gameplay_Fixes======================
======================Cool Stuff=======================
=====================Missing_Junk======================
'''


import pygame as pg
import random
from settings_v2 import *
from sprites_v2 import *
from time import sleep

class Game:
    def __init__ (self):
        # init game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.playing = True
        self.alive = True
        self.start = False
        self.layer = 0
        self.placement = 0
    # init pygame and create window

    def new(self):
        # Groups
        self.players = pg.sprite.Group()
        self.immovables = pg.sprite.Group()
        self.traps = pg.sprite.Group()
        self.used_traps = pg.sprite.Group()
        self.hiddens = pg.sprite.Group()
        self.baddies = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.flags = pg.sprite.Group()
        self.mapping()
    # Runs the mapping method to create the entire "level" or Map

    def run(self):
        while self.playing:
            self.new()
            while self.alive:
                self.clock.tick(TICKS)
                self.events()
                self.update()
                self.draw()
                self.collision()
                self.scrolling()
                self.death()
            self.reset()
    # Game loop, Runs while playing, resets the world once you die

    def reset(self):
        for i in self.hiddens:
            self.hiddens.remove(i)
        for i in self.players:
            self.players.remove(i)
        for i in self.immovables:
            self.immovables.remove(i)
        for i in self.traps:
            self.traps.remove(i)
        for i in self.used_traps:
            self.used_traps.remove(i)
        for i in self.baddies:
            self.baddies.remove(i)
        for i in self.powerups:
            self.powerups.remove(i)
        for i in self.flags:
            self.flags.remove(i)
        self.alive = True
    # Rests the map and sets life to true so the game restarts
        
    def update(self):
        self.hiddens.update()
        self.players.update()
        self.immovables.update()
        self.traps.update()
        self.used_traps.update()
        self.flags.update()
        self.baddies.update()
        self.powerups.update()
    # updates sprites

    def mapping(self):
        sl = self.layer
        sp = self.placement
        for i in MAP:
            sl += 1
            sp = 0
            for r in i:
                if r == "a":
                    pass
                elif r == "g":
                    self.s = Immovable(sp,sl,s_top_mask)
                    self.immovables.add(self.s)
                elif r == "s":
                    self.s = Immovable(sp,sl,s_bot_mask)
                    self.immovables.add(self.s)
                elif r == "j":
                    self.j = Powerup(sp,sl,1)
                    self.powerups.add(self.j)
                elif r == "r":
                    self.r = Powerup(sp,sl,randint(0,3))
                    self.powerups.add(self.r)
                elif r == "t":
                    self.t = Trap(sp,sl,t_top_mask)
                    self.traps.add(self.t)
                elif r == "u":
                    self.t = Trap(sp,sl,t_bot_mask)
                    self.traps.add(self.t)
                elif r == "h":
                    self.h = Hidden(sp,sl)
                    self.hiddens.add(self.h)
                elif r == "e":
                    self.b = Baddie(sp,sl)
                    self.baddies.add(self.b)
                elif r == "p":
                    self.gamer = Player(sp,sl)
                    self.players.add(self.gamer)
                elif r == "f":
                    self.f = Flag(sp,sl,"fake")
                    self.flags.add(self.f)
                elif r == "l":
                    self.l = Flagpole(sp,sl,"fake")
                    self.flags.add(self.l)
                elif r == "c":
                    self.f = Flag(sp,sl,"real")
                    self.flags.add(self.f)
                elif r == "b":
                    self.l = Flagpole(sp,sl,"real")
                    self.flags.add(self.l)
                sp += 1
        # Inserts the different blocks into the game based on their location in the layer and their letter
        # sp is self.pos.x and sl is self.pos.y

    def collision(self):
        block_hit_g = pg.sprite.spritecollideany(self.gamer, self.immovables, False)
        block_hit_t = pg.sprite.spritecollideany(self.gamer, self.traps, False)
        block_hit_h = pg.sprite.spritecollideany(self.gamer, self.hiddens, False)
        if block_hit_g:
            print(block_hit_g)
            if self.gamer.rect.bottom < block_hit_g.rect.top + 29:     
                self.gamer.pos.y = block_hit_g.rect.top + 1
                self.gamer.vel.y = 0
                self.gamer.collide_g = True
            elif self.gamer.rect.top > block_hit_g.rect.bottom - 29:
                self.gamer.vel.y = 0
                self.gamer.collide_g = False
                self.gamer.jumps = self.gamer.max_jumps
        # Ground collision

        if block_hit_t:
            print(block_hit_t)
            if self.gamer.rect.bottom < block_hit_t.rect.top + 29:
                self.used_traps.add(block_hit_t)
                block_hit_t.acc.y = GRAVITY
                self.traps.remove(block_hit_t)
                self.gamer.pos.y = block_hit_t.rect.top - 1
                self.gamer.vel.y = 0
                self.gamer.collide_g = False
            elif self.gamer.rect.top > block_hit_t.rect.bottom - 29:
                self.gamer.vel.y = 0
                self.gamer.collide_g = False
                self.gamer.jumps = self.gamer.max_jumps
        # Trap collision

        if block_hit_h:
            print(block_hit_h)
            if self.gamer.rect.bottom < block_hit_h.rect.top + 29:     
                self.gamer.pos.y = block_hit_h.rect.top + 1
                self.gamer.vel.y = 0
                self.gamer.collide_g = True
            # elif self.gamer.rect.top > block_hit_h.rect.bottom - 29 and not block_hit_h.color == RED:
            #     self.hiddens.remove(block_hit_h)
            #     block_hit_h.color = RED
            #     print(block_hit_h.color)
            #     self.hiddens.add(block_hit_h)
        # Hidden Collision
                
        elif not block_hit_g or block_hit_t or block_hit_h:
            self.gamer.collide_g = False
    # Collision detection for the player with specified blocks so that the player does not just float randomly
        
        for i in self.baddies:
            b_hits_g = pg.sprite.spritecollide(i, self.immovables, False)
            b_hits_t = pg.sprite.spritecollide(i, self.traps, False)
            i.vel.x = 0
            if b_hits_g:
                i.pos.y = b_hits_g[0].rect.top + 1
                i.vel.y = 0
                i.collide_g = True
                i.vel.x = -5
            if b_hits_t:
                i.pos.y = b_hits_t[0].rect.top + 1
                i.vel.y = 0
                i.collide_g = True
                i.vel.x = -5
            elif not b_hits_g or b_hits_t:
                i.collide_g = False
        # Collision for baddies so that they don't just fall through the world
    # sprite collision

    def scrolling(self):
        if self.gamer.pos.x >= WIDTH / 2 and self.gamer.vel.x > 0:
            for i in self.immovables:
                i.vel.x = -self.gamer.vel.x
            for i in self.traps:
                i.vel.x = -self.gamer.vel.x
            for i in self.used_traps:
                i.vel.x = -self.gamer.vel.x
            for i in self.hiddens:
                i.vel.x = -self.gamer.vel.x
            for i in self.powerups:
                i.vel.x = -self.gamer.vel.x
            for i in self.flags:
                i.vel.x = -self.gamer.vel.x
            for i in self.baddies:
                i.vel.x = -self.gamer.vel.x - 5
            self.gamer.pos.x = WIDTH / 2
        elif self.gamer.pos.x < WIDTH / 2:
            for i in self.immovables:
                i.vel.x = 0
            for i in self.traps:
                i.vel.x = 0
            for i in self.used_traps:
                i.vel.x = 0
            for i in self.hiddens:
                i.vel.x = 0
            for i in self.powerups:
                i.vel.x = 0
            for i in self.flags:
                i.vel.x = 0
        # Map scrolling

    def death(self):
        player_deathblow = pg.sprite.spritecollideany(self.gamer, self.baddies, False)
        player_item_collect = pg.sprite.spritecollideany(self.gamer, self.powerups, False)
        player_flag_collect = pg.sprite.spritecollideany(self.gamer, self.flags, False)
        if player_deathblow:
            print(player_deathblow)
            self.alive = False
        if self.gamer.pos.y > HEIGHT + 60:
            self.alive = False
        if player_item_collect:
            self.powerups.remove(player_item_collect)
            if player_item_collect.type == 0:
                self.alive = False
            elif player_item_collect.type == 1:
                self.gamer.max_jumps += 1
            elif player_item_collect.type == 2:
                self.gamer.max_vel += 10
            elif player_item_collect.type == 3:
                self.gamer.max_vel = PLAYER_MAX_VEL
                self.gamer.max_jumps = PLAYER_MAX_JUMPS
            # removes the powerups and applies the abilities absed on the powerup number
        if player_flag_collect:
            if player_flag_collect.reality == "real":
                self.playing = False
                self.alive = False
                self.running = False
            # real Flag instantly ends the game
            elif player_flag_collect.reality == "fake":
                self.alive = False
            # fake Flag kills player without ending game
        for i in self.baddies:
            if i.pos.y > HEIGHT:
                self.baddies.remove(i)
        # Removes enemies that drop below the height
        for i in self.used_traps:
            if i.pos.y > HEIGHT:
                self.used_traps.remove(i)
        # removes traps that drop below height
        # Player, Enemy, and Powerup removal. also works for endgame

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                    self.alive = False
                    self.running = False
        # listening for events (specifically quitting)

    def draw(self):
        # self.screen.fill(RED)
        self.screen.fill(BLACK)
        self.hiddens.draw(self.screen)
        self.players.draw(self.screen)
        self.traps.draw(self.screen)
        self.used_traps.draw(self.screen)
        self.immovables.draw(self.screen)
        self.baddies.draw(self.screen)
        self.powerups.draw(self.screen)
        self.flags.draw(self.screen)
        # double buffer
        pg.display.flip()
        # screen creation
    
    def show_start_screen(self):
        keys = pg.key.get_pressed()
        self.screen.fill(RED)
        while self.start == False:
            if keys[pg.K_SPACE]:
                self.running = True
                self.start = True
            else:
                pass
    # self explanitory

    # def show_go_screen(self):
    #     self.screen.fill(BLACK)

        # show game over screen
        # pass
    # init sound mixer

g=Game()

# g.show_start_screen()
while g.running:
    g.run()
    # g.show_go_screen
pg.quit()
# Runs the game...