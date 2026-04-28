import pygame
from settings import *
class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(IMAGE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.image,(PLAYER_WIDTH,PLAYER_HEIGHT))

        self.rect = self.image.get_rect(midbottom=(100, HEIGHT - 10))

        self.jump_power = -18   # сильнее прыжок
        self.gravity = 0
        self.gravity_force = 0.6  # слабее гравитация

    def update(self):
        keys = pygame.key.get_pressed()

    # skok
        if (keys[pygame.K_w] or keys[pygame.K_SPACE]) and self.rect.bottom >= HEIGHT - 10:
            self.gravity = self.jump_power

    # gravitce
        self.gravity += self.gravity_force
        self.rect.y += self.gravity

    # zem
        if self.rect.bottom >= HEIGHT - 10:
            self.rect.bottom = HEIGHT - 10