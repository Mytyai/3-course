import pygame
import numpy as np


pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("10")

a, b = 100, 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

running = True
while running:
    screen.fill(WHITE)

    for theta in np.linspace(0, 5 * np.pi, 5000):
            r = b + 2 * a * np.cos(theta)
            x = int(r * np.cos(theta) + 350)
            y = int(r * np.sin(theta) + 350)

            pygame.draw.circle(screen, BLACK, (x, y), 1)
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()