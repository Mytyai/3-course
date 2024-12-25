import pygame
import random


class Bonus(pygame.sprite.Sprite):
    def __init__(self, ai_game, bonus_type):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load(f"images/{bonus_type}_bonus.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.screen.get_width() - self.rect.width)
        self.rect.y = 0

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.bonus_speed
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)