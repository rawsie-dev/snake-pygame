import pygame
import Var
import Utility
import random

def initialize_music():
    Var.sound_death = pygame.mixer.Sound(Utility.resource_path(Var.music_death))
    Var.sound_click = pygame.mixer.Sound(Utility.resource_path(Var.music_click))
    Var.sound_apple_eat = pygame.mixer.Sound(Utility.resource_path(Var.music_apple_eat))

    pygame.mixer.music.set_volume(0.375)
    Var.sound_death.set_volume(0.5)
    Var.sound_click.set_volume(0.5)
    Var.sound_apple_eat.set_volume(0.5)

def settings():
    pygame.mixer_music.load(Utility.resource_path(Var.music_settings))
    pygame.mixer_music.play(-1)

def main_game():
    if Var.bad_apple:
        pygame.mixer_music.load(Utility.resource_path(Var.music_bad_apple))
        pygame.mixer_music.play(-1)
        return
    if Var.snake_skin == 3:
        pygame.mixer_music.load(Utility.resource_path(Var.music_frisk[Var.music_frisk_index]))
        pygame.mixer_music.play()
        return
    pygame.mixer_music.load(Utility.resource_path(Var.music_game[Var.music_index]))
    pygame.mixer_music.play()

def game_over():
    pygame.mixer.Channel(0).play(Var.sound_death)
    if random.randint(1, 5) == 1 and not Var.loss < 3:
        pygame.mixer_music.load(Utility.resource_path(Var.music_rick_roll))
        pygame.mixer_music.play(-1)
    else:
        pygame.mixer_music.load(Utility.resource_path(Var.music_game_over))
        pygame.mixer_music.play(-1)

def win():
    pygame.mixer_music.load(Utility.resource_path(Var.music_win))
    pygame.mixer_music.play(1)

def click():
    pygame.mixer.Channel(1).play(Var.sound_click)

def apple_eat():
    pygame.mixer.Channel(2).play(Var.sound_apple_eat)

def set_volume(music, sfx):
    pygame.mixer.music.set_volume(music * 0.75)
    Var.sound_death.set_volume(sfx)
    Var.sound_click.set_volume(sfx)
    Var.sound_apple_eat.set_volume(sfx)

def pause():
    pygame.mixer.music.pause()
    pygame.mixer.pause()

def resume():
    pygame.mixer.music.unpause()
    pygame.mixer.unpause()
