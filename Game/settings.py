import pygame
pygame.init()

BUTTON_IMAGE_PATH = 'pics/button.png'

WIDTH = 1280
HEIGHT = 720

PLAYER_WIDTH = 64
PLAYER_HEIGHT = 64




title_font = pygame.font.SysFont('Arial',100)
menu_font = pygame.font.SysFont('Arial',50)
title_text = title_font.render("Accursed souls", True, (255,255,255))
title_rect = title_text.get_rect(midleft=(70,70))
play_text = menu_font.render("Play", True, (255,255,255))
play_rect = play_text.get_rect(midleft=(70,200))
settings_text = menu_font.render("Settings", True, (255,255,255))
settings_rect = settings_text.get_rect(midleft=(70,300))
exit_text = menu_font.render("Exit", True, (255,255,255))
exit_rect = exit_text.get_rect(midleft=(70,600))

audio_text = menu_font.render("Audio", True, (255,255,255))
audio_rect = audio_text.get_rect(midleft=(70,200))
video_text = menu_font.render("Video", True, (255,255,255))
video_rect = video_text.get_rect(midleft=(70,300))
gameplay_text = menu_font.render("Gameplay", True, (255,255,255))
gameplay_rect = gameplay_text.get_rect(midleft=(70,400))
return_text = menu_font.render("return", True, (255,255,255))
return_rect = return_text.get_rect(midleft=(70,600))

difficulty_text = menu_font.render("Difficulty", True, (255,255,255))
difficulty_rect = difficulty_text.get_rect(center=(440,200))

fullscreen_text = menu_font.render("Fullscreen", True, (255,255,255))
fullscreen_rect = fullscreen_text.get_rect(center=(440,200))

main_volume_text = menu_font.render("Main volume", True, (255,255,255))
main_volume_rect = main_volume_text.get_rect(center=(440,200))