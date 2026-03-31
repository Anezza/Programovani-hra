import pygame
import sys
from settings import *
import character
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
fullscreen = False
state = "MENU"
settings_state = "SETTINGS"
running = True
while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
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
        screen.fill((0,0,0))
        vypis_menu()
    elif state == "PLAYING":
        screen.fill((0,0,0))
    elif state == "SETTINGS":
        screen.fill((0,0,0))
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
    pygame.display.update()
pygame.quit()