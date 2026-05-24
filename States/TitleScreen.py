import pygame
import Var
import States.Music as Music
import random
import Utility
import Render

def initialize():
    Var.TILE_HEIGHT = 20
    Var.TILE_WIDTH = 25
    Var.score = -3
    Var.TILE_SIZE = min(500//(Var.TILE_HEIGHT + 3), 600//(Var.TILE_WIDTH + 3))
    Var.top_indent = (500 - Var.TILE_HEIGHT * Var.TILE_SIZE) // 2 - round(3/2 * Var.TILE_SIZE)
    Var.left_indent = (600 - Var.TILE_WIDTH * Var.TILE_SIZE) // 2 - round(3/2 * Var.TILE_SIZE)
    snake_init_x = 1
    snake_init_y = 1
    Var.snake_body = []

    for i in range(0, 9):
        for j in range(0, 25):
            Var.snake_body.append([snake_init_x + j, snake_init_y + i * 2])
            Var.score += 1
        if (i <= 8):
            for j in range(24, -1, -1):
                Var.snake_body.append([snake_init_x + j, snake_init_y + (i * 2 + 1)])
                Var.score += 1
    i += 1
    Var.snake_body.append([snake_init_x + j, snake_init_y + i * 2])
    Var.apple_array = []
    Var.apple_x = 1
    while Var.apple_x <= Var.TILE_WIDTH:
        Var.apple_y = 1
        while Var.apple_y <= Var.TILE_HEIGHT:
            Var.apple_array.append([Var.apple_x, Var.apple_y])
            Var.apple_y += 1
        Var.apple_x += 1

    filter_apple = [apple for apple in Var.apple_array if apple not in Var.snake_body]

    apple = random.choice(filter_apple)

    Var.apple_x = Var.snake_body[-1][0]
    Var.apple_y = Var.snake_body[-1][1]

    for i in range(6, 0, -1):
        Var.apple_x = Var.snake_body[-1][0] - i
        if Var.apple_x > 1 and [Var.apple_x, Var.apple_y] not in Var.snake_body:
            break
    else:
        Var.apple_x = apple[0]
        Var.apple_y = apple[1]
    Utility.update_skin(Var.snake_skin)

    Render.render_background()

    s = pygame.Surface((Var.SCREEN_WIDTH, Var.SCREEN_HEIGHT - 100))  # the size of your rect
    s.set_alpha(50)                # alpha level
    s.fill((0, 0, 0))           # this fills the entire surface
    Var.screen.blit(s, (0, 0))
    Var.screen.blit(pygame.transform.gaussian_blur(Var.screen, 3), (0, 0))
    text_title_screen_x = Var.SCREEN_WIDTH / 2
    text_title_screen_y = Var.SCREEN_HEIGHT / 3 + 30

    font_title_screen = pygame.font.Font('freesansbold.ttf', 50)

    text_title_screen = font_title_screen.render('SNAKE GAME', True, (255, 255, 255))

    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    margin = 3
    for i in range(8):
        text_title_screen = font_title_screen.render('SNAKE GAME', True, (0, 100, 0))
        textRect_title_screen = text_title_screen.get_rect()
        textRect_title_screen.center = (text_title_screen_x + dxy[i][0] * margin, text_title_screen_y + dxy[i][1] * margin)
        Var.screen.blit(text_title_screen, textRect_title_screen)

    text_title_screen = font_title_screen.render('SNAKE GAME', True, (255, 255, 255))
    textRect_title_screen = text_title_screen.get_rect()
    textRect_title_screen.center = (text_title_screen_x, text_title_screen_y)
    Var.screen.blit(text_title_screen, textRect_title_screen)
    pygame.draw.rect(Var.screen, (0, 140, 0), (Var.SCREEN_WIDTH/2 - 160, 280, 100, 40))
    pygame.draw.rect(Var.screen, (0, 140, 0), (Var.SCREEN_WIDTH/2 - 50, 280, 100, 40))
    pygame.draw.rect(Var.screen, (0, 140, 0), (Var.SCREEN_WIDTH/2 + 60, 280, 100, 40))

    font = pygame.font.Font('freesansbold.ttf', 20)
    option1 = font.render('Play', True, (255, 255, 255))
    option2 = font.render('Settings', True, (255, 255, 255))
    Var.screen.blit(option1, (Var.SCREEN_WIDTH/2 - 130, 290))
    Var.screen.blit(option2, (Var.SCREEN_WIDTH/2 - 41, 290))
    option3 = font.render('Quit', True, (255, 255, 255))
    Var.screen.blit(option3, (Var.SCREEN_WIDTH/2 + 88, 290))

    pygame.display.flip()


def title_screen():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 280 <= event.pos[1] <= 320:
                if Var.SCREEN_WIDTH/2 - 160 <= event.pos[0] <= Var.SCREEN_WIDTH/2 - 60:
                    Music.click()
                    Var.running = True
                    Var.retry = False
                    Var.title_screen = False
                    

                elif Var.SCREEN_WIDTH/2 - 50 <= event.pos[0] <= Var.SCREEN_WIDTH/2 + 50:
                    Music.click()
                    Var.settings = True
                    Var.running = True
                    Var.retry = False
                    Var.title_screen = False
                    
                elif Var.SCREEN_WIDTH/2 + 60 <= event.pos[0] <= Var.SCREEN_WIDTH/2 + 160:
                    Music.click()
                    Var.running = False
                    Var.retry = False
                    Var.title_screen = False

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
                Var.title_screen = False
        if event.type == pygame.QUIT:
            Var.running = False
            Var.retry = False
            Var.settings = False
            Var.title_screen = False
