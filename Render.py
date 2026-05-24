import pygame
import Var
import Utility

def render_background():
    # Draw background
    Var.screen.fill((255, 255, 255))
    borderColor = [[(0, 102, 0), (50, 205, 50)], [(0, 102, 0), (50, 205, 50)], [(21, 83, 110), (66, 185, 235)], [(0, 102, 0), (50, 205, 50)]]
    secondBorderColor = [[(38, 140, 38), (127, 255, 0)], [(38, 140, 38), (127, 255, 0)], [(32, 116, 153), (173, 249, 255)], [(38, 140, 38), (127, 255, 0)]]
    background_color = [[(144, 238, 144), (152, 251, 152)], [(144, 238, 144), (152, 251, 152)], [(191, 217, 242), (225, 237, 247)], [(144, 238, 144), (152, 251, 152)]]

    pygame.draw.rect(Var.screen, borderColor[Var.snake_skin][Var.Mode], [0, 0, Var.SCREEN_WIDTH, Var.SCREEN_HEIGHT - 100], 0)
    pygame.draw.rect(Var.screen, secondBorderColor[Var.snake_skin][Var.Mode], [Var.left_indent + Var.TILE_SIZE * 2/3, Var.top_indent + Var.TILE_SIZE * 2/3, Var.left_indent + Var.TILE_SIZE * 5/3 + Var.TILE_SIZE * Var.TILE_WIDTH, Var.top_indent + Var.TILE_SIZE * 5/3 + Var.TILE_SIZE * Var.TILE_HEIGHT], 0)
    for i in range (1, Var.TILE_HEIGHT + 1):
        for j in range (1, Var.TILE_WIDTH + 1):
            if not Var.snake_epilepsy:
                if (i + j) % 2 == 0:
                    pygame.draw.rect(Var.screen, background_color[Var.snake_skin][0], [Var.left_indent + Var.TILE_SIZE*j + Var.TILE_SIZE/2, Var.top_indent + Var.TILE_SIZE*i + Var.TILE_SIZE/2, Var.TILE_SIZE, Var.TILE_SIZE], 0)
                else:
                    pygame.draw.rect(Var.screen, background_color[Var.snake_skin][1], [Var.left_indent + Var.TILE_SIZE*j + Var.TILE_SIZE/2, Var.top_indent + Var.TILE_SIZE*i + Var.TILE_SIZE/2, Var.TILE_SIZE, Var.TILE_SIZE], 0)
            else:
                if (i + j) % 2 == 0:
                    pygame.draw.rect(Var.screen, Utility.hsv_to_rgb((int(((Var.TILE_HEIGHT - 1 - i) + (Var.TILE_WIDTH - 1 - j)) * 10 + Var.snake_rgb_frame_counter/2) % 360) / 360.0, 0.5, 1), [Var.left_indent + Var.TILE_SIZE*j + Var.TILE_SIZE/2, Var.top_indent + Var.TILE_SIZE*i + Var.TILE_SIZE/2, Var.TILE_SIZE, Var.TILE_SIZE], 0)
                else:
                    pygame.draw.rect(Var.screen, Utility.hsv_to_rgb((int(((Var.TILE_HEIGHT - 1 - i) + (Var.TILE_WIDTH - 1 - j)) * 10 + Var.snake_rgb_frame_counter/2) % 360) / 360.0, 0.3, 1), [Var.left_indent + Var.TILE_SIZE*j + Var.TILE_SIZE/2, Var.top_indent + Var.TILE_SIZE*i + Var.TILE_SIZE/2, Var.TILE_SIZE, Var.TILE_SIZE], 0)

    if Var.bad_apple:
        for i in range (1, Var.TILE_HEIGHT + 1):
            for j in range (1, Var.TILE_WIDTH + 1):
                black = 0
                white = 0
                for k in range (round(60/Var.TILE_HEIGHT * (i - 1)), round(60/Var.TILE_HEIGHT * i)):
                    for l in range (round(80/Var.TILE_WIDTH * (j - 1)), round(80/Var.TILE_WIDTH * j)):
                        # print(int(Var.bad_apple_frame_counter) % 6569, k, l)
                        if int(Var.bad_apple_frame[int(Var.bad_apple_frame_counter) % 6569][k][l]) == 0:
                            black += 1
                        else:
                            white += 1
                if black > white:
                    # pygame.draw.rect(Var.screen, (50, 50, 50, 100), [Var.left_indent + Var.TILE_SIZE*j + Var.TILE_SIZE/2, Var.top_indent + Var.TILE_SIZE*i + Var.TILE_SIZE/2, Var.TILE_SIZE, Var.TILE_SIZE], 0)
                    s = pygame.Surface((Var.TILE_SIZE, Var.TILE_SIZE))  # the size of your rect
                    s.set_alpha(50)                # alpha level
                    s.fill((0, 0, 0))           # this fills the entire surface
                    Var.screen.blit(s, (Var.left_indent + Var.TILE_SIZE*j + Var.TILE_SIZE/2, Var.top_indent + Var.TILE_SIZE*i + Var.TILE_SIZE/2))

    #sDraw landmines
    if Var.challenge[1] == 1:
        for k in Var.mineList:
            i = k[0]
            j = k[1]
            pygame.draw.rect(Var.screen, (255, 204, 0), [Var.left_indent + Var.TILE_SIZE*i + Var.TILE_SIZE/2, Var.top_indent + Var.TILE_SIZE*j + Var.TILE_SIZE/2, Var.TILE_SIZE, Var.TILE_SIZE], 0)

    # Drawing Body
    # Var.snake_body.insert(0, last_position)
    if Var.snake_skin > 0:
        if Var.TILE_SIZE < 20:
            for part_of_snake_body in range(0, len(Var.snake_body) - 1):
                # pygame.draw.rect(Var.screen, (46, 139, 87), [Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/3, Var.TILE_SIZE - Var.TILE_SIZE/3], 0)
                if (Var.snake_body[part_of_snake_body + 1][1] + 1) % (Var.TILE_HEIGHT + 2) == Var.snake_body[part_of_snake_body][1]:
                    if Var.snake_body[max(0, part_of_snake_body - 1)][1] == (Var.snake_body[part_of_snake_body][1] + 1) % (Var.TILE_HEIGHT + 2):
                        Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_body, 0), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    elif Var.snake_body[max(0, part_of_snake_body - 1)][0] == (Var.snake_body[part_of_snake_body][0] + 1) % (Var.TILE_WIDTH + 2):
                        Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_turn, 90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    elif Var.snake_body[max(0, part_of_snake_body - 1)][0] == (Var.snake_body[part_of_snake_body][0] - 1) % (Var.TILE_WIDTH + 2):
                        Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_turn, 180), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    else:
                        Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_tail, 0), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))



                if (Var.snake_body[part_of_snake_body + 1][1] - 1) % (Var.TILE_HEIGHT + 2) == Var.snake_body[part_of_snake_body][1]:
                    if Var.snake_body[max(0, part_of_snake_body - 1)][1] == (Var.snake_body[part_of_snake_body][1] - 1) % (Var.TILE_HEIGHT + 2):
                        Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_body, 180), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    elif Var.snake_body[max(0, part_of_snake_body - 1)][0] == (Var.snake_body[part_of_snake_body][0] + 1) % (Var.TILE_WIDTH + 2):
                        Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_turn, 0), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    elif Var.snake_body[max(0, part_of_snake_body - 1)][0] == (Var.snake_body[part_of_snake_body][0] - 1) % (Var.TILE_WIDTH + 2):
                        Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_turn, -90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    else:
                        Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_tail, 180), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))


                if (Var.snake_body[part_of_snake_body + 1][0] - 1) % (Var.TILE_WIDTH + 2) == Var.snake_body[part_of_snake_body][0]:
                    if Var.snake_body[max(0, part_of_snake_body - 1)][0] == (Var.snake_body[part_of_snake_body][0] - 1) % (Var.TILE_WIDTH + 2):
                        Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_body, -90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    elif Var.snake_body[max(0, part_of_snake_body - 1)][1] == (Var.snake_body[part_of_snake_body][1] + 1) % (Var.TILE_HEIGHT + 2):
                        Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_turn, 0), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    elif Var.snake_body[max(0, part_of_snake_body - 1)][1] == (Var.snake_body[part_of_snake_body][1] - 1) % (Var.TILE_HEIGHT + 2):
                        Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_turn, 90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    else:
                        Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_tail, -90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))

                if (Var.snake_body[part_of_snake_body + 1][0] + 1) % (Var.TILE_WIDTH + 2) == Var.snake_body[part_of_snake_body][0]:
                    if Var.snake_body[max(0, part_of_snake_body - 1)][0] == (Var.snake_body[part_of_snake_body][0] + 1) % (Var.TILE_WIDTH + 2):
                        Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_body, 90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    elif Var.snake_body[max(0, part_of_snake_body - 1)][1] == (Var.snake_body[part_of_snake_body][1] + 1) % (Var.TILE_HEIGHT + 2):
                        Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_turn, -90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    elif Var.snake_body[max(0, part_of_snake_body - 1)][1] == (Var.snake_body[part_of_snake_body][1] - 1) % (Var.TILE_HEIGHT + 2):
                        Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_turn, 180), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    else:
                        Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_tail, 90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))


            # Drawing Head
            if (Var.snake_body[-2][1] + 1) % (Var.TILE_HEIGHT + 2) == Var.snake_body[-1][1]:
                Var.screen.blit(pygame.transform.smoothscale(Var.sprite_head, (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[-1][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[-1][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))

            if (Var.snake_body[-2][1] - 1) % (Var.TILE_HEIGHT + 2) == Var.snake_body[-1][1]:
                Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_head, 180), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[-1][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[-1][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))

            if (Var.snake_body[-2][0] + 1) % (Var.TILE_WIDTH + 2) == Var.snake_body[-1][0]:
                Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_head, 90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[-1][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[-1][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))

            if (Var.snake_body[-2][0] - 1) % (Var.TILE_WIDTH + 2) == Var.snake_body[-1][0]:
                Var.screen.blit(pygame.transform.smoothscale(pygame.transform.rotate(Var.sprite_head, -90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[-1][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[-1][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
        else:
            for part_of_snake_body in range(0, len(Var.snake_body) - 1):
            # pygame.draw.rect(Var.screen, (46, 139, 87), [Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/3, Var.TILE_SIZE - Var.TILE_SIZE/3], 0)
                if (Var.snake_body[part_of_snake_body + 1][1] + 1) % (Var.TILE_HEIGHT + 2) == Var.snake_body[part_of_snake_body][1]:
                    if Var.snake_body[max(0, part_of_snake_body - 1)][1] == (Var.snake_body[part_of_snake_body][1] + 1) % (Var.TILE_HEIGHT + 2):
                        Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_body, 0), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    elif Var.snake_body[max(0, part_of_snake_body - 1)][0] == (Var.snake_body[part_of_snake_body][0] + 1) % (Var.TILE_WIDTH + 2):
                        Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_turn, 90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    elif Var.snake_body[max(0, part_of_snake_body - 1)][0] == (Var.snake_body[part_of_snake_body][0] - 1) % (Var.TILE_WIDTH + 2):
                        Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_turn, 180), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    else:
                        Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_tail, 0), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))



                if (Var.snake_body[part_of_snake_body + 1][1] - 1) % (Var.TILE_HEIGHT + 2) == Var.snake_body[part_of_snake_body][1]:
                    if Var.snake_body[max(0, part_of_snake_body - 1)][1] == (Var.snake_body[part_of_snake_body][1] - 1) % (Var.TILE_HEIGHT + 2):
                        Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_body, 180), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    elif Var.snake_body[max(0, part_of_snake_body - 1)][0] == (Var.snake_body[part_of_snake_body][0] + 1) % (Var.TILE_WIDTH + 2):
                        Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_turn, 0), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    elif Var.snake_body[max(0, part_of_snake_body - 1)][0] == (Var.snake_body[part_of_snake_body][0] - 1) % (Var.TILE_WIDTH + 2):
                        Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_turn, -90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    else:
                        Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_tail, 180), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))


                if (Var.snake_body[part_of_snake_body + 1][0] - 1) % (Var.TILE_WIDTH + 2) == Var.snake_body[part_of_snake_body][0]:
                    if Var.snake_body[max(0, part_of_snake_body - 1)][0] == (Var.snake_body[part_of_snake_body][0] - 1) % (Var.TILE_WIDTH + 2):
                        Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_body, -90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    elif Var.snake_body[max(0, part_of_snake_body - 1)][1] == (Var.snake_body[part_of_snake_body][1] + 1) % (Var.TILE_HEIGHT + 2):
                        Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_turn, 0), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    elif Var.snake_body[max(0, part_of_snake_body - 1)][1] == (Var.snake_body[part_of_snake_body][1] - 1) % (Var.TILE_HEIGHT + 2):
                        Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_turn, 90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    else:
                        Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_tail, -90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))

                if (Var.snake_body[part_of_snake_body + 1][0] + 1) % (Var.TILE_WIDTH + 2) == Var.snake_body[part_of_snake_body][0]:
                    if Var.snake_body[max(0, part_of_snake_body - 1)][0] == (Var.snake_body[part_of_snake_body][0] + 1) % (Var.TILE_WIDTH + 2):
                        Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_body, 90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    elif Var.snake_body[max(0, part_of_snake_body - 1)][1] == (Var.snake_body[part_of_snake_body][1] + 1) % (Var.TILE_HEIGHT + 2):
                        Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_turn, -90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    elif Var.snake_body[max(0, part_of_snake_body - 1)][1] == (Var.snake_body[part_of_snake_body][1] - 1) % (Var.TILE_HEIGHT + 2):
                        Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_turn, 180), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))
                    else:
                        Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_tail, 90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))


            # Drawing Head
            if (Var.snake_body[-2][1] + 1) % (Var.TILE_HEIGHT + 2) == Var.snake_body[-1][1]:
                Var.screen.blit(pygame.transform.scale(Var.sprite_head, (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[-1][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[-1][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))

            if (Var.snake_body[-2][1] - 1) % (Var.TILE_HEIGHT + 2) == Var.snake_body[-1][1]:
                Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_head, 180), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[-1][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[-1][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))

            if (Var.snake_body[-2][0] + 1) % (Var.TILE_WIDTH + 2) == Var.snake_body[-1][0]:
                Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_head, 90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[-1][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[-1][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))

            if (Var.snake_body[-2][0] - 1) % (Var.TILE_WIDTH + 2) == Var.snake_body[-1][0]:
                Var.screen.blit(pygame.transform.scale(pygame.transform.rotate(Var.sprite_head, -90), (Var.TILE_SIZE, Var.TILE_SIZE)), (Var.left_indent + Var.snake_body[-1][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[-1][1] * Var.TILE_SIZE + Var.TILE_SIZE/2))

    else:
        # Plain Snake Drawing Code (Legacy)
        
        # Drawing Body
        for part_of_snake_body in range(len(Var.snake_body) - 1):
            if Var.snake_rgb:
                snake_body_color = Utility.hsv_to_rgb((int((len(Var.snake_body) - part_of_snake_body - 1) * 10 + Var.snake_rgb_frame_counter) % 360) / 360.0, 1, 1)
            else:
                snake_body_color = (46, 139, 87)
            pygame.draw.rect(Var.screen, snake_body_color, [Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/3, Var.TILE_SIZE - Var.TILE_SIZE/3], 0)
            if Var.snake_body[part_of_snake_body + 1][1] + 1 == Var.snake_body[part_of_snake_body][1] or Var.snake_body[max(0, part_of_snake_body - 1)][1] + 1 == Var.snake_body[part_of_snake_body][1]:
                pygame.draw.rect(Var.screen, snake_body_color, [Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 - Var.TILE_SIZE/10, Var.TILE_SIZE - Var.TILE_SIZE/3, Var.TILE_SIZE - Var.TILE_SIZE/6 + Var.TILE_SIZE/10], 0)

            if Var.snake_body[part_of_snake_body + 1][1] - 1 == Var.snake_body[part_of_snake_body][1] or Var.snake_body[max(0, part_of_snake_body - 1)][1] - 1 == Var.snake_body[part_of_snake_body][1]:
                pygame.draw.rect(Var.screen, snake_body_color, [Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6 + Var.TILE_SIZE/10, Var.TILE_SIZE - Var.TILE_SIZE/3, Var.TILE_SIZE - Var.TILE_SIZE/6 + Var.TILE_SIZE/10], 0)

            if Var.snake_body[part_of_snake_body + 1][0] + 1 == Var.snake_body[part_of_snake_body][0] or Var.snake_body[max(0, part_of_snake_body - 1)][0] + 1 == Var.snake_body[part_of_snake_body][0]:
                pygame.draw.rect(Var.screen, snake_body_color, [Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 - Var.TILE_SIZE/10, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/6 + Var.TILE_SIZE/10, Var.TILE_SIZE - Var.TILE_SIZE/3], 0)

            if Var.snake_body[part_of_snake_body + 1][0] - 1 == Var.snake_body[part_of_snake_body][0] or Var.snake_body[max(0, part_of_snake_body - 1)][0] - 1 == Var.snake_body[part_of_snake_body][0]:
                pygame.draw.rect(Var.screen, snake_body_color, [Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6 + Var.TILE_SIZE/10, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/6 + Var.TILE_SIZE/10, Var.TILE_SIZE - Var.TILE_SIZE/3], 0)
            
        pygame.draw.rect(Var.screen, (0, 100, 0), [Var.left_indent + Var.snake_body[-1][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.top_indent + Var.snake_body[-1][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/3, Var.TILE_SIZE - Var.TILE_SIZE/3], 0)

        # Drawing Head
        if Var.snake_body[-2][1] + 1 == Var.snake_body[-1][1]:
            pygame.draw.rect(Var.screen, (0, 100, 0), [Var.left_indent + Var.snake_body[-1][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.top_indent + Var.snake_body[-1][1] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.TILE_SIZE - Var.TILE_SIZE/3, Var.TILE_SIZE - Var.TILE_SIZE/6], 0)

        if Var.snake_body[-2][1] - 1 == Var.snake_body[-1][1]:
            pygame.draw.rect(Var.screen, (0, 100, 0), [Var.left_indent + Var.snake_body[-1][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.top_indent + Var.snake_body[-1][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/3, Var.TILE_SIZE - Var.TILE_SIZE/6], 0)

        if Var.snake_body[-2][0] + 1 == Var.snake_body[-1][0]:
            pygame.draw.rect(Var.screen, (0, 100, 0), [Var.left_indent + Var.snake_body[-1][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[-1][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/3], 0)

        if Var.snake_body[-2][0] - 1 == Var.snake_body[-1][0]:
            pygame.draw.rect(Var.screen, (0, 100, 0), [Var.left_indent + Var.snake_body[-1][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.top_indent + Var.snake_body[-1][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/3], 0)

        
        # for part_of_snake_body in range(len(Var.snake_body) - 1):
        #     pygame.draw.rect(Var.screen, (46, 139, 87), [Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/3, Var.TILE_SIZE - Var.TILE_SIZE/3], 0)
        #     if Var.snake_body[part_of_snake_body + 1][1] + 1 == Var.snake_body[part_of_snake_body][1] or Var.snake_body[max(0, part_of_snake_body - 1)][1] + 1 == Var.snake_body[part_of_snake_body][1]:
        #         pygame.draw.rect(Var.screen, (46, 139, 87), [Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 - Var.TILE_SIZE/10, Var.TILE_SIZE - Var.TILE_SIZE/3, Var.TILE_SIZE - Var.TILE_SIZE/6 + Var.TILE_SIZE/10], 0)

        #     if Var.snake_body[part_of_snake_body + 1][1] - 1 == Var.snake_body[part_of_snake_body][1] or Var.snake_body[max(0, part_of_snake_body - 1)][1] - 1 == Var.snake_body[part_of_snake_body][1]:
        #         pygame.draw.rect(Var.screen, (46, 139, 87), [Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6 + Var.TILE_SIZE/10, Var.TILE_SIZE - Var.TILE_SIZE/3, Var.TILE_SIZE - Var.TILE_SIZE/6 + Var.TILE_SIZE/10], 0)

        #     if Var.snake_body[part_of_snake_body + 1][0] + 1 == Var.snake_body[part_of_snake_body][0] or Var.snake_body[max(0, part_of_snake_body - 1)][0] + 1 == Var.snake_body[part_of_snake_body][0]:
        #         pygame.draw.rect(Var.screen, (46, 139, 87), [Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 - Var.TILE_SIZE/10, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/6 + Var.TILE_SIZE/10, Var.TILE_SIZE - Var.TILE_SIZE/3], 0)

        #     if Var.snake_body[part_of_snake_body + 1][0] - 1 == Var.snake_body[part_of_snake_body][0] or Var.snake_body[max(0, part_of_snake_body - 1)][0] - 1 == Var.snake_body[part_of_snake_body][0]:
        #         pygame.draw.rect(Var.screen, (46, 139, 87), [Var.left_indent + Var.snake_body[part_of_snake_body][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6 + Var.TILE_SIZE/10, Var.top_indent + Var.snake_body[part_of_snake_body][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/6 + Var.TILE_SIZE/10, Var.TILE_SIZE - Var.TILE_SIZE/3], 0)
            
        # pygame.draw.rect(Var.screen, (0, 100, 0), [Var.left_indent + Var.snake_body[-1][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.top_indent + Var.snake_body[-1][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/3, Var.TILE_SIZE - Var.TILE_SIZE/3], 0)

        # # Drawing Head
        # if Var.snake_body[-2][1] + 1 == Var.snake_body[-1][1]:
        #     pygame.draw.rect(Var.screen, (0, 100, 0), [Var.left_indent + Var.snake_body[-1][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.top_indent + Var.snake_body[-1][1] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.TILE_SIZE - Var.TILE_SIZE/3, Var.TILE_SIZE - Var.TILE_SIZE/6], 0)

        # if Var.snake_body[-2][1] - 1 == Var.snake_body[-1][1]:
        #     pygame.draw.rect(Var.screen, (0, 100, 0), [Var.left_indent + Var.snake_body[-1][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.top_indent + Var.snake_body[-1][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/3, Var.TILE_SIZE - Var.TILE_SIZE/6], 0)

        # if Var.snake_body[-2][0] + 1 == Var.snake_body[-1][0]:
        #     pygame.draw.rect(Var.screen, (0, 100, 0), [Var.left_indent + Var.snake_body[-1][0] * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.snake_body[-1][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/3], 0)

        # if Var.snake_body[-2][0] - 1 == Var.snake_body[-1][0]:
        #     pygame.draw.rect(Var.screen, (0, 100, 0), [Var.left_indent + Var.snake_body[-1][0] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.top_indent + Var.snake_body[-1][1] * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/3], 0)

    # Drawing Apple

    if Var.snake_skin > 0:
        if Var.applePoison == 0: 
            if Var.TILE_SIZE < 20:
                Var.screen.blit(pygame.transform.smoothscale(Var.sprite_apple, (Var.TILE_SIZE, Var.TILE_SIZE)), [Var.left_indent + Var.apple_x * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.apple_y * Var.TILE_SIZE + Var.TILE_SIZE/2])
            else:
                Var.screen.blit(pygame.transform.scale(Var.sprite_apple, (Var.TILE_SIZE, Var.TILE_SIZE)), [Var.left_indent + Var.apple_x * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.apple_y * Var.TILE_SIZE + Var.TILE_SIZE/2])
        else:
            if Var.TILE_SIZE < 20:
                Var.screen.blit(pygame.transform.smoothscale(Var.sprite_bad_apple, (Var.TILE_SIZE, Var.TILE_SIZE)), [Var.left_indent + Var.apple_x * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.apple_y * Var.TILE_SIZE + Var.TILE_SIZE/2])
            else:
                Var.screen.blit(pygame.transform.smoothscale(Var.sprite_bad_apple, (Var.TILE_SIZE, Var.TILE_SIZE)), [Var.left_indent + Var.apple_x * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + Var.apple_y * Var.TILE_SIZE + Var.TILE_SIZE/2])
    else:
        appleColor = (220, 20, 60)
        if Var.applePoison:
            appleColor = (133, 20, 220)
        pygame.draw.rect(Var.screen, appleColor, [Var.left_indent + Var.apple_x * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.top_indent + Var.apple_y * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/3, Var.TILE_SIZE - Var.TILE_SIZE/3], 0)


    
    #Draw Shade (Challenge 2)
    if Var.challenge[2] == 1:
        pygame.draw.rect(Var.screen, (10, 10, 20), [Var.left_indent, Var.top_indent, (Var.snake_body[-1][0] - 5)*Var.TILE_SIZE + 3/2 * Var.TILE_SIZE, Var.SCREEN_HEIGHT - 100 - 4/3 * Var.TILE_SIZE], 0)
        pygame.draw.rect(Var.screen, (10, 10, 20), [Var.left_indent + (Var.snake_body[-1][0] + 5)*Var.TILE_SIZE + 2/5 * Var.TILE_SIZE, Var.top_indent, Var.SCREEN_WIDTH - (Var.snake_body[-1][0] + 5)*Var.TILE_SIZE - 1 * Var.TILE_SIZE, Var.SCREEN_HEIGHT - 100 - 4/3 * Var.TILE_SIZE], 0)
        pygame.draw.rect(Var.screen, (10, 10, 20), [Var.left_indent, Var.top_indent, Var.SCREEN_WIDTH - 4/3 * Var.TILE_SIZE, (Var.snake_body[-1][1] - 5)*Var.TILE_SIZE + 3/2 * Var.TILE_SIZE], 0)
        pygame.draw.rect(Var.screen, (10, 10, 20), [Var.left_indent, Var.top_indent + (Var.snake_body[-1][1] + 5)*Var.TILE_SIZE + 1/2 * Var.TILE_SIZE, Var.SCREEN_WIDTH - 4/3 * Var.TILE_SIZE, Var.SCREEN_HEIGHT - 100 - 2/3 * Var.TILE_SIZE - (Var.top_indent + (Var.snake_body[-1][1] + 5)*Var.TILE_SIZE + 1/2 * Var.TILE_SIZE)], 0)
    
    #Draw border
    pygame.draw.rect(Var.screen, borderColor[Var.snake_skin][Var.Mode], [0, 0, Var.SCREEN_WIDTH, Var.top_indent + Var.TILE_SIZE * 2/3], 0)
    pygame.draw.rect(Var.screen, borderColor[Var.snake_skin][Var.Mode], [0, 0, Var.left_indent + Var.TILE_SIZE * 2/3, Var.SCREEN_HEIGHT - 100], 0)
    pygame.draw.rect(Var.screen, borderColor[Var.snake_skin][Var.Mode], [0, Var.top_indent + Var.TILE_SIZE * 7/3 + Var.TILE_SIZE * Var.TILE_HEIGHT, Var.SCREEN_WIDTH, 500 - (Var.top_indent + Var.TILE_SIZE * 7/3 + Var.TILE_SIZE * Var.TILE_HEIGHT)], 0)
    pygame.draw.rect(Var.screen, borderColor[Var.snake_skin][Var.Mode], [Var.left_indent + Var.TILE_SIZE * 7/3 + Var.TILE_SIZE * Var.TILE_WIDTH, 0, Var.SCREEN_WIDTH, Var.SCREEN_HEIGHT - 100], 0)

    text_point_x = Var.SCREEN_WIDTH / 2
    text_point_y = 550
    font_point = pygame.font.Font('freesansbold.ttf', 30)
    text_point = font_point.render('POINT: ' + str(Var.score), True, (0, 0, 0))
    textRect_point = text_point.get_rect()  
    textRect_point.center = (text_point_x, text_point_y)
    Var.screen.blit(text_point, textRect_point)
    
    # volume_render()

    Var.screen.blit(pygame.transform.scale(Var.sprite_pause_button, (50, 50)), [Var.SCREEN_WIDTH - 80, Var.SCREEN_HEIGHT - 80])


    # pygame.display.flip()