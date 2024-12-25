import pygame
import numpy as np


pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("1")

point = np.array([50, 50])  

def apply_transformation(point, matrix):
    return np.dot(matrix, point)

transformation_matrix = np.array([[1, 3], [4, 1]])  

transformed_point = apply_transformation(point, transformation_matrix)

print(f"Начальные координаты: {point}")
print(f"Полученные координаты: {transformed_point}")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, point, 5)
    pygame.draw.circle(screen, BLUE, transformed_point, 5)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()