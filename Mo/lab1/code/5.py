import pygame
import numpy as np


pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("5")

L = np.array([[50, 100], [250, 200], [50, 200], [250, 300]])
T = np.array([[1, 2], [3, 1]])  

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