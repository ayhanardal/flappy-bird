import pygame
from sys import exit
from random import randint

fps = 30
game_mode = 0 # | 0- Opening | 1- Game | 2- Pause | 3- Game after pause
width = 600
height = 600
w_2 = 300
h_2 = 300
number_blank = 25
blank_x_base = 140
blank_y_base = 530
blank_h_x_base = 500
blank_h_y_base = 530
high_score = 0
obstaclex = width + 50
obstacley = 490
gravity = 0
start_time = 0
patetes = 0
animation_time = 0
previous_position = 0

pygame.init()
display = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('background/bg.png').convert_alpha()
bg_rect = bg_surface.get_rect(topleft = (0,0))
bg_rect_2 = bg_surface.get_rect(topleft = (width,0))

font = pygame.font.Font('font/Pixeltype.ttf',50)
score = font.render('Score : ',False,(10,10,10))
score_rect = score.get_rect(left =10,centery=550)

high_score_t = font.render('High Score : ', False,(10,10,10))
high_score_rect = high_score_t.get_rect(right = 500, centery= 550)


grd_surface = pygame.image.load('background/grd.png').convert_alpha()
grd_rect = grd_surface.get_rect(bottomleft = (0,height))
grd_rect_2 = grd_surface.get_rect(bottomleft = (width,height))

title = pygame.image.load('ui/title.png').convert_alpha()
title_rect = title.get_rect(centerx = w_2,centery = h_2 - 200)

start_msg = pygame.image.load('ui/start-message.png').convert_alpha()
start_msg_rect = start_msg.get_rect(centerx =w_2, centery= h_2 + 40)

start_bird = pygame.image.load('ui/start-bird.png').convert_alpha()
start_bird_rect = start_bird.get_rect(centerx = w_2, centery = h_2 - 60)

player0 = pygame.image.load('bird/yellowbird-downflap.png').convert_alpha()
player1 = pygame.image.load('bird/yellowbird-midflap.png').convert_alpha()
player2 = pygame.image.load('bird/yellowbird-upflap.png').convert_alpha()
player_anim = [player0,player1,player2]
player = player_anim[1]
player_rect = player1.get_rect(centerx = w_2, centery = h_2 - 60)

obstacle = pygame.image.load('obstacle\pipe-green.png').convert_alpha()
obstacle_rect = obstacle.get_rect(bottomleft = (obstaclex,obstacley))

obstacle_t = pygame.image.load('obstacle\pipe-green-t.png').convert_alpha()
obstacle_rect_t = obstacle_t.get_rect(bottomleft = (obstaclex,obstacley - 420))

obstacle_y_list = [70 , 120, 190, 230, 270, 319]

scoreboard = pygame.image.load('ui/scoreboard.png').convert_alpha()
scoreboard = pygame.transform.scale(scoreboard, size = (345, 171)) 
scoreboard_rect = scoreboard.get_rect(centerx =w_2,centery=height)

start_button = pygame.image.load('ui/start-button.png').convert_alpha()
start_button2 = pygame.image.load('ui/start-button2.png').convert_alpha()
start_button = pygame.transform.scale2x(start_button)
start_button2 = pygame.transform.scale2x(start_button2)
start_button_rect = start_button.get_rect(centerx =w_2, top=height + 100)

space_icon = pygame.image.load('ui/space1.png').convert_alpha()
space_icon = pygame.transform.scale(space_icon, size = (175,75))
space_icon_rect = space_icon.get_rect(centerx =w_2, top=h_2 + 40)

space2_icon = pygame.image.load('ui/space2.png').convert_alpha()
space2_icon = pygame.transform.scale(space2_icon, size = (175,75))
space2_icon_rect = space2_icon.get_rect(centerx =w_2, top=h_2 + 40)

space_anim = [space_icon,space2_icon]

