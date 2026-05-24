import sys
import os
import pygame
import Var
import Render

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def update_skin(skin):
    Var.sprite_pause_button = pygame.image.load(resource_path(f"Assets/Pause.png"))
    if skin == 0:
        return
    Var.sprite_head = pygame.image.load(resource_path(f"Assets/{Var.image_folder[skin]}/Head.png")).convert_alpha()
    Var.sprite_body = pygame.image.load(resource_path(f"Assets/{Var.image_folder[skin]}/Body.png")).convert_alpha()
    Var.sprite_turn = pygame.image.load(resource_path(f"Assets/{Var.image_folder[skin]}/Turn.png")).convert_alpha()
    Var.sprite_tail = pygame.image.load(resource_path(f"Assets/{Var.image_folder[skin]}/Tail.png")).convert_alpha()
    Var.sprite_apple = pygame.image.load(resource_path(f"Assets/{Var.image_folder[skin]}/Apple.png")).convert_alpha()
    Var.sprite_bad_apple = pygame.image.load(resource_path(f"Assets/{Var.image_folder[skin]}/Bad_apple.png")).convert_alpha()
    
def hsv_to_rgb(h:float, s:float, v:float) -> tuple:
    if s:
        if h == 1.0:
            h = 0.0
        i = int(h * 6.0)
        f = h * 6.0 - i
        
        w = v * (1.0 - s)
        q = v * (1.0 - s * f)
        t = v * (1.0 - s * (1.0 - f))
        
        v *= 255
        w *= 255
        q *= 255
        t *= 255

        if i == 0: 
            return (v, t, w)
        if i == 1: 
            return (q, v, w)
        if i == 2: 
            return (w, v, t)
        if i == 3: 
            return (w, q, v)
        if i == 4: 
            return (t, w, v)
        if i == 5: 
            return (v, w, q)
    else: 
        v *= 255
        return (v, v, v)
    
def skin_selection_maker(): # set clip size to 6 x 5 then run this clip
    Var.TILE_HEIGHT = 3
    Var.TILE_WIDTH = 2
    Var.TILE_SIZE = min(500//(Var.TILE_HEIGHT + 5), 600//(Var.TILE_WIDTH + 4))
    Var.snake_body = [[1, 3], [1, 2], [1, 1], [2, 1]]
    Var.apple_x = 2
    Var.apple_y = 2
    Render.render_background()
    if Var.snake_skin > 0:
        Var.screen.blit(pygame.transform.scale(Var.sprite_bad_apple, (Var.TILE_SIZE, Var.TILE_SIZE)), [Var.left_indent + 2 * Var.TILE_SIZE + Var.TILE_SIZE/2, Var.top_indent + 3 * Var.TILE_SIZE + Var.TILE_SIZE/2])
    else:
        pygame.draw.rect(Var.screen, (133, 20, 220), [Var.left_indent + 2 * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.top_indent + 3 * Var.TILE_SIZE + Var.TILE_SIZE/2 + Var.TILE_SIZE/6, Var.TILE_SIZE - Var.TILE_SIZE/3, Var.TILE_SIZE - Var.TILE_SIZE/3], 0)


    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:                                
                    Var.running = False
                    Var.retry = False
                    Var.settings = False
