import pygame
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.run_images_right = [
            pygame.image.load('pics/enp1.png'),
            pygame.image.load('pics/enp2.png')]
        self.run_images_left = [
            pygame.image.load('pics/enl1.png'),
            pygame.image.load('pics/enl2.png')]
        self.idle_image = pygame.image.load('pics/enst.png')
        self.image = self.idle_image
        self.image = pygame.transform.scale(self.image,(PLAYER_WIDTH,PLAYER_HEIGHT))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 0
        self.jump_vel = 0
        self.jump = 0
        self.move_delay = 0
        self.on_ground = False
        self.frame_index = 0
        self.anim_timer = 0
        self.facing = 1
    def update(self):
        self.rect.x += self.speed
        self.jump_vel += 1
        if self.speed > 0:
            self.facing = 1
        elif self.speed < 0:
            self.facing = -1
        if self.jump_vel > 20:
            self.jump_vel = 20
        self.rect.y += self.jump_vel 
        self.on_ground = False
        if self.speed != 0:
            self.anim_timer += 1
            if self.anim_timer >= 5:
                self.anim_timer = 0
                self.frame_index += 1
                if self.facing == 1:
                    frames = self.run_images_right
                else:
                    frames = self.run_images_left
                if self.frame_index >= len(frames):
                    self.frame_index = 0
                self.image = frames[self.frame_index]
        else:
            if self.facing == 1:
                self.image = self.run_images_right[0]
            else:
                self.image = self.run_images_left[0]
            self.frame_index = 0