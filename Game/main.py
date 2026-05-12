import pygame
import sys
import random
from settings import *
from character import *
from Platforms import *
from enemy import *
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
background = pygame.image.load('pics/gamebackground.png').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
hrac = Character()
hrac_group = pygame.sprite.Group()
hrac_group.add(hrac)
platforms = pygame.sprite.Group()
plat1 = Platform(0, HEIGHT - 20, WIDTH, 20)
plat2 = Platform(0, HEIGHT - 190, WIDTH // 4, 15)
plat3 = Platform(WIDTH - WIDTH // 4, HEIGHT - 190, WIDTH // 4, 15)
plat4 = Platform(426, HEIGHT - 360, 428, 15)
platforms.add(plat1, plat2, plat3, plat4)
enemy = Enemy(640,HEIGHT-360)
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)
state = "MENU"
settings_state = "SETTINGS"
spawn_points = [(160,HEIGHT - 190), (640,HEIGHT-360), (1120,HEIGHT - 190)]
enemy_spawn_timer = 0
body = 0
base_font = pygame.font.Font(None, 40)
score_text = base_font.render(f"score: {body}", True, (255,255,255))
def hra():
    global state, enemy_spawn_timer, body, score_text
    hrac_group.update()
    hrac_group.draw(screen)
    platforms.update()
    platforms.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    screen.blit(score_text,(10,50))
    plat_coll = pygame.sprite.spritecollide(hrac, platforms, False)
    for plat in plat_coll:
        if hrac.jump_vel > 0:
            hrac.rect.bottom = plat.rect.top
            hrac.jump_vel = 0
            hrac.jump = 0
            hrac.on_ground = True
    for enemy in enemy_group:
        enemy_plat_coll = pygame.sprite.spritecollide(enemy, platforms, False)
        for plat in enemy_plat_coll:
            if enemy.jump_vel > 0:
                enemy.rect.bottom = plat.rect.top
                enemy.jump_vel = 0
                enemy.jump = 0
                enemy.on_ground = True
        if enemy.move_delay > 0:
            enemy.move_delay -= 1
        else:
            if enemy.rect.centerx < hrac.rect.centerx:
                enemy.speed = 5
            elif enemy.rect.centerx > hrac.rect.centerx:
                enemy.speed = -5
            if enemy.on_ground and enemy.rect.centery > hrac.rect.centery:
                enemy.jump_vel = -20
                enemy.on_ground = False
            enemy.move_delay = 30
    if pygame.sprite.spritecollide(hrac,enemy_group, False):
        hrac.kill()
        state = "GAME_OVER"
    if hrac.attacking:
        screen.blit(hrac.attack_image, hrac.attack_rect)
    if hrac.attack_rect:
        for enemy in enemy_group:
            if hrac.attack_rect.colliderect(enemy.rect):
                enemy.kill()
                body += 1
                score_text = base_font.render(f"score: {body}", True, (255,255,255))
    enemy_spawn_timer += 1
    if enemy_spawn_timer >= 30 and len(enemy_group) < 3:
        x, y = random.choice(spawn_points)
        enemy_group.add(Enemy(x, y))
        enemy_spawn_timer = 0
def vypis_menu():
    screen.blit(title_text, title_rect)
    screen.blit(play_text,play_rect)
    screen.blit(settings_text,settings_rect)
    screen.blit(exit_text,exit_rect)
def vypis_settings():
    screen.blit(audio_text,audio_rect)
    screen.blit(video_text,video_rect)
    screen.blit(gameplay_text,gameplay_rect)
    screen.blit(return_text,return_rect)
def vypis_gameplay():
    screen.blit(difficulty_text,difficulty_rect)
def vypis_audio():
    screen.blit(main_volume_text,main_volume_rect)
def vypis_video():
    screen.blit(fullscreen_text,fullscreen_rect)
def reset_game():
    global hrac, enemy_group, state, body, score_text
    enemy_group.empty()
    hrac.rect.center = (WIDTH//2,HEIGHT-100)
    hrac.speed = 0
    hrac.jump_vel = 0
    hrac.jump = 0
    hrac.attacking = False
    hrac.attack_rect = None
    hrac_group.add(hrac)
    body = 0
    score_text = base_font.render(f"score: {body}", True, (255,255,255))
fullscreen = False
running = True
while running:
    for event in pygame.event.get(): 
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if state == "PLAYING":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        hrac.start_attack()
            if state == "MENU":
                if play_rect.collidepoint(mouse_pos):
                    state = "PLAYING"                     
                elif settings_rect.collidepoint(mouse_pos):
                    state = "SETTINGS"
                    settings_state = "SETTINGS"
                elif exit_rect.collidepoint(mouse_pos):
                    running = False
            if state == "SETTINGS":
                if return_rect.collidepoint(mouse_pos):
                    state = "MENU"
                if gameplay_rect.collidepoint(mouse_pos):
                    settings_state = "GAMEPLAY"
                if video_rect.collidepoint(mouse_pos):
                    settings_state = "VIDEO"
                if audio_rect.collidepoint(mouse_pos):
                    settings_state = "AUDIO"
            if settings_state == "VIDEO":
                if fullscreen_rect.collidepoint(mouse_pos):
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((screen.get_width(),screen.get_height()), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(),screen.get_height()), pygame.RESIZABLE)
    if state == "MENU":
        screen.blit(background, (0, 0))
        vypis_menu()
    elif state == "PLAYING":
        screen.blit(background, (0, 0))
        hra()
    elif state == "SETTINGS":
        screen.blit(background, (0, 0))
        if settings_state == "SETTINGS":
            vypis_settings()
        if settings_state == "GAMEPLAY":
            vypis_settings()
            vypis_gameplay()
        if settings_state == "AUDIO":
            vypis_settings()
            vypis_audio()
        if settings_state == "VIDEO":
            vypis_settings()
            vypis_video()
    elif state == "GAME_OVER":
        screen.fill((0,0,0))
        state = "MENU"
        reset_game()
    pygame.display.update()
    clock.tick(30)
    print(hrac.attacking)
pygame.quit()