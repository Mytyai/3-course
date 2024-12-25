import pygame
import numpy as np
import math

pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption('11')

initial_vertices = np.array([[2, -2], [-2, -2], [-2, 2], [2, 2]]) * 100
m = 0.9
alpha = math.pi / 32  

WHITE = (255, 255, 255)
RED = (255, 0, 0)

def transform(vertices, scale, angle):
    scaled_vertices = vertices * scale
    
    rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
    
    rotated_vertices = scaled_vertices @ rotation_matrix
    
    return rotated_vertices

def center_vertices(vertices, screen_size):
    center_x, center_y = screen_size[0] / 2, screen_size[1] / 2
    centered_vertices = vertices + np.array([center_x, center_y])
    return centered_vertices

running = True
vertices = initial_vertices.copy()
while running:
    screen.fill((WHITE))
    
    transformed_vertices = vertices
    for i in range(20):
        transformed_vertices = transform(transformed_vertices, m, alpha)
        
        centered_vertices = center_vertices(transformed_vertices, (700, 700))
        
        points = centered_vertices.astype(int)
        pygame.draw.polygon(screen, RED, points.tolist(), 2)
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
pygame.quit()