_0 = pygame.image.load('number_symbols/0.png').convert_alpha()
_1 = pygame.image.load('number_symbols/1.png').convert_alpha()
_2 = pygame.image.load('number_symbols/2.png').convert_alpha()
_3 = pygame.image.load('number_symbols/3.png').convert_alpha()
_4 = pygame.image.load('number_symbols/4.png').convert_alpha()
_5 = pygame.image.load('number_symbols/5.png').convert_alpha()
_6 = pygame.image.load('number_symbols/6.png').convert_alpha()
_7 = pygame.image.load('number_symbols/7.png').convert_alpha()
_8 = pygame.image.load('number_symbols/8.png').convert_alpha()
_9 = pygame.image.load('number_symbols/9.png').convert_alpha()

_0r = _0.get_rect(topleft=(blank_x_base,blank_y_base))
_1r = _1.get_rect(topleft=(blank_x_base,blank_y_base))
_2r = _2.get_rect(topleft=(blank_x_base,blank_y_base))
_3r = _3.get_rect(topleft=(blank_x_base,blank_y_base))
_4r = _4.get_rect(topleft=(blank_x_base,blank_y_base))
_5r = _5.get_rect(topleft=(blank_x_base,blank_y_base))
_6r = _6.get_rect(topleft=(blank_x_base,blank_y_base))
_7r = _7.get_rect(topleft=(blank_x_base,blank_y_base))
_8r = _8.get_rect(topleft=(blank_x_base,blank_y_base))
_9r = _9.get_rect(topleft=(blank_x_base,blank_y_base))

_0r1 = _0.get_rect(topleft=(blank_x_base + number_blank,blank_y_base))
_1r1 = _1.get_rect(topleft=(blank_x_base + number_blank,blank_y_base))
_2r1 = _2.get_rect(topleft=(blank_x_base + number_blank,blank_y_base))
_3r1 = _3.get_rect(topleft=(blank_x_base + number_blank,blank_y_base))
_4r1 = _4.get_rect(topleft=(blank_x_base + number_blank,blank_y_base))
_5r1 = _5.get_rect(topleft=(blank_x_base + number_blank,blank_y_base))
_6r1 = _6.get_rect(topleft=(blank_x_base + number_blank,blank_y_base))
_7r1 = _7.get_rect(topleft=(blank_x_base + number_blank,blank_y_base))
_8r1 = _8.get_rect(topleft=(blank_x_base + number_blank,blank_y_base))
_9r1 = _9.get_rect(topleft=(blank_x_base + number_blank,blank_y_base))

_0r2 = _0.get_rect(topleft=(blank_x_base + (number_blank * 2),blank_y_base))
_1r2 = _1.get_rect(topleft=(blank_x_base + (number_blank * 2),blank_y_base))
_2r2 = _2.get_rect(topleft=(blank_x_base + (number_blank * 2),blank_y_base))
_3r2 = _3.get_rect(topleft=(blank_x_base + (number_blank * 2),blank_y_base))
_4r2 = _4.get_rect(topleft=(blank_x_base + (number_blank * 2),blank_y_base))
_5r2 = _5.get_rect(topleft=(blank_x_base + (number_blank * 2),blank_y_base))
_6r2 = _6.get_rect(topleft=(blank_x_base + (number_blank * 2),blank_y_base))
_7r2 = _7.get_rect(topleft=(blank_x_base + (number_blank * 2),blank_y_base))
_8r2 = _8.get_rect(topleft=(blank_x_base + (number_blank * 2),blank_y_base))
_9r2 = _9.get_rect(topleft=(blank_x_base + (number_blank * 2),blank_y_base))

_0r3 = _0.get_rect(topleft=(blank_x_base + (number_blank * 3),blank_y_base))
_1r3 = _1.get_rect(topleft=(blank_x_base + (number_blank * 3),blank_y_base))
_2r3 = _2.get_rect(topleft=(blank_x_base + (number_blank * 3),blank_y_base))
_3r3 = _3.get_rect(topleft=(blank_x_base + (number_blank * 3),blank_y_base))
_4r3 = _4.get_rect(topleft=(blank_x_base + (number_blank * 3),blank_y_base))
_5r3 = _5.get_rect(topleft=(blank_x_base + (number_blank * 3),blank_y_base))
_6r3 = _6.get_rect(topleft=(blank_x_base + (number_blank * 3),blank_y_base))
_7r3 = _7.get_rect(topleft=(blank_x_base + (number_blank * 3),blank_y_base))
_8r3 = _8.get_rect(topleft=(blank_x_base + (number_blank * 3),blank_y_base))
_9r3 = _9.get_rect(topleft=(blank_x_base + (number_blank * 3),blank_y_base))

