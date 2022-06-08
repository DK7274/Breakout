import pygame

pygame.init()
screen = pygame.display.set_mode((550,366))
backdrop = pygame.image.load("gorrila.jpg")

pygame.display.set_caption("Breaking Out")

game_over = False

while not game_over:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pygame.display.flip()

pygame.quit()