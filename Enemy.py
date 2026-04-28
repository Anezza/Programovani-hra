import pygame
from settings import *
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(ENEMY_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))

        self.rect = self.image.get_rect(
            midbottom=(WIDTH + random.randint(100, 400), HEIGHT - 10)
        )

        self.speed = 0.6

    def update(self):
        self.rect.x -= self.speed

        # если ушёл за экран → появляется снова справа
        if self.rect.right < 0:
            self.rect.left = WIDTH + random.randint(100, 400)