_0rh = _0.get_rect(topleft=(blank_h_x_base,blank_h_y_base))
_1rh = _1.get_rect(topleft=(blank_h_x_base,blank_h_y_base))
_2rh = _2.get_rect(topleft=(blank_h_x_base,blank_h_y_base))
_3rh = _3.get_rect(topleft=(blank_h_x_base,blank_h_y_base))
_4rh = _4.get_rect(topleft=(blank_h_x_base,blank_h_y_base))
_5rh = _5.get_rect(topleft=(blank_h_x_base,blank_h_y_base))
_6rh = _6.get_rect(topleft=(blank_h_x_base,blank_h_y_base))
_7rh = _7.get_rect(topleft=(blank_h_x_base,blank_h_y_base))
_8rh = _8.get_rect(topleft=(blank_h_x_base,blank_h_y_base))
_9rh = _9.get_rect(topleft=(blank_h_x_base,blank_h_y_base))

_0r1h = _0.get_rect(topleft=(blank_h_x_base + number_blank,blank_h_y_base))
_1r1h = _1.get_rect(topleft=(blank_h_x_base + number_blank,blank_h_y_base))
_2r1h = _2.get_rect(topleft=(blank_h_x_base + number_blank,blank_h_y_base))
_3r1h = _3.get_rect(topleft=(blank_h_x_base + number_blank,blank_h_y_base))
_4r1h = _4.get_rect(topleft=(blank_h_x_base + number_blank,blank_h_y_base))
_5r1h = _5.get_rect(topleft=(blank_h_x_base + number_blank,blank_h_y_base))
_6r1h = _6.get_rect(topleft=(blank_h_x_base + number_blank,blank_h_y_base))
_7r1h = _7.get_rect(topleft=(blank_h_x_base + number_blank,blank_h_y_base))
_8r1h = _8.get_rect(topleft=(blank_h_x_base + number_blank,blank_h_y_base))
_9r1h = _9.get_rect(topleft=(blank_h_x_base + number_blank,blank_h_y_base))

_0r2h = _0.get_rect(topleft=(blank_h_x_base + (number_blank * 2),blank_h_y_base))
_1r2h = _1.get_rect(topleft=(blank_h_x_base + (number_blank * 2),blank_h_y_base))
_2r2h = _2.get_rect(topleft=(blank_h_x_base + (number_blank * 2),blank_h_y_base))
_3r2h = _3.get_rect(topleft=(blank_h_x_base + (number_blank * 2),blank_h_y_base))
_4r2h = _4.get_rect(topleft=(blank_h_x_base + (number_blank * 2),blank_h_y_base))
_5r2h = _5.get_rect(topleft=(blank_h_x_base + (number_blank * 2),blank_h_y_base))
_6r2h = _6.get_rect(topleft=(blank_h_x_base + (number_blank * 2),blank_h_y_base))
_7r2h = _7.get_rect(topleft=(blank_h_x_base + (number_blank * 2),blank_h_y_base))
_8r2h = _8.get_rect(topleft=(blank_h_x_base + (number_blank * 2),blank_h_y_base))
_9r2h = _9.get_rect(topleft=(blank_h_x_base + (number_blank * 2),blank_h_y_base))

