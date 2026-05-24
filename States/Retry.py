import pygame
import Var
import States.Music as Music

def render():
    Var.screen.blit(pygame.transform.gaussian_blur(Var.screen, 1), (0, 0))
    s = pygame.Surface((Var.SCREEN_WIDTH, Var.SCREEN_HEIGHT - 100))  # the size of your rect
    s.set_alpha(50)                # alpha level
    s.fill((0, 0, 0))           # this fills the entire surface
    Var.screen.blit(s, (0, 0))
    Var.highScore = max(Var.score, Var.highScore)
    font = pygame.font.Font('freesansbold.ttf', 25)
    text_highscore = font.render('Highest Point: ' + str(Var.highScore), True, (255, 255, 255))
    Var.screen.blit(text_highscore, (Var.SCREEN_WIDTH/2 - 100, Var.SCREEN_HEIGHT/2 - 40))
    if Var.win_the_game:
        Music.win()
        text_you_win_x = Var.SCREEN_WIDTH / 2
        text_you_win_y = Var.SCREEN_HEIGHT / 3 + 30
        font_you_win = pygame.font.Font('freesansbold.ttf', 50)
        text_you_win = font_you_win.render('YOU WIN', True, (255, 0, 0))
        textRect_you_win = text_you_win.get_rect()  
        textRect_you_win.center = (text_you_win_x, text_you_win_y)
        Var.screen.blit(text_you_win, textRect_you_win)

    else:
        Music.game_over()
        text_game_over_x = Var.SCREEN_WIDTH / 2
        text_game_over_y = Var.SCREEN_HEIGHT / 3 + 30
        font_game_over = pygame.font.Font('freesansbold.ttf', 50)
        text_game_over = font_game_over.render('GAME OVER', True, (255, 0, 0))
        textRect_game_over = text_game_over.get_rect()  
        textRect_game_over.center = (text_game_over_x, text_game_over_y)
        Var.screen.blit(text_game_over, textRect_game_over)
    
    pygame.draw.rect(Var.screen, (0, 140, 0), (Var.SCREEN_WIDTH/2 - 160, 300, 100, 40))
    pygame.draw.rect(Var.screen, (0, 140, 0), (Var.SCREEN_WIDTH/2 - 50, 300, 100, 40))
    pygame.draw.rect(Var.screen, (0, 140, 0), (Var.SCREEN_WIDTH/2 + 60, 300, 100, 40))

    font = pygame.font.Font('freesansbold.ttf', 20)
    option1 = font.render('Replay', True, (255, 255, 255))
    option2 = font.render('Settings', True, (255, 255, 255))
    Var.screen.blit(option1, (Var.SCREEN_WIDTH/2 - 143, 310))
    Var.screen.blit(option2, (Var.SCREEN_WIDTH/2 - 41, 310))
    option3 = font.render('Quit', True, (255, 255, 255))
    Var.screen.blit(option3, (Var.SCREEN_WIDTH/2 + 88, 310))

    pygame.display.flip()

def retry():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 0 < event.pos[1] - Var.SCREEN_HEIGHT/2 < 40:
                if (0 < event.pos[0] - Var.SCREEN_WIDTH/2 + 145 < 90):
                    Music.click()
                    Var.running = True
                    Var.retry = False
                    

                elif (0 < event.pos[0] - Var.SCREEN_WIDTH/2 + 45 < 90):
                    Music.click()
                    Var.settings = True
                    Var.running = True
                    Var.retry = False
                    
                elif (0 < event.pos[0] - Var.SCREEN_WIDTH/2 - 55 < 90):
                    Music.click()
                    Var.running = False
                    Var.retry = False

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
            if event.key == pygame.K_ESCAPE:                                
                Var.running = False
                Var.retry = False
                Var.settings = False
        if event.type == pygame.QUIT:
            Var.running = False
            Var.retry = False
            Var.settings = False

