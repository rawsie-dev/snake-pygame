import pygame
import Var
import math
import States.Music as Music
import States.Settings as Settings
from States.Slider import Slider, Menu, UI

def click_pause():
    Var.gamepause = not Var.gamepause

    if not Var.gamepause:
        Music.resume()
        return

    Music.pause()
    Music.click()

def GamePause():
    Var.bad_apple_last_frame = -2
    Var.snake_rgb_last_frame = -2

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            Var.history_keys_pressed.append(event.key)
            if Var.history_keys_pressed[-10:] == Var.snake_rgb_key_code:
                Var.snake_rgb = not Var.snake_rgb
                if Var.snake_epilepsy: 
                    Var.snake_epilepsy = False
                    Var.history_keys_pressed.append(-1)
            if Var.history_keys_pressed[-30:] == Var.snake_rgb_key_code * 3:
                Var.history_keys_pressed.append(-1)
                Var.snake_epilepsy = not Var.snake_epilepsy

            if event.key == pygame.K_ESCAPE: 
                Var.gamepause = False
                Var.running = False
                Var.settings = False

            elif event.key == pygame.K_p:
                click_pause()
        elif event.type == pygame.QUIT:
            Var.gamepause = False
            Var.running = False
            Var.settings = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (Var.SCREEN_WIDTH/2 - 160 <= event.pos[0] <= Var.SCREEN_WIDTH/2 - 60) and (210 <= event.pos[1] <= 250):
                Music.click()
                click_pause()
            elif (Var.SCREEN_WIDTH/2 - 50 <= event.pos[0] <= Var.SCREEN_WIDTH/2 + 50) and (210 <= event.pos[1] <= 250):
                Music.click()
                Var.running = False
                Var.settings = True
            elif (Var.SCREEN_WIDTH/2 + 60 <= event.pos[0] <= Var.SCREEN_WIDTH/2 + 160) and (210 <= event.pos[1] <= 250):
                Music.click()
                Var.gamepause = False
                Var.running = False
                Var.settings = False

            elif (380 <= event.pos[0] <= 480) and (287 <= event.pos[1] <= 327): 
                Var.mute_music = not Var.mute_music
                Music.click()
            elif (380 <= event.pos[0] <= 480) and (332 <= event.pos[1] <= 372): 
                Var.mute_sfx = not Var.mute_sfx
                if not Var.mute_sfx:
                    Music.click()

            dist_x = event.pos[0] - (Var.SCREEN_WIDTH - 64)
            dist_y = event.pos[1] - (Var.SCREEN_WIDTH - 45)
            if math.hypot(dist_x, dist_y) <= 30:
                Music.click()
                click_pause()
            

    s = pygame.Surface((Var.SCREEN_WIDTH, Var.SCREEN_HEIGHT - 100))  # the size of your rect
    s.set_alpha(50)                # alpha level
    s.fill((0, 0, 0))           # this fills the entire surface
    Var.screen.blit(s, (0, 0))
    Var.screen.blit(pygame.transform.gaussian_blur(Var.screen, 2), (0, 0))

    font = pygame.font.Font('freesansbold.ttf', 50)
    pauseText = font.render('GAME PAUSED', True, (255, 255, 255))
    Var.screen.blit(pauseText, (Var.SCREEN_WIDTH/2-187, 130))
    

    pygame.draw.rect(Var.screen, (0, 140, 0), (Var.SCREEN_WIDTH/2 - 160, 210, 100, 40))
    pygame.draw.rect(Var.screen, (0, 140, 0), (Var.SCREEN_WIDTH/2 - 50, 210, 100, 40))
    pygame.draw.rect(Var.screen, (0, 140, 0), (Var.SCREEN_WIDTH/2 + 60, 210, 100, 40))

    font = pygame.font.Font('freesansbold.ttf', 20)
    option1 = font.render('Resume', True, (255, 255, 255))
    option2 = font.render('Replay', True, (255, 255, 255))
    Var.screen.blit(option1, (Var.SCREEN_WIDTH/2 - 149, 220))
    Var.screen.blit(option2, (Var.SCREEN_WIDTH/2 - 33, 220))
    option3 = font.render('Quit', True, (255, 255, 255))
    Var.screen.blit(option3, (Var.SCREEN_WIDTH/2 + 85, 220))

    font = pygame.font.Font('freesansbold.ttf', 28)

    textMusic = font.render('Music:', True, (255, 255, 255))
    Var.screen.blit(textMusic, (120, 298))
    pygame.draw.rect(Var.screen, ((0, 200, 0) if Var.mute_music else (0, 100, 0)), (380, 287, 100, 40))
    music = font.render(("Off" if Var.mute_music else "On"), True, (255, 255, 255))
    Var.screen.blit(music, (405, 292))

    textSfx = font.render('SFX:', True, (255, 255, 255))
    Var.screen.blit(textSfx, (120, 343))
    pygame.draw.rect(Var.screen, ((0, 200, 0) if Var.mute_sfx else (0, 100, 0)), (380, 332, 100, 40))
    sfx = font.render(("Off" if Var.mute_sfx else "On"), True, (255, 255, 255))
    Var.screen.blit(sfx, (405, 337))

    textVolume = font.render('Volume:', True, (255, 255, 255))
    Var.screen.blit(textVolume, (120, 388))
    Settings.volume_slider_pause.run()
    Var.volume = Settings.volume_slider_pause.sliders[0].get_value()
    Music.set_volume((0 if Var.mute_music else Var.volume/100), (0 if Var.mute_sfx else Var.volume/100))
    Settings.volume_slider.sliders[0].update_value(Var.volume)


