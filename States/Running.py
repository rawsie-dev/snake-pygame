import pygame
import Render
import Var
import math
import Utility
import States.GamePause as GamePause
import States.EntitySpawn as EntitySpawn
import States.Music as Music


def running():
    if Var.gamepause:
        Render.render_background()
        GamePause.GamePause()
        pygame.display.flip()
        return
    if not pygame.mixer.music.get_busy() and not Var.bad_apple:
        if Var.snake_skin == 3:
            Var.music_frisk_index += 1
            Var.music_frisk_index = Var.music_frisk_index % len(Var.music_frisk)
            pygame.mixer_music.load(Utility.resource_path(Var.music_frisk[Var.music_frisk_index]))
            pygame.mixer_music.play()
        else:
            Var.music_index += 1
            Var.music_index = Var.music_index % len(Var.music_game)
            pygame.mixer_music.load(Utility.resource_path(Var.music_game[Var.music_index]))
            pygame.mixer_music.play()
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
                Var.running = False
                Var.retry = False
                Var.settings = False
            
            if Var.dizzy == 0:
                if event.key == pygame.K_UP or event.key == pygame.K_w:  
                    Var.move_queue.append(1)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:  
                    Var.move_queue.append(2)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:   
                    Var.move_queue.append(3)
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:   
                    Var.move_queue.append(4)

            else: # Challenge mode: Bad apple
                if event.key == pygame.K_UP or event.key == pygame.K_w: 
                    Var.move_queue.append(4)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                    Var.move_queue.append(3)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:  
                    Var.move_queue.append(2)
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:   
                    Var.move_queue.append(1)

            if event.key == pygame.K_p:
                GamePause.click_pause()
                return


        elif event.type == pygame.QUIT:
            Var.running = False
            Var.retry = False
            Var.settings = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            dist_x = event.pos[0] - (Var.SCREEN_WIDTH - 64)
            dist_y = event.pos[1] - (Var.SCREEN_WIDTH - 45)
            if math.hypot(dist_x, dist_y) <= 30:
                GamePause.click_pause()
                return
    

    #Variables.snake_body = [[snake_x + Variables.snake_size / 2, snake_y + Variables.snake_size / 2] for snake_x, snake_y in Variables.snake_body]
    
    # Variables.snake_body = [[snake_x - Variables.snake_size / 2, snake_y - Variables.snake_size / 2] for snake_x, snake_y in Variables.snake_body]

    frame_interval = Var.fpsClock.tick(Var.FPS) / 16

    Var.frame_counter += frame_interval

    if Var.bad_apple:
        if Var.bad_apple_last_frame == -2:
            Var.bad_apple_last_frame = -1
        else:
            Var.bad_apple_frame_counter += frame_interval / (25/12) # 2.085 - 2.083
        if int(Var.bad_apple_frame_counter) > Var.bad_apple_last_frame:
            Var.bad_apple_last_frame = Var.bad_apple_frame_counter
            Render.render_background()

    if Var.snake_rgb or Var.snake_epilepsy:
        if Var.snake_rgb_last_frame == -2:
            Var.snake_rgb_last_frame = -1
        else:
            Var.snake_rgb_frame_counter += frame_interval * 2
        if int(Var.snake_rgb_frame_counter) > Var.snake_rgb_last_frame:
            Var.snake_rgb_last_frame = Var.snake_rgb_frame_counter
            Render.render_background()

    # print(Var.snake_rgb_frame_counter)
    # pygame.draw.rect(Var.screen, (255, 255, 255), (20, 515, 213, 55))
    # volume_render()
    pygame.display.flip()

    Var.move_queue = Var.move_queue[0:3+1]
    if Var.frame_counter % Var.speed > frame_interval:
        return
    else:
        Var.frame_counter = 1
    
    if len(Var.move_queue) > 0:
        if Var.move_queue[0] == Var.wrong_direction:
            Var.move_queue = []
        else:
            Var.direction = Var.move_queue.pop(0)
            Var.wrong_direction = 5 - Var.direction

    if Var.direction == 1:
        Var.snake_body.append([Var.snake_body[-1][0], Var.snake_body[-1][1] - 1])

    elif Var.direction == 2:
        Var.snake_body.append([Var.snake_body[-1][0] + 1, Var.snake_body[-1][1]])

    elif Var.direction == 3:
        Var.snake_body.append([Var.snake_body[-1][0] - 1, Var.snake_body[-1][1]])

    elif Var.direction == 4:
        Var.snake_body.append([Var.snake_body[-1][0], Var.snake_body[-1][1] + 1])


    if Var.direction > 0:
        # if pygame.Rect(Var.snake_body[-1][0]*Var.TILE_SIZE, Var.snake_body[-1][1]*Var.TILE_SIZE, Var.TILE_SIZE, Var.TILE_SIZE).colliderect(pygame.Rect(Var.apple_x * Var.TILE_SIZE, Var.apple_y * Var.TILE_SIZE, Var.radius_of_apple * 2, Var.radius_of_apple * 2)):
        if (Var.snake_body[-1][0] == Var.apple_x and Var.snake_body[-1][1] == Var.apple_y) or (Var.challenge[4] == 1 and abs(Var.snake_body[-1][0] - Var.apple_x) <= 1 and abs(Var.snake_body[-1][1] - Var.apple_y) <= 1):
            Music.apple_eat()
            Var.score += 1
            if (Var.applePoison == 1): Var.dizzy = 1
            else: Var.dizzy = 0

            #Challenge Variables.Mode Reversal
            if Var.challenge[5] == 1:
                Var.snake_body = list(reversed(Var.snake_body))
                if Var.snake_body[-1][0] + 1 == Var.snake_body[-2][0]:
                    Var.direction = 3
                elif Var.snake_body[-1][0] - 1 == Var.snake_body[-2][0]:
                    Var.direction = 2
                elif Var.snake_body[-1][1] + 1 == Var.snake_body[-2][1]:
                    Var.direction = 1
                elif Var.snake_body[-1][1] - 1 == Var.snake_body[-2][1]:
                    Var.direction = 4
                Var.wrong_direction = 5 - Var.direction

            EntitySpawn.entitySpawn()
        else: 
            del Var.snake_body[0]

    if Var.Mode == 1:
        for part in range(len(Var.snake_body)):
            Var.snake_body[part][0] = Var.snake_body[part][0] % (Var.TILE_WIDTH + 2)
            Var.snake_body[part][1] = Var.snake_body[part][1] % (Var.TILE_HEIGHT + 2)
    else:
        if (Var.snake_body[-1][0] >= Var.TILE_WIDTH + 1) or (Var.snake_body[-1][0] <= 0)  or (Var.snake_body[-1][1] <= 0) or (Var.snake_body[-1][1] >= Var.TILE_HEIGHT + 1):
            Var.running = False
            Var.retry = True

    if len(Var.snake_body) >= 5:
        for part in range(len(Var.snake_body) - 1):
            if Var.snake_body[-1] == Var.snake_body[part]:
                Var.running = False
                Var.retry = True

    if Var.challenge[1] == 1:
        for k in Var.mineList:
            if Var.snake_body[-1] == k:
                Var.running = False
                Var.retry = True

    # Challenge Variables.Mode Moving
    if Var.challenge[4] == 1:
        # print(Var.appleDirection)
        if Var.apple_x <= 1: # Chạm tường trái
            Var.appleDirection = Var.appleDirection | 1

        if Var.apple_x >= Var.TILE_WIDTH: # Chạm tường phải
            Var.appleDirection = Var.appleDirection & 2

        if Var.apple_y <= 1: # Chạm trần
            Var.appleDirection = Var.appleDirection & 1

        if Var.apple_y >= Var.TILE_HEIGHT: # Chạm đáy 
            Var.appleDirection = Var.appleDirection | 2


        if Var.appleDirection & 2 == 0: # 0_
            Var.apple_y += 1
        if Var.appleDirection & 2: # 1_
            Var.apple_y -= 1
        if Var.appleDirection & 1: # _1
            Var.apple_x += 1
        if Var.appleDirection & 1 == 0: # _0
            Var.apple_x -= 1
        # else: Var.appleDirection = random.randint(0,3)

    Render.render_background()


    if Var.score >= Var.TILE_HEIGHT * Var.TILE_WIDTH - 3:
        Var.win_the_game = True
        Var.running = False
        Var.retry = True
        

