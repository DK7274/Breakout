import pygame

pygame.init()
screen = pygame.display.set_mode((1000,1000)) #sets size of window
backdrop = pygame.image.load("Images/gorrila.jpg") #loads monkey
backdrop = pygame.transform.scale(backdrop,(1000,1000)) #resizes image
backdropbox = screen.get_rect()
pygame.display.set_caption("Breaking Out") #names window

clock = pygame.time.Clock()

game_over = False

while not game_over:
    dt = clock.tick(50)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    screen.blit(backdrop,backdropbox)
    pygame.display.flip()

pygame.quit()