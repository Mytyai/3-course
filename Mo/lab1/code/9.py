import pygame
import numpy as np


pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("9")

L = np.array([[5, 1], [5, 2], [3, 2]]) * 60
T = np.array([[2, 0], [0, 2]])

scaled_L = (T @ L.T).T

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.polygon(screen, RED, L, 5)  
    pygame.draw.polygon(screen, BLUE, scaled_L, 5)
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()