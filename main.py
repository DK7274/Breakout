import pygame
from pygame.locals import*
# rect is for rectangle properties, (0 = left, 1 = top, 2 = width, 3 = height)
pygame.init()

screen = pygame.display.set_mode((1000,950)) #sets size of window
backdrop = pygame.image.load("Images/gorrila.jpg").convert() #loads monkey
backdrop = pygame.transform.scale(backdrop,(1000,950)) #resizes image
pygame.display.set_caption("Breaking Out") #names window
backdropbox = screen.get_rect()

#bat
bat = pygame.image.load("Images/breakout.png").convert_alpha()
bat_rect = bat.get_rect()
bat_rect[1] = screen.get_height() - 150 #starts bat 150 off the bootom
#ball
ball = pygame.image.load("Images/ball.png").convert_alpha()
ball = pygame.transform.scale(ball,(100,100))
ball_rect = ball.get_rect()
ball_start = (50 ,300)
ball_speed = (3.0,3.0)
ball_served = False
sx,sy = ball_speed # speed x,y direction
ball_rect.topleft = ball_start # sets the ball position
#bricks
brick = pygame.image.load("Images/brick.png").convert_alpha()
brick = pygame.transform.scale(brick,(100,50))
bricks = []
brick_rect = brick.get_rect()
brick_rows = 5
brick_cols = 3
brick_gap = 10

brick_cols = screen.get_width() // (brick_rect[2] + brick_gap) #gets screen width and uses floor division to find the closest WHOLE NUMBER added with gaps for columns
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap)*brick_cols + brick_gap) // 2
for y in range(brick_rows):
    brickY = (y*(brick_rect[3]+brick_gap) + brick_gap) #offset y axis by brick gap
    for x in range(brick_cols):
        brickX = x*(brick_rect[2] + brick_gap) + side_gap #offset x axis by brick gap
        bricks.append((brickX,brickY))

clock = pygame.time.Clock()
game_over = False
x=0
screen.blit(backdrop,backdropbox)

while not game_over:
    dt = clock.tick(50)
    # now blit backdrop onto backdropbox
    screen.fill((0,0,0))
    screen.blit(backdrop,(0,0))
    for b in bricks:
        screen.blit(brick,b) #loads all the bricks into the scene in a looping array
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

    if pressed[K_SPACE]:
        ball_served = True

    if bat_rect[0] + bat_rect.width >= ball_rect[0] >= bat_rect[0] and \
        ball_rect[1] + ball_rect.width >= bat_rect[1] and \
        sy > 0: #when bat hit ball it reverts all movement
        sy *= -1

        #speed up when hit ball and limit speed to 10
        if sx > 10:
            sx = 10
        if sx < -10:
            sx = -10
        if sy > 10:
            sy = 10
        if sy < -10:
            sy = -10
        else:
            sx *= 1.5
            sy *= 1.5

        continue
    # screen edge effect

    # brick hits
    delete_brick = None
    for b in bricks:
        bx,by = b  # get the vals of the brick
        if bx <= ball_rect[0] <= bx + brick_rect.width and by <= ball_rect[1] <= by + brick_rect.height and \
        by <= ball_rect[1] <= by + brick_rect.height:
            delete_brick = b

            if ball_rect[0] <= bx + 2:
                sx *= -1
            elif ball_rect[0] >= bx + brick_rect.width - 2:
                sx *= -1
            if ball_rect[1] <= by + 2:
                sy *= -1
            elif ball_rect[1] >= by + brick_rect.height - 2:
                sy *= -1
            break

    if delete_brick is not None:
        bricks.remove(delete_brick)

    #the None keyword is used to define a null value, or no value at all
    # None is not the same as 0, False, or an empty string.
    #None is a data type of its own (NoneType) and only None can be None

    #top

    if ball_rect[1] <=0: # Y pos
        ball_rect[1] = 0
        sy *= -1 # flips direction

    #bottom

    if ball_rect[1] >= screen.get_height() - ball_rect.height:
       # ball_rect[1] = screen.get_height() - ball_rect.height
       # sy *= -1
        ball_served = False
        ball_rect.topleft = ball_start

    #left
    if ball_rect[0] <=0:
        ball_rect[0] = 0
        sx *= -1
    #right
    if ball_rect[0] >= screen.get_width() - ball_rect.width:
        ball_rect[0] = screen.get_width()  - ball_rect.width
        sx *= -1
        # move ball after space is pressed


    #move the ball
    ball_rect[0]: x #get position of ball

    if ball_served:
        ball_rect[0] += sx # move left
        ball_rect[1] += sy # move right

    screen.blit(bat,bat_rect) #updates position of the bat
    bat_rect[0] = x
    if ball_served:
        ball_rect[0] += sx
        ball_rect[1] += sy
    pygame.display.update()

pygame.quit()