_0r3h = _0.get_rect(topleft=(blank_h_x_base + (number_blank * 3),blank_h_y_base))
_1r3h = _1.get_rect(topleft=(blank_h_x_base + (number_blank * 3),blank_h_y_base))
_2r3h = _2.get_rect(topleft=(blank_h_x_base + (number_blank * 3),blank_h_y_base))
_3r3h = _3.get_rect(topleft=(blank_h_x_base + (number_blank * 3),blank_h_y_base))
_4r3h = _4.get_rect(topleft=(blank_h_x_base + (number_blank * 3),blank_h_y_base))
_5r3h = _5.get_rect(topleft=(blank_h_x_base + (number_blank * 3),blank_h_y_base))
_6r3h = _6.get_rect(topleft=(blank_h_x_base + (number_blank * 3),blank_h_y_base))
_7r3h = _7.get_rect(topleft=(blank_h_x_base + (number_blank * 3),blank_h_y_base))
_8r3h = _8.get_rect(topleft=(blank_h_x_base + (number_blank * 3),blank_h_y_base))
_9r3h = _9.get_rect(topleft=(blank_h_x_base + (number_blank * 3),blank_h_y_base))

numbers = [_0,_1,_2,_3,_4,_5,_6,_7,_8,_9]

blank0 = [_0r,_1r,_2r,_3r,_4r,_5r,_6r,_7r,_8r,_9r]
blank1 = [_0r1,_1r1,_2r1,_3r1,_4r1,_5r1,_6r1,_7r1,_8r1,_9r1]
blank2 = [_0r2,_1r2,_2r2,_3r2,_4r2,_5r2,_6r2,_7r2,_8r2,_9r2]
blank3 = [_0r3,_1r3,_2r3,_3r3,_4r3,_5r3,_6r3,_7r3,_8r3,_9r3]

blank0_h = [_0rh,_1rh,_2rh,_3rh,_4rh,_5rh,_6rh,_7rh,_8rh,_9rh]
blank1_h = [_0r1h,_1r1h,_2r1h,_3r1h,_4r1h,_5r1h,_6r1h,_7r1h,_8r1h,_9r1h]
blank2_h = [_0r2h,_1r2h,_2r2h,_3r2h,_4r2h,_5r2h,_6r2h,_7r2h,_8r2h,_9r2h]
blank3_h = [_0r3h,_1r3h,_2r3h,_3r3h,_4r3h,_5r3h,_6r3h,_7r3h,_8r3h,_9r3h]

def display_score():

    global numbers, blank0, blank1, blank2, blank3, start_time
    
    current_time = int(pygame.time.get_ticks() / 1000) - start_time

    current_time_str = str(current_time)

    current_blank = []

    for number in current_time_str:
        current_blank.append(number)
    
    if len(current_blank) >= 1:
        if current_blank[0] == '0':
            display.blit(numbers[0],blank0[0])
        elif current_blank[0] == '1':
            display.blit(numbers[1],blank0[1])
        elif current_blank[0] == '2':
            display.blit(numbers[2],blank0[2])
        elif current_blank[0] == '3':
            display.blit(numbers[3],blank0[3])
        elif current_blank[0] == '4':
            display.blit(numbers[4],blank0[4])
        elif current_blank[0] == '5':
            display.blit(numbers[5],blank0[5])
        elif current_blank[0] == '6':
            display.blit(numbers[6],blank0[6])
        elif current_blank[0] == '7':
            display.blit(numbers[7],blank0[7])
        elif current_blank[0] == '8':
            display.blit(numbers[8],blank0[8])
        elif current_blank[0] == '9':
            display.blit(numbers[9],blank0[9])
        
    if len(current_blank) >= 2:
        if current_blank[1] == '0':
            display.blit(numbers[0],blank1[0])
        elif current_blank[1] == '1':
            display.blit(numbers[1],blank1[1])
        elif current_blank[1] == '2':
            display.blit(numbers[2],blank1[2])
        elif current_blank[1] == '3':
            display.blit(numbers[3],blank1[3])
        elif current_blank[1] == '4':
            display.blit(numbers[4],blank1[4])
        elif current_blank[1] == '5':
            display.blit(numbers[5],blank1[5])
        elif current_blank[1] == '6':
            display.blit(numbers[6],blank1[6])
        elif current_blank[1] == '7':
            display.blit(numbers[7],blank1[7])
        elif current_blank[1] == '8':
            display.blit(numbers[8],blank1[8])
        elif current_blank[1] == '9':
            display.blit(numbers[9],blank1[9])

    if len(current_blank) >= 3:
        if current_blank[2] == '0':
            display.blit(numbers[0],blank2[0])
        elif current_blank[2] == '1':
            display.blit(numbers[1],blank2[1])
        elif current_blank[2] == '2':
            display.blit(numbers[2],blank2[2])
        elif current_blank[2] == '3':
            display.blit(numbers[3],blank2[3])
        elif current_blank[2] == '4':
            display.blit(numbers[4],blank2[4])
        elif current_blank[2] == '5':
            display.blit(numbers[5],blank2[5])
        elif current_blank[2] == '6':
            display.blit(numbers[6],blank2[6])
        elif current_blank[2] == '7':
            display.blit(numbers[7],blank2[7])
        elif current_blank[2] == '8':
            display.blit(numbers[8],blank2[8])
        elif current_blank[2] == '9':
            display.blit(numbers[9],blank2[9])

    if len(current_blank) == 4:
        if current_blank[3] == '0':
            display.blit(numbers[0],blank3[0])
        elif current_blank[3] == '1':
            display.blit(numbers[1],blank3[1])
        elif current_blank[3] == '2':
            display.blit(numbers[2],blank3[2])
        elif current_blank[3] == '3':
            display.blit(numbers[3],blank3[3])
        elif current_blank[3] == '4':
            display.blit(numbers[4],blank3[4])
        elif current_blank[3] == '5':
            display.blit(numbers[5],blank3[5])
        elif current_blank[3] == '6':
            display.blit(numbers[6],blank3[6])
        elif current_blank[3] == '7':
            display.blit(numbers[7],blank3[7])
        elif current_blank[3] == '8':
            display.blit(numbers[8],blank3[8])
        elif current_blank[3] == '9':
            display.blit(numbers[9],blank3[9])

    current_blank = []

    return current_time

