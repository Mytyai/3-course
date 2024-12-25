import pygame
import numpy as np


pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("3")

line_start = np.array([10, 10])
line_end = np.array([50, 100])
transformation_matrix = np.array([[1, 3], [4, 1]])

transformed_line_start = transformation_matrix @ line_start
transformed_line_end = transformation_matrix @ line_end

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.line(screen, RED, line_start, line_end, 5)
    pygame.draw.line(screen, BLUE, transformed_line_start, transformed_line_end, 5)
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()