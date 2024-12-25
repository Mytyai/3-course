import pygame
import numpy as np


pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("4")

L = np.array([[0, 100], [200, 300]])  
T = np.array([[1, 2], [3, 1]])  

transformed_L = (T @ L.T).T

midpoint_L = (L[0] + L[1]) / 2

midpoint_transformed_L = (transformed_L[0] + transformed_L[1]) / 2

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.line(screen, RED, L[0], L[1], 5)
    pygame.draw.circle(screen, RED, midpoint_L.astype(int), 7)

    pygame.draw.line(screen, BLUE, transformed_L[0], transformed_L[1], 5)
    pygame.draw.circle(screen, BLUE, midpoint_transformed_L.astype(int), 7)

    pygame.draw.line(screen, GREEN, midpoint_L, midpoint_transformed_L, 1)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()