def display_high_score():

    global high_score, numbers, blank0_h, blank1_h, blank2_h, blank3_h

    if display_score() > high_score:
        high_score = display_score()
    
    high_score_str = str(high_score)

    current_h_blank = []

    for number in high_score_str:
        current_h_blank.append(number)

    if len(current_h_blank) >= 1:
        if current_h_blank[0] == '0':
            display.blit(numbers[0],blank0_h[0])
        elif current_h_blank[0] == '1':
            display.blit(numbers[1],blank0_h[1])
        elif current_h_blank[0] == '2':
            display.blit(numbers[2],blank0_h[2])
        elif current_h_blank[0] == '3':
            display.blit(numbers[3],blank0_h[3])
        elif current_h_blank[0] == '4':
            display.blit(numbers[4],blank0_h[4])
        elif current_h_blank[0] == '5':
            display.blit(numbers[5],blank0_h[5])
        elif current_h_blank[0] == '6':
            display.blit(numbers[6],blank0_h[6])
        elif current_h_blank[0] == '7':
            display.blit(numbers[7],blank0_h[7])
        elif current_h_blank[0] == '8':
            display.blit(numbers[8],blank0_h[8])
        elif current_h_blank[0] == '9':
            display.blit(numbers[9],blank0_h[9])
        
    if len(current_h_blank) >= 2:
        if current_h_blank[1] == '0':
            display.blit(numbers[0],blank1_h[0])
        elif current_h_blank[1] == '1':
            display.blit(numbers[1],blank1_h[1])
        elif current_h_blank[1] == '2':
            display.blit(numbers[2],blank1_h[2])
        elif current_h_blank[1] == '3':
            display.blit(numbers[3],blank1_h[3])
        elif current_h_blank[1] == '4':
            display.blit(numbers[4],blank1_h[4])
        elif current_h_blank[1] == '5':
            display.blit(numbers[5],blank1_h[5])
        elif current_h_blank[1] == '6':
            display.blit(numbers[6],blank1_h[6])
        elif current_h_blank[1] == '7':
            display.blit(numbers[7],blank1_h[7])
        elif current_h_blank[1] == '8':
            display.blit(numbers[8],blank1_h[8])
        elif current_h_blank[1] == '9':
            display.blit(numbers[9],blank1_h[9])

    if len(current_h_blank) >= 3:
        if current_h_blank[2] == '0':
            display.blit(numbers[0],blank2_h[0])
        elif current_h_blank[2] == '1':
            display.blit(numbers[1],blank2_h[1])
        elif current_h_blank[2] == '2':
            display.blit(numbers[2],blank2_h[2])
        elif current_h_blank[2] == '3':
            display.blit(numbers[3],blank2_h[3])
        elif current_h_blank[2] == '4':
            display.blit(numbers[4],blank2_h[4])
        elif current_h_blank[2] == '5':
            display.blit(numbers[5],blank2_h[5])
        elif current_h_blank[2] == '6':
            display.blit(numbers[6],blank2_h[6])
        elif current_h_blank[2] == '7':
            display.blit(numbers[7],blank2_h[7])
        elif current_h_blank[2] == '8':
            display.blit(numbers[8],blank2_h[8])
        elif current_h_blank[2] == '9':
            display.blit(numbers[9],blank2_h[9])

    if len(current_h_blank) == 4:
        if current_h_blank[3] == '0':
            display.blit(numbers[0],blank3_h[0])
        elif current_h_blank[3] == '1':
            display.blit(numbers[1],blank3_h[1])
        elif current_h_blank[3] == '2':
            display.blit(numbers[2],blank3_h[2])
        elif current_h_blank[3] == '3':
            display.blit(numbers[3],blank3_h[3])
        elif current_h_blank[3] == '4':
            display.blit(numbers[4],blank3_h[4])
        elif current_h_blank[3] == '5':
            display.blit(numbers[5],blank3_h[5])
        elif current_h_blank[3] == '6':
            display.blit(numbers[6],blank3_h[6])
        elif current_h_blank[3] == '7':
            display.blit(numbers[7],blank3_h[7])
        elif current_h_blank[3] == '8':
            display.blit(numbers[8],blank3_h[8])
        elif current_h_blank[3] == '9':
            display.blit(numbers[9],blank3_h[9])

    current_h_blank = []

    return int(high_score)

