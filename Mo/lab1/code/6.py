import pygame
import numpy as np


pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("6")

L = np.array([[-0.5, 1.5], [3, -2], [-1, -1], [3, 5/3]]) * 100
T = np.array([[1, 2], [1, -3]])  

transformed_L = np.dot(T, L.T).T

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.line(screen, RED, L[0], L[1], 5)
    pygame.draw.line(screen, RED, L[2], L[3], 5)
    pygame.draw.line(screen, BLUE, transformed_L[0], transformed_L[1], 5)
    pygame.draw.line(screen, BLUE, transformed_L[2], transformed_L[3], 5)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()