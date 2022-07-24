import pygame
from pygame import K_RIGHT, K_LEFT

pygame.init()
screen = pygame.display.set_mode((1000,1000)) #sets size of window
backdrop = pygame.image.load("Images/gorrila.jpg") #loads monkey
backdrop = pygame.transform.scale(backdrop,(1000,1000)) #resizes image
backdropbox = screen.get_rect()
pygame.display.set_caption("Breaking Out") #names window

#bat
bat = pygame.image.load("Images/breakout.png").convert_alpha()
bat_rect = bat.get_rect()
bat_rect[1] = screen.get_height() - 100 #starts bat 100 off the bootom
#ball
ball = pygame.image.load("Images/ball.png").convert_alpha()
ball_rect = ball.get_rect()
ball_start = (200,200)
ball_speed = (3.0,3.0)
ball_served = False
sx,sy = ball_speed
ball_rect.topleft = ball_start
#bricks
brick = pygame.image.load("Images/brick.png").convert_alpha()
bricks = []
brick_rect = brick.get_rect()
brick_rows = 5
brick_cols = 3
brick_gap = 10

brick_cols = screen.get_width() // (brick_rect[2] + brick_gap)
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap)*brick_cols + brick_gap) // 2
for y in range(brick_rows):
    brickY = (y*(brick_rect[3]+brick_gap) + brick_gap)
    for x in range(brick_cols):
        brickX = x*(brick_rect[2] + brick_gap) + side_gap
        bricks.append((brickX,brickY))

clock = pygame.time.Clock()
game_over = False
x=0

while not game_over:
    dt = clock.tick(60)
    screen.fill((0,0,0))
    screen.blit(backdrop,(0,0))
    for b in bricks:
        screen.blit(brick,b)
    screen.blit(bat,bat_rect)
    screen.blit(ball,ball_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pressed = pygame.key.get_pressed()
    if pressed[K_LEFT]:
        x -=1*dt

    if pressed[K_RIGHT]:
        x += 1*dt

    screen.blit(bat,bat_rect)
    bat_rect[0]
    pygame.display.update()

pygame.quit()