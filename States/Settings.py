import pygame
import Var
import Utility
import random
from States.Slider import Slider, Menu, UI
import States.Music as Music

UI.init(Var.screen)
menu_board = Menu(Var.screen, [Slider((320, 130), (400, 20), 20, 3, 40), Slider((320, 230), (400, 20), 25, 3, 50)])
volume_slider = Menu(Var.screen, [Slider((320, 130), (400, 20), 50, 0, 100, True)])
volume_slider_pause = Menu(Var.screen, [Slider((371, 405), (220, 20), 50, 0, 100, True, True)])

def settings():
    def page1():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Var.running = False
                Var.retry = False
                Var.settings = False

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
                    Var.running = False
                    Var.retry = False
                    Var.settings = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if (504 < event.pos[0] < 592) and (0 < event.pos[1] < 50):
                    Var.settings_page += 1
                    Music.click()
                if (417 < event.pos[0] <= 504) and (0 < event.pos[1] < 50):
                    Var.settings_page -= 1
                    Music.click()
                Var.settings_page = (Var.settings_page - 1) % 3 + 1

                # SPEED ----------------------------------------------------
                if (45 < event.pos[0] < 195) and (110 < event.pos[1] < 160): 
                    Var.speed = 10
                    Music.click()
                elif (225 < event.pos[0] < 375) and (110 < event.pos[1] < 160): 
                    Var.speed = 7
                    Music.click()
                elif (405 < event.pos[0] < 555) and (110 < event.pos[1] < 160): 
                    Var.speed = 4
                    Music.click()
                # MODE ----------------------------------------------------
                if (45 < event.pos[0] < 195) and (210 < event.pos[1] < 260): 
                    Var.Mode = 0
                    Var.desc = "Standard snake game"
                    Music.click()
                elif (225 < event.pos[0] < 375) and (210 < event.pos[1] < 260): 
                    Var.Mode = 1
                    Var.desc = "The map is a dimensional loop"
                    Music.click()
                # CHALLENGE ----------------------------------------------------
                if (45 < event.pos[0] < 195) and (310 < event.pos[1] < 360): 
                    Var.challenge[1] = 1 - Var.challenge[1]
                    Var.poison_streak = 0
                    Music.click()
                elif (225 < event.pos[0] < 375) and (310 < event.pos[1] < 360): 
                    Var.challenge[2] = 1 - Var.challenge[2]
                    Var.poison_streak = 0
                    Music.click()
                elif (405 < event.pos[0] < 555) and (310 < event.pos[1] < 360): 
                    Var.challenge[3] = 1 - Var.challenge[3]
                    Var.poison_streak += 1
                    if Var.poison_streak >= Var.poison_streak_goal:
                        Var.poison_streak_goal = random.randint(2, 5)
                        Var.bad_apple = not Var.bad_apple
                        Var.poison_streak = 0
                        if Var.bad_apple:
                            Var.text_poison = "Bad Apple"
                            Var.text_poison_position = (409, 322)
                        else:
                            Var.text_poison = "Poison"
                            Var.text_poison_position = (432, 322)
                    Music.click()
                elif (45 < event.pos[0] < 195) and (375 < event.pos[1] < 425): 
                    Var.challenge[4] = 1 - Var.challenge[4]
                    Var.poison_streak = 0
                    Music.click()
                elif (225 < event.pos[0] < 375) and (375 < event.pos[1] < 425): 
                    Var.challenge[5] = 1 - Var.challenge[5]
                    Var.poison_streak = 0
                    Music.click()

                #PLAY
                if (0 < event.pos[0] - Var.SCREEN_WIDTH/2 + 50 < 100) and (0 < event.pos[1] - Var.SCREEN_HEIGHT*6/7 < 40):
                    Var.settings = False
                    Var.running = True
                    Var.colorPlay = (123,116,108)
                    Music.click()

            if event.type == pygame.MOUSEMOTION:
                # print(event.pos[0], event.pos[1])
                if (50 < event.pos[0] < 190) and (310 < event.pos[1] < 360): 
                    Var.rule = "Rule: Avoid stepping onto randomly-spawned landmines"
                elif (225 < event.pos[0] < 350) and (310 < event.pos[1] < 360): 
                    Var.rule = "Rule: Navigate through the map in darkness"
                elif (405 < event.pos[0] < 510) and (310 < event.pos[1] < 360): 
                    Var.rule = "Rule: Eating " + ("poisonous" if not Var.bad_apple else "bad") + " apples will invert your control"
                elif (50 < event.pos[0] < 190) and (375 < event.pos[1] < 425): 
                    Var.rule = "Rule: Apples can move freely across the map"
                elif (225 < event.pos[0] < 350) and (375 < event.pos[1] < 425): 
                    Var.rule = "Rule: The snake reverses its body after eating an apple"
                else: Var.rule = ""

                if (0 < event.pos[0] - Var.SCREEN_WIDTH/2 + 50 < 100) and (0 < event.pos[1] - Var.SCREEN_HEIGHT*6/7 < 40):
                    Var.colorPlay = (255, 0, 0)
                else:
                    Var.colorPlay = (123,116,108)

        font = pygame.font.Font('freesansbold.ttf', 28)
        Var.screen.blit(font.render('< 1 / 3 >', True, (255, 255, 255)), (Var.SCREEN_WIDTH - 142, 10))
        # Speed
        pygame.draw.rect(Var.screen, (Var.colorSelect if Var.speed == 10 else Var.colorUnselect), (45, 110, 150, 50))
        pygame.draw.rect(Var.screen, (Var.colorSelect if Var.speed == 7 else Var.colorUnselect), (225, 110, 150, 50))
        pygame.draw.rect(Var.screen, (Var.colorSelect if Var.speed == 4 else Var.colorUnselect), (405, 110, 150, 50))
        textSpeed = font.render('Speed:', True, (0, 0, 0))
        speed1 = font.render('Slow', True, (255, 255, 255))
        speed2 = font.render('Medium', True, (255, 255, 255))
        speed3 = font.render('Fast', True, (255, 255, 255))
        Var.screen.blit(textSpeed, (30, 70))
        Var.screen.blit(speed1, (85, 120))
        Var.screen.blit(speed2, (245, 120))
        Var.screen.blit(speed3, (451, 120))
            # Variables.Mode
        pygame.draw.rect(Var.screen, (Var.colorSelect if Var.Mode == 0 else Var.colorUnselect), (45, 210, 150, 50))
        pygame.draw.rect(Var.screen, (Var.colorSelect if Var.Mode == 1 else Var.colorUnselect), (225, 210, 150, 50))
        textMode = font.render('Mode:', True, (0, 0, 0))
        mode1 = font.render('Normal', True, (255, 255, 255))
        mode2 = font.render('Loop', True, (255, 255, 255))
        Var.screen.blit(textMode, (30, 170))
        Var.screen.blit(mode1, (69, 220))
        Var.screen.blit(mode2, (265, 220))

        font = pygame.font.Font('freesansbold.ttf', 17)
        textDesc = font.render(Var.desc, True, (0, 0, 0))
        Var.screen.blit(textDesc, (130, 179))

            # Challenge
        font = pygame.font.Font('freesansbold.ttf', 28)
        pygame.draw.rect(Var.screen, (Var.colorSelect if Var.challenge[1] else Var.colorUnselect), (45, 310, 150, 50))
        pygame.draw.rect(Var.screen, (Var.colorSelect if Var.challenge[2] else Var.colorUnselect), (225, 310, 150, 50))
        pygame.draw.rect(Var.screen, (Var.colorSelect if Var.challenge[3] else Var.colorUnselect), (405, 310, 150, 50))
        pygame.draw.rect(Var.screen, (Var.colorSelect if Var.challenge[4] else Var.colorUnselect), (45, 375, 150, 50))
        pygame.draw.rect(Var.screen, (Var.colorSelect if Var.challenge[5] else Var.colorUnselect), (225, 375, 150, 50))
        textChallenge = font.render('Challenge:', True, (0, 0, 0))
        challenge1 = font.render('Landmine', True, (255, 255, 255))
        challenge2 = font.render('Blackout', True, (255, 255, 255))
        challenge3 = font.render(Var.text_poison, True, (255, 255, 255))
        challenge4 = font.render('Motion', True, (255, 255, 255))
        challenge5 = font.render('Reversal', True, (255, 255, 255))
        Var.screen.blit(textChallenge, (30, 270))
        Var.screen.blit(challenge1, (53, 322))    
        Var.screen.blit(challenge2, (240, 322)) 
        Var.screen.blit(challenge3, Var.text_poison_position)
        Var.screen.blit(challenge4, (73, 387))
        Var.screen.blit(challenge5, (240, 387))
        font = pygame.font.Font('freesansbold.ttf', 17)
        textRule = font.render(Var.rule, True, (0, 0, 0))
        Var.screen.blit(textRule, (50, 436))

       
    def page2():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Var.running = False
                Var.retry = False
                Var.settings = False

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
                    Var.running = False
                    Var.retry = False
                    Var.settings = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if (504 < event.pos[0] < 592) and (0 < event.pos[1] < 50):
                    Var.settings_page += 1
                    Music.click()
                if (417 < event.pos[0] <= 504) and (0 < event.pos[1] < 50):
                    Var.settings_page -= 1
                    Music.click()
                Var.settings_page = (Var.settings_page - 1) % 3 + 1

                if (395 < event.pos[0] < 445) and (351 < event.pos[1] < 422):
                    Var.snake_skin += 1
                    Var.snake_skin = Var.snake_skin % len(Var.image_folder)
                    if Var.snake_skin == 0:
                        Var.snake_rgb_visits += 1
                        if random.randint(1, 5) == 1 and Var.snake_rgb_visits > 3:
                            Var.snake_rgb = not Var.snake_rgb
                    Music.click()
                if (153 < event.pos[0] < 204) and (351 < event.pos[1] < 422):
                    Var.snake_skin -= 1
                    Var.snake_skin = Var.snake_skin % len(Var.image_folder)
                    if Var.snake_skin == 0:
                        Var.snake_rgb_visits += 1
                        if random.randint(1, 5) == 1 and Var.snake_rgb_visits > 3:
                            Var.snake_rgb = not Var.snake_rgb
                    Music.click()
                #PLAY
                if (0 < event.pos[0] - Var.SCREEN_WIDTH/2 + 50 < 100) and (0 < event.pos[1] - Var.SCREEN_HEIGHT*6/7 < 40):
                    Var.settings = False
                    Var.running = True
                    Var.colorPlay = (123,116,108)
                    Music.click()
            
            if event.type == pygame.MOUSEMOTION:
                if (0 < event.pos[0] - Var.SCREEN_WIDTH/2 + 50 < 100) and (0 < event.pos[1] - Var.SCREEN_HEIGHT*6/7 < 40):
                    Var.colorPlay = (255, 0, 0)
                else:
                    Var.colorPlay = (123,116,108)

        font = pygame.font.Font('freesansbold.ttf', 30)
        Var.screen.blit(font.render('< 2 / 3 >', True, (255, 255, 255)), (Var.SCREEN_WIDTH - 142, 10))

        textBoard = font.render('Board Height:', True, (0, 0, 0))
        Var.screen.blit(textBoard, (30, 70))
        textBoard = font.render('Board Width:', True, (0, 0, 0))
        Var.screen.blit(textBoard, (30, 170))
        menu_board.run()
        Var.TILE_HEIGHT = int(menu_board.sliders[0].get_value())
        Var.TILE_WIDTH = int(menu_board.sliders[1].get_value())
        textSkin = font.render('Skin:', True, (0, 0, 0))
        Var.screen.blit(textSkin, (30, 270))
        sprite_skin = pygame.image.load(Utility.resource_path(f"Assets/Skin/{Var.snake_skin}.png"))
        Var.screen.blit(pygame.transform.scale(sprite_skin, (150, 200)), [225, 290])
        arrow_skin = pygame.image.load(Utility.resource_path(f"Assets/Skin/Arrow.png"))
        Var.screen.blit(pygame.transform.rotate(pygame.transform.scale(arrow_skin, (60, 60)), 180), [390, 360])
        Var.screen.blit(pygame.transform.rotate(pygame.transform.scale(arrow_skin, (60, 60)), 0), [150, 360])
        if Var.snake_skin == 0:
            if Var.snake_rgb:
                s = pygame.Surface((150, 200))  # the size of your rect
                s.set_alpha(70)                # alpha level
                s.fill(Utility.hsv_to_rgb((Var.snake_rgb_frame_counter % 360) / 360.0, 1, 1))         # this fills the entire surface
                Var.screen.blit(s, (225, 290))
    
    def page3():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Var.running = False
                Var.retry = False
                Var.settings = False

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
                    Var.running = False
                    Var.retry = False
                    Var.settings = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if (504 < event.pos[0] < 592) and (0 < event.pos[1] < 50):
                    Var.settings_page += 1
                    Music.click()
                if (417 < event.pos[0] <= 504) and (0 < event.pos[1] < 50):
                    Var.settings_page -= 1
                    Music.click()
                Var.settings_page = (Var.settings_page - 1) % 3 + 1

                if (150 < event.pos[0] < 300) and (187 < event.pos[1] < 237): 
                    Var.mute_music = not Var.mute_music
                    Music.click()
                if (270 < event.pos[0] < 420) and (287 < event.pos[1] < 337): 
                    Var.mute_sfx = not Var.mute_sfx
                    if not Var.mute_sfx:
                        Music.click()
                
                if (0 < event.pos[0] - Var.SCREEN_WIDTH/2 + 50 < 100) and (0 < event.pos[1] - Var.SCREEN_HEIGHT*6/7 < 40):
                    Var.settings = False
                    Var.running = True
                    Var.colorPlay = (123,116,108)
                    Music.click()

            if event.type == pygame.MOUSEMOTION:
                if (0 < event.pos[0] - Var.SCREEN_WIDTH/2 + 50 < 100) and (0 < event.pos[1] - Var.SCREEN_HEIGHT*6/7 < 40):
                    Var.colorPlay = (255, 0, 0)
                else:
                    Var.colorPlay = (123,116,108)

        font = pygame.font.Font('freesansbold.ttf', 30)
        Var.screen.blit(font.render('< 3 / 3 >', True, (255, 255, 255)), (Var.SCREEN_WIDTH - 142, 10))
        textVolume = font.render('Volume:', True, (0, 0, 0))
        Var.screen.blit(textVolume, (30, 70))
        volume_slider.run()
        Var.volume = volume_slider.sliders[0].get_value()
        Music.set_volume((0 if Var.mute_music else Var.volume/100), (0 if Var.mute_sfx else Var.volume/100))
        volume_slider_pause.sliders[0].update_value(Var.volume)

        textMusic = font.render('Music:', True, (0, 0, 0))
        Var.screen.blit(textMusic, (30, 198))
        pygame.draw.rect(Var.screen, (Var.colorUnselect if Var.mute_music else Var.colorSelect), (150, 187, 150, 50))
        music = font.render(("Off" if Var.mute_music else "On"), True, (255, 255, 255))
        Var.screen.blit(music, (200, 197))

        textSfx = font.render('Sound effects:', True, (0, 0, 0))
        Var.screen.blit(textSfx, (30, 298))
        pygame.draw.rect(Var.screen, (Var.colorUnselect if Var.mute_sfx else Var.colorSelect), (270, 287, 150, 50))
        sfx = font.render(("Off" if Var.mute_sfx else "On"), True, (255, 255, 255))
        Var.screen.blit(sfx, (320, 297))
        

    Var.highScore = 0
    Var.screen.fill((243,243,243))
    frame_interval = Var.fpsClock.tick(Var.FPS) / 16
    Var.snake_rgb_frame_counter += frame_interval * 2
    
    #Settings
    font = pygame.font.Font('freesansbold.ttf', 30)
    pygame.draw.rect(Var.screen, (5, 99, 5), (0, 0, Var.SCREEN_WIDTH, 50))
    textSetting = font.render('SETTINGS', True, (255, 255, 255))
    Var.screen.blit(textSetting, (10, 12))
    # pygame.draw.rect(Var.screen, (9, 62, 7), (Var.SCREEN_WIDTH - 240, 0, 120, 50))
    # pygame.draw.rect(Var.screen, (5, 99, 5), (Var.SCREEN_WIDTH - 120, 0, 120, 50))
    # pygame.draw.rect(Var.screen, (96,180,108), (Var.SCREEN_WIDTH - 125, 5, 120, 40))
    # pygame.draw.line(Var.screen, (0, 0, 0), (Var.SCREEN_WIDTH - 300, 0), (Var.SCREEN_WIDTH - 300, 48), width=3)
    # Var.screen.blit(font.render('Snake', True, (255, 255, 255)), (Var.SCREEN_WIDTH - 230, 10))
    # Var.screen.blit(font.render('Board', True, (255, 255, 255)), (Var.SCREEN_WIDTH - 105, 10))
        # Play Button
    font = pygame.font.Font('freesansbold.ttf', 30)
    pygame.draw.rect(Var.screen, Var.colorPlay, (Var.SCREEN_WIDTH/2 - 50, Var.SCREEN_HEIGHT*6/7, 100, 40))
    textPlay = font.render('PLAY', True, (255, 255, 255))
    Var.screen.blit(textPlay, (Var.SCREEN_WIDTH/2 - 40, Var.SCREEN_HEIGHT*6/7 + 7))

    if Var.settings_page == 1:
        page1()
    elif Var.settings_page == 2: # second page
        page2()
    else:
        page3()
    
    if (not (Var.TILE_HEIGHT == 4 and Var.TILE_WIDTH == 20)) and (not (Var.TILE_HEIGHT == 6 and Var.TILE_WIDTH == 9)) and (not (Var.TILE_HEIGHT == 5 and Var.TILE_WIDTH == 30)) and Var.scroll_x_page_2 <= Var.scroll_off:
        Var.scrolled_page_2 = False
    if ((Var.TILE_HEIGHT == 4 and Var.TILE_WIDTH == 20) or (Var.TILE_HEIGHT == 6 and Var.TILE_WIDTH == 9) or (Var.TILE_HEIGHT == 5 and Var.TILE_WIDTH == 30)) and not Var.scrolled_page_2:
        Var.scroll_x_page_2 = 1000
        Var.scrolled_page_2 = True
    if (not (Var.TILE_HEIGHT == 4 and Var.TILE_WIDTH == 20)) and (not (Var.TILE_HEIGHT == 6 and Var.TILE_WIDTH == 9)) and (not (Var.TILE_HEIGHT == 5 and Var.TILE_WIDTH == 30)):
        Var.scroll_x_page_2 = Var.scroll_off
        Var.scrolled_page_2 = False

    if (not int(Var.volume) == 69) and Var.scroll_x_page_3 <= Var.scroll_off:
        Var.scrolled_page_3 = False
    if int(Var.volume) == 69 and not Var.scrolled_page_3:
        Var.scroll_x_page_3 = 1000
        Var.scrolled_page_3 = True
    if not int(Var.volume) == 69:
        Var.scroll_x_page_3 = Var.scroll_off
        Var.scrolled_page_3 = False

    if Var.scroll_x_page_2 > Var.scroll_off:
        font = pygame.font.Font('freesansbold.ttf', 100)
        textNice = font.render('NICEEEEEEEEEEEEEEEEEEEEEEE', True, (0, 0, 0))
        Var.screen.blit(textNice, (Var.scroll_x_page_2, Var.SCREEN_HEIGHT/2))
        Var.scroll_x_page_2 -= 20
    
    if Var.scroll_x_page_3 > Var.scroll_off:
        font = pygame.font.Font('freesansbold.ttf', 100)
        textNice = font.render('NICEEEEEEEEEEEEEEEEEEEEEEE', True, (0, 0, 0))
        Var.screen.blit(textNice, (Var.scroll_x_page_3, Var.SCREEN_HEIGHT/2))
        Var.scroll_x_page_3 -= 20

    if Var.snake_epilepsy:
        s = pygame.Surface((600, 600))  # the size of your rect
        s.set_alpha(70)                # alpha level
        s.fill(Utility.hsv_to_rgb(((Var.snake_rgb_frame_counter * 2 + 180) % 360) / 360.0, 1, 1))         # this fills the entire surface
        Var.screen.blit(s, (0, 0))

    pygame.display.flip()
