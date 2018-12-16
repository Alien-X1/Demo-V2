# This file was made by Cal
import pygame as pg


TITLE = "Rage It"

# Frames Per Second
TICKS = 60

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

GREEN = (0,255,0)
YELLOW = (255,255,0)
RED = (255,0,0)
ORANGE = (255,155,0)
# REDDISH = (240,55,66)

L_BLUE = (0,179,233)
TEAL = (0,108,144)
NAVY = (0,14,76)
SEA = (0,173,136)

# Player same settings
PIX = 30
FRICTION = 1
ACCELERATION = 1
GRAVITY = 1
PLAYER_JUMP_VEL = 15
PLAYER_MAX_VEL = 4
PLAYER_MAX_JUMPS = 1

# MAP for level 1

KEY     = ['1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0']
LAYER1  = ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','e','a','a','a','a','a','a']
LAYER2  = ['a','r','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
LAYER3  = ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','e','a','a','a','a','a','a','a','a','a','a','a','a','a','a','e','a','a','a','a','a','a']
LAYER4  = ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
LAYER5  = ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','e','a','a','a','a','a','a','a','a','a','a','a','a','a','a','e','a','a','a','a','a','a']
LAYER6  = ['a','a','a','a','h','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
LAYER7  = ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','e','a','j','a','a','a','a','a','a','a','a','a','a','a','a','e','a','a','a','a','a','a']
LAYER8  = ['a','a','a','a','a','a','a','h','a','a','a','a','a','a','a','a','a','a','t','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
LAYER9  = ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','e','a','a','a','a','a','a']
LAYER10 = ['a','a','a','a','a','a','a','a','a','a','g','g','a','a','a','a','g','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
LAYER11 = ['a','a','a','a','a','a','a','a','a','a','s','s','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','e','a','a','a','a','a','a']
LAYER12 = ['p','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','f','a']
LAYER13 = ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','t','g','g','g','g','g','a','a','a','a','l','a']
LAYER14 = ['g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','g','t','t','t','g','t','t','t','t','t','t','t','t','u','s','s','s','s','s','g','g','g','g','g','g']
LAYER15 = ['s','s','a','a','a','s','s','s','s','s','s','s','s','s','s','s','u','u','u','s','u','u','u','u','u','u','u','u','u','s','s','s','s','s','s','s','s','s','s','s']
LAYER16 = ['s','s','a','h','a','s','s','s','s','s','s','s','s','s','s','s','u','u','u','s','u','u','u','u','u','s','u','u','u','s','s','s','s','s','s','s','s','s','s','s']
LAYER17 = ['s','s','a','a','a','s','s','s','s','s','s','s','s','s','s','s','u','u','u','s','u','u','u','u','u','s','u','u','u','s','s','s','s','s','s','s','s','s','s','s','a','a','a','a','a','a','a','a','a','a','a','a','a','c']
LAYER18 = ['s','s','a','a','a','s','s','s','s','s','s','s','s','s','s','s','u','u','u','s','u','u','u','u','u','s','u','u','u','s','s','s','s','s','s','s','s','s','s','s','a','a','a','a','a','a','a','a','a','a','a','a','a','b']
LAYER19 = ['s','s','a','a','a','s','s','s','s','s','s','s','s','s','s','s','u','u','u','s','u','u','u','u','u','s','u','u','u','s','s','s','s','s','s','s','s','s','s','s','a','a','a','a','h','a','a','a','h','a','a','a','h','h','h']
LAYER20 = ['s','s','a','a','a','s','s','s','s','s','s','s','s','s','s','s','u','u','u','s','u','u','u','u','u','s','u','u','u','s','s','s','s','s','s','s','s','s','s','s']
MAP = [LAYER1,LAYER2,LAYER3,LAYER4,LAYER5,LAYER6,LAYER7,LAYER8,LAYER9,LAYER10,LAYER11,LAYER12,LAYER13,LAYER14,LAYER15,LAYER16,LAYER17,LAYER18,LAYER19,LAYER20]

# Screen Dimensions
HEIGHT = PIX * len(MAP)
WIDTH = int(8/5 * HEIGHT)

# Masks
b1_mask = pg.image.load("Demo-V2\_v2_images\Baddie_block_1.png")
b2_mask = pg.image.load("Demo-V2\_v2_images\Baddie_block_2.png")
f_mask = pg.image.load("Demo-V2\_v2_images\Flag_block.png")
s_top_mask = pg.image.load("Demo-V2\_v2_images\Solid_block.png")
t_top_mask = pg.image.load("Demo-V2\_v2_images\Trap_block.png")
s_bot_mask = pg.image.load("Demo-V2\_v2_images\Solid_block_under.png")
t_bot_mask = pg.image.load("Demo-V2\_v2_images\Trap_block_under.png")
p_stand_mask = pg.image.load("Demo-V2\_v2_images\Player_block_1.png")
p_walk_right_mask_1 = pg.image.load("Demo-V2\_v2_images\Player_block_2.png")
p_walk_right_mask_2 = pg.image.load("Demo-V2\_v2_images\Player_block_2.png")
p_walk_left_mask_1 = pg.transform.flip(p_walk_right_mask_1,True,False)
p_walk_left_mask_2 = pg.transform.flip(p_walk_right_mask_2,True,False)
p_jump_right_mask = pg.image.load("Demo-V2\_v2_images\Player_block_4.png")
p_jump_left_mask = pg.transform.flip(p_jump_right_mask,True,False)
h_mask =  pg.image.load("Demo-V2\_v2_images\Hidden_block.png")
pow_mask =  pg.image.load("Demo-V2\_v2_images\Power_block.png")
b_masks = [b1_mask,b2_mask]
p_walk_right_masks = [p_walk_right_mask_1,p_walk_right_mask_2]
p_walk_left_masks = [p_walk_left_mask_1,p_walk_left_mask_2]
p_jump_masks = [p_jump_right_mask,p_jump_left_mask]
#importing all the images for use in the game