def display_reset():

    global gravity, width, height, w_2, h_2, obstaclex, obstacley

    obstacle_rect_t.x = obstaclex
    obstacle_rect.x = obstaclex
    bg_rect.x = 0
    bg_rect_2.x = width
    grd_rect.x = 0
    grd_rect_2.x = width
    title_rect.centerx = w_2
    title_rect.centery = h_2 - 200

    player_rect.centerx = w_2
    player_rect.centery = h_2

    gravity = 0

def display_scores():

    global score, score_rect, high_score_t, high_score_rect

    display.blit(score,score_rect)
    display_score()
    display.blit(high_score_t,high_score_rect)
    display_high_score()

def display_environment():
    
    global animation_time, previous_position, player

    if game_mode == 0:
        display.blit(bg_surface,bg_rect)
        display.blit(obstacle,obstacle_rect)
        display.blit(obstacle_t,obstacle_rect_t)
        display.blit(grd_surface,grd_rect)
        display.blit(title,title_rect)
        display.blit(start_bird,start_bird_rect)
        animation_time += 1
        
        if animation_time % fps >= fps / 2:
            display.blit(space_anim[0],space_icon_rect)
        else:
            display.blit(space_anim[1],space2_icon_rect)

    elif game_mode == 1:
        display.blit(bg_surface,bg_rect)
        display.blit(bg_surface,bg_rect_2)
        display.blit(obstacle,obstacle_rect)
        display.blit(obstacle_t,obstacle_rect_t)
        display.blit(grd_surface,grd_rect)
        display.blit(grd_surface,grd_rect_2)
    

        if previous_position > player_rect.y:
            player = player_anim[0]
        elif previous_position < player_rect.y:
            player = player_anim[2]
        else:
            player = player_anim[1]

        previous_position = player_rect.y

        display.blit(player,player_rect)

        if title_rect.centery > -100:
            display.blit(title,title_rect)
        if start_msg_rect.centery < 700:    
            display.blit(start_msg,start_msg_rect)

    elif game_mode == 2:
        display.blit(bg_surface,bg_rect)
        display.blit(bg_surface,bg_rect_2)
        display.blit(obstacle,obstacle_rect)
        display.blit(obstacle_t,obstacle_rect_t)
        display.blit(grd_surface,grd_rect)
        display.blit(grd_surface,grd_rect_2)
        display.blit(player,player_rect)

        display.blit(scoreboard,scoreboard_rect)
        display.blit(sb_score,sb_score_rect)
        display.blit(sb_h_score,sb_h_score_rect)

        mouse_pos = pygame.mouse.get_pos()

        if start_button_rect.collidepoint(mouse_pos):
            display.blit(start_button2,start_button_rect)
        else:
            display.blit(start_button,start_button_rect)
    
    elif game_mode == 3:
        display.blit(bg_surface,bg_rect)
        display.blit(obstacle,obstacle_rect)
        display.blit(obstacle_t,obstacle_rect_t)
        display.blit(grd_surface,grd_rect)
        display.blit(title,title_rect)
        display.blit(start_bird,start_bird_rect)
        
        animation_time += 1
        
        if animation_time % fps >= fps / 2:
            display.blit(space_anim[0],space_icon_rect)
        else:
            display.blit(space_anim[1],space2_icon_rect)

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print('\n','Cikis yapildi (x)','\n')
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                print('\n','Cikis yapildi (esc)','\n')
                pygame.quit()
                exit()

            if event.key == pygame.K_SPACE and game_mode == 1:
                gravity = -10

            if event.key == pygame.K_SPACE and (game_mode == 0 or game_mode == 3):
                start_time = int(pygame.time.get_ticks() / 1000)
                gravity = -10
                game_mode = 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_press = pygame.mouse.get_pos()
            if start_button_rect.collidepoint(mouse_press):
                start_time = int(pygame.time.get_ticks() / 1000)
                game_mode = 3

    if game_mode == 0:

        display_environment()
        
    elif game_mode == 1:

        player_rect.centerx -= 4
        if player_rect.centerx < 150:
            player_rect.centerx = 150 

        grd_rect.x  -= 4
        grd_rect_2.x -= 4

        if grd_rect.x < -600:
            grd_rect.x = 0
            grd_rect_2.x = 600

        bg_rect.x  -= 4
        bg_rect_2.x -= 4

        if bg_rect.x < -600:
            bg_rect.x = 0
            bg_rect_2.x = 600

        if player_rect.bottom > 480:
            player_rect.bottom = 480

        if player_rect.top < 0:
            player_rect.top = 0

        obstacle_rect.x -= 4
        obstacle_rect_t.x -= 4
        
        if obstacle_rect.x < -100:
            obstacle_rect.x = 600
            obstacle_rect_t.x = 600
            random_int = randint(0,5)
            obstacle_rect.top = (obstacle_y_list[random_int] + 100)
            obstacle_rect_t.bottom = obstacle_y_list[random_int] 

        if player_rect.colliderect(obstacle_rect) or player_rect.colliderect(obstacle_rect_t) or player_rect.bottom > 479 :
            game_mode = 2

        gravity += 1
        player_rect.y += gravity

        title_rect.y -= 20
        start_msg_rect.y += 20

        display_environment()
        display_scores()

        sb_h_score = font.render(str(display_high_score()),False,(10,10,10))  
        sb_score = font.render(str(display_score()),False,(10,10,10))
        sb_score_rect = sb_score.get_rect(centerx=410,centery=585)
        sb_h_score_rect = sb_h_score.get_rect(centerx=410,centery=650)

    elif game_mode == 2:
        display_environment()

        patetes += 3
        scoreboard_rect.y -= patetes
        sb_h_score_rect.y -= patetes
        sb_score_rect.y -= patetes
        start_button_rect.y -= patetes

        if sb_score_rect.centery < 285:
            sb_score_rect.centery = 285
        
        if start_button_rect.top < 400:
            start_button_rect.top = 400

        if sb_h_score_rect.centery < 350:
            sb_h_score_rect.centery = 350

        if scoreboard_rect.centery < 300:
            scoreboard_rect.centery = 300    
  
    elif game_mode == 3:

        display_reset()
        display_environment()

    pygame.display.update()
    clock.tick(fps)



