import pygame
pygame.init()
#Cesty k obrázkům
IMAGE_PATH = 'character/st.png'
BUTTON_IMAGE_PATH = 'images/button.png'

#Nastavení rozměrů
WIDTH = 1280
HEIGHT = 720
#Nastavení postavy
PLAYER_SPEED = 1
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 100

ENEMY_IMAGE = "images/button.png"

BACKGROUND_IMAGE = "images/background.png"





#Definice fontů
title_font = pygame.font.SysFont('Arial',100)
menu_font = pygame.font.SysFont('Arial',50)
#Načtení a úprava obrázku tlačítka pro hlavní menu
#button_img = pygame.image.load(BUTTON_IMAGE_PATH).convert_alpha()
#button_img = pygame.transform.scale(button_img, (300, 80))
#Hlavní menu - Texty a jejich umístění
title_text = title_font.render("Accursed souls", True, (255,255,255))
title_rect = title_text.get_rect(midleft=(70,70))
play_text = menu_font.render("Play", True, (255,255,255))
play_rect = play_text.get_rect(midleft=(70,200))
settings_text = menu_font.render("Settings", True, (255,255,255))
settings_rect = settings_text.get_rect(midleft=(70,300))
exit_text = menu_font.render("Exit", True, (255,255,255))
exit_rect = exit_text.get_rect(midleft=(70,600))
#Menu Nastavení
audio_text = menu_font.render("Audio", True, (255,255,255))
audio_rect = audio_text.get_rect(midleft=(70,200))
video_text = menu_font.render("Video", True, (255,255,255))
video_rect = video_text.get_rect(midleft=(70,300))
gameplay_text = menu_font.render("Gameplay", True, (255,255,255))
gameplay_rect = gameplay_text.get_rect(midleft=(70,400))
return_text = menu_font.render("return", True, (255,255,255))
return_rect = return_text.get_rect(midleft=(70,600))
#Podrobnosti v nastavení
difficulty_text = menu_font.render("Difficulty", True, (255,255,255))
difficulty_rect = difficulty_text.get_rect(center=(440,200))

fullscreen_text = menu_font.render("Fullscreen", True, (255,255,255))
fullscreen_rect = fullscreen_text.get_rect(center=(440,200))

main_volume_text = menu_font.render("Main volume", True, (255,255,255))
main_volume_rect = main_volume_text.get_rect(center=(440,200))

