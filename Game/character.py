import pygame
from settings import *
class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.attack_images = [
            pygame.image.load('pics/1.png').convert_alpha(),
            pygame.image.load('pics/2.png').convert_alpha(),
            pygame.image.load('pics/3.png').convert_alpha(),
            pygame.image.load('pics/4.png').convert_alpha(),
            pygame.image.load('pics/5.png').convert_alpha(),
            pygame.image.load('pics/6.png').convert_alpha()]
        self.run_images = [
            pygame.image.load('pics/chp.png'),
            pygame.image.load('pics/chp3.png')]
        self.idle_image = pygame.image.load('pics/st.png')
        self.image = self.idle_image
        self.image = pygame.transform.scale(self.image,(PLAYER_WIDTH,PLAYER_HEIGHT))
        self.rect = self.image.get_rect(center = (WIDTH//2,HEIGHT-100))
        self.speed = 0
        self.jump_vel = 0
        self.jump = 0
        self.frame_index = 0
        self.anim_timer = 0
        self.attack_rect = None
        self.facing = 1
        self.attacking = False
        self.attack_timer = 0
        self.attack_cooldown = 0 
        self.attack_frame = 0
        self.attack_image = self.attack_images[0]
        self.on_ground = False
    def start_attack(self):
        if self.attack_cooldown == 0:
            self.attacking = True
            self.attack_timer = 12
            self.attack_frame = 0
            self.attack_cooldown = 20   
    def update(self):
        keys = pygame.key.get_pressed()
        if abs(self.speed) > 0.1:
            self.anim_timer += 1
            if self.anim_timer >= 5:
                self.anim_timer = 0
                self.frame_index += 1
                if self.frame_index >= len(self.run_images):
                    self.frame_index = 0
            self.image = self.run_images[self.frame_index]
        else:
            self.image = self.idle_image
            self.frame_index = 0
        if self.speed < 0:
            self.image = pygame.transform.flip(self.image, True, False)
        self.attack_rect = None
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        if self.attacking:
            self.attack_timer -= 1
            progress = 12 - self.attack_timer
            if progress <= 2:
                self.attack_frame = 0
            elif progress <= 4:
                self.attack_frame = 1
            elif progress <= 6:
                self.attack_frame = 2
            elif progress <= 8:
                self.attack_frame = 3
            elif progress <= 10:
                self.attack_frame = 4
            else:
                self.attack_frame = 5
            attack_rect = pygame.Rect(self.rect)
            if self.on_ground == True and self.facing == 1:
                attack_rect.x += self.rect.width//2 + 16
            elif self.on_ground == True and self.facing == 2:
                attack_rect.x -= self.rect.width//2 + 16
            elif self.on_ground == True and self.facing == 3:
                attack_rect.y -= self.rect.height//2 + 16
            elif self.on_ground == False:
                attack_rect.y += self.rect.height//2 + 16
            attack_rect.width = self.rect.width
            self.attack_rect = attack_rect
            base_image = self.attack_images[self.attack_frame]
            if self.facing == 1:
                self.attack_image = base_image
            elif self.facing == 2:
                self.attack_image = pygame.transform.flip(base_image, True, False)
            elif self.facing == 3:
                self.attack_image = pygame.transform.rotate(base_image, 90)
            elif self.on_ground == False:
                self.attack_image = pygame.transform.rotate(base_image, -90)
            if self.attack_timer <= 0:
                self.attacking = False
                self.attack_frame = 0
                self.attack_rect = None
        if keys[pygame.K_w]:
            self.facing = 3
        if keys[pygame.K_a] and self.rect.left > 0:
            self.speed -= 1
        elif keys[pygame.K_d] and self.rect.right < WIDTH:
            self.speed += 1
        if self.speed > 0:
            self.speed -= 0.5
            self.facing = 1
            if self.speed < 0:
                self.speed = 0
        elif self.speed < 0:
            self.speed += 0.5
            self.facing = 2
            if self.speed > 0:
                self.speed = 0
        if keys[pygame.K_SPACE] and self.jump == 0:
            self.jump = 1
            self.jump_vel = -20
            self.on_ground = False
        self.jump_vel += 1
        if self.jump_vel > 20:
            self.jump_vel = 20
        if self.speed > 7:
            self.speed = 7
        if self.speed < -7:
            self.speed = -7
        self.rect.y += self.jump_vel
        self.rect.x += self.speed