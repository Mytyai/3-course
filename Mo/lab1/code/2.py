import pygame


pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("2")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

font = pygame.font.SysFont(None, 50)

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.circle(screen, BLACK, (350, 350), 50)
    pygame.draw.line(screen, BLUE, (50, 50), (400, 50), 5)
    pygame.draw.line(screen, RED, (50, 100), (400, 100), 5)
    pygame.draw.line(screen, YELLOW, (50, 150), (400, 150), 5)

    text = font.render("Hello world!", True, GREEN)
    screen.blit(text, (200, 200))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()