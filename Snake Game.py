import pygame
import random
import Var
import Utility
import States.Settings as Settings
import States.Running as Running
import States.Retry as Retry
import States.Music as Music
import States.TitleScreen as TitleScreen
import time

# pygame.mixer_music.load("Assets/UnwelcomeSchool.opus")
# pygame.mixer_music.play(-1)
def init_():
    Var.dizzy = 0
    Var.applePoison = 0
    Var.appleDirection = 2  # random.randint(0, 3)
    Var.TILE_SIZE = min(500//(Var.TILE_HEIGHT + 3), 600//(Var.TILE_WIDTH + 3))
    # Var.SCREEN_WIDTH = (Var.TILE_WIDTH + 3) * Var.TILE_SIZE
    # Var.SCREEN_HEIGHT = (Var.TILE_HEIGHT + 3) * Var.TILE_SIZE + 120
    # print(Variables.SCREEN_WIDTH, Variables.SCREEN_HEIGHT)
    # Var.screen = pygame.display.set_mode((600, 600))
    Var.top_indent = (500 - Var.TILE_HEIGHT * Var.TILE_SIZE) // 2 - round(3/2 * Var.TILE_SIZE)
    Var.left_indent = (600 - Var.TILE_WIDTH * Var.TILE_SIZE) // 2 - round(3/2 * Var.TILE_SIZE)

    # print(Var.TILE_SIZE)
    Var.frame_counter = 0

    Var.snake_size = Var.TILE_SIZE
  
    Var.win_the_game = False
    Var.retry = False 

    Var.wrong_direction = 2
    Var.direction = 0
    Var.score = 0

    snake_init_x = Var.TILE_WIDTH//2
    snake_init_y = (Var.TILE_HEIGHT + 1) // 2
    if Var.TILE_WIDTH > 3:
        Var.snake_body = [[snake_init_x - i + 1, snake_init_y] for i in range(3)]
    else:
        Var.snake_body = [[3, snake_init_y], [2, snake_init_y], [1, snake_init_y]]

    # snake_init_x = 1
    # snake_init_y = 1
    # Var.snake_body = []

    # for i in range(0, 10):
    #     for j in range(0, 25):
    #         Var.snake_body.append([snake_init_x + j, snake_init_y + i * 2])
    #     if (i <= 8):
    #         for j in range(24, -1, -1):
    #             Var.snake_body.append([snake_init_x + j, snake_init_y + (i * 2 + 1)])

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
    
    Var.move_queue = []


    Utility.update_skin(Var.snake_skin)
    # Utility.skin_selection_maker()

    Var.mineList = []

    Var.radius_of_apple = Var.TILE_SIZE / 2
    Var.gamepause = False

    Var.bad_apple_frame_counter = 0
    Var.bad_apple_last_frame = -2

    Var.snake_rgb_frame_counter = 0
    Var.snake_rgb_last_frame = -2

    Var.music_frisk_index = random.randint(0, len(Var.music_frisk) - 1)
    Var.music_index = random.randint(0, len(Var.music_game) - 1)


Var.poison_streak_goal = random.randint(2, 5)
Music.initialize_music()


with open(Utility.resource_path("Assets/Bad Apple.txt"), "r") as f:
    Var.bad_apple_frame = f.read().split("a")
for i in range(len(Var.bad_apple_frame)):
    Var.bad_apple_frame[i] = Var.bad_apple_frame[i].split("\n")
    if Var.bad_apple_frame[i][0] == "":
        del Var.bad_apple_frame[i][0]
    if Var.bad_apple_frame[i][-1] == "":
        del Var.bad_apple_frame[i][-1]

Music.settings()

# pygame.mixer.Channel(0).play(pygame.mixer.Sound(Utility.resource_path(Var.music_settings)))

TitleScreen.initialize()
while Var.title_screen:
    TitleScreen.title_screen()

while Var.settings:
    Settings.settings()

while True:
    init_()
    Music.main_game()

    while Var.running:
        Running.running()
    if not Var.win_the_game:
        Var.loss += 1
    if (not Var.running) and (not Var.retry) and (not Var.settings):
        break
    if not Var.gamepause:
        Retry.render()
        while Var.retry:
            Retry.retry()
    if (not Var.running) and (not Var.retry) and (not Var.settings):
        break
    Music.settings()

    while Var.settings: 
        Settings.settings()
    
    if (not Var.running) and (not Var.retry) and (not Var.settings):
        break

Music.pause()

def jumpscare():
    
    # Set initial screen dimensions
    pygame.display.set_caption("S̸̡̛͇̣̫̏̇̃͒͑̾̔͊͋̊́̓̈́͐̿̃̀̐̂̈́͠͝͝͝n̴͔͖̈̃͌̋̐͊̍̑́̂͗̏a̴̡̡̨̢͍̩͕̣̱̘͙̫͈̝͇̩̞̥̭̳̞̣̒͜͜͝ͅk̸̤̙͙̣̇̓̇́̽͘͜͠ͅḙ̴̛̟̣̯̏̄́͛͗͌̆̀̋͋͆̃̑̈͊́̏̔̈́̔͗̕̕͠ ̵̢͙̦͔̝͖̹͕̤̱͍̙̩͙͎̩͓͑̍̑̾̐̅̆̉̓̇̌̀͆̉̈̈́͒̆̌͂̕͠͠͝Ģ̷̥͓̠̻̟̙̰̈͐̈́̋̾͐̍̀͋́̂̒̍͒͆̄̒͒̇̂̈́͘a̵̺̱̞̝͕̺̫̺̫̩̞̽̊͂̊̌̈́͆̍̋̆̄̿̋͒͛͐͑̕̕͝͠͠͠͝͝m̸̡̡̜̣̮͕̲̜̹̱̖̩̦̹̦͚͓̺̼̗̈́̀̈́̊̌̏̈́ẽ̴̢̯͈̗͍̭̞͔̗̠̞̬̾́̃͗̿̏̾̽͑̊͌̈́͗̈́̆̅̾̊̆̄̍̍̚̚̕̚͝͠͝")
    
    # Load image and sound (replace with actual file paths)
    jumpscare_img = [pygame.image.load(Utility.resource_path(f"Assets/Chara/Chara{i}.png")) for i in range(0, 3)]  # Replace with actual Chara jumpscare image
    nine_img = pygame.image.load(Utility.resource_path("Assets/Chara/Nine.png"))
    slice_img = [pygame.transform.scale_by(pygame.image.load(Utility.resource_path(f"Assets/Chara/Slice{i}.png")), 6) for i in range(0, 6)]
    jumpscare_sound = pygame.mixer.Sound(Utility.resource_path("Assets/Chara/Chara Jumpscare.mp3"))  # Replace with actual Chara jumpscare sound
    chara_slash = pygame.mixer.Sound(Utility.resource_path("Assets/Chara/Chara Slash.mp3"))
    chara_nine = pygame.mixer.Sound(Utility.resource_path("Assets/Chara/Nine.mp3"))
    
    # Play sound
    jumpscare_sound.play()
    
    start_size = 100  # Initial small size
    max_size = 400    # Final large size
    duration = 2      # Duration of the effect
    index = 0
    start_time = time.time()
    
    while time.time() - start_time < duration:
        elapsed = time.time() - start_time
        scale = int(start_size + (max_size - start_size) * (elapsed / duration))
        
        # Resize image
        resized_img = pygame.transform.scale(jumpscare_img[index % 3], (scale, scale * 30/19))
        
        # Flashing background effect
        if int(elapsed * 10) % 2 == 0:
            Var.screen.fill((255, 0, 0))  # Red flash
        else:
            Var.screen.fill((0, 0, 0))    # Black flash
        
        # Draw image at center
        img_x = (Var.SCREEN_WIDTH - scale) // 2 + random.randint(-scale//10, scale//10)
        img_y = (Var.SCREEN_HEIGHT - scale) // 2 + random.randint(-scale//10, scale//10)
        Var.screen.blit(resized_img, (img_x, img_y - 100))
        pygame.display.flip()
        
        time.sleep(0.05)
        index += 1
        for _ in pygame.event.get():
            pass

    chara_slash.play()
    for i in range(0, 6):
        img_x = (Var.SCREEN_WIDTH - scale) // 2 + 100
        img_y = (Var.SCREEN_HEIGHT - scale) // 2
        if i > 3:
            img_y += i * 50
        if i > 4:
            img_y += 80
        Var.screen.fill((0, 0, 0))    # Black flash
        Var.screen.blit(slice_img[i], (img_x, img_y))
        pygame.display.flip()
        time.sleep(0.5)
        for _ in pygame.event.get():
            pass
    Var.screen.fill((0, 0, 0))
    pygame.display.flip()
    time.sleep(1)
    chara_nine.play()
    start_time = time.time()
    while time.time() - start_time < 5:
        offset_x = random.randint(-5, 5)
        offset_y = random.randint(-5, 5)
        Var.screen.fill((0, 0, 0))
        for x in range(-5, Var.SCREEN_WIDTH, 35):
            for y in range(-5, Var.SCREEN_HEIGHT, 35):
                Var.screen.blit(nine_img, (x + offset_x, y + offset_y))
        pygame.display.flip()
        time.sleep(0.01)
        for _ in pygame.event.get():
            pass

    pygame.quit()


if Var.snake_skin == 3 and int(Var.volume) == 99 and Var.TILE_HEIGHT == 9 and Var.TILE_WIDTH == 9:
    jumpscare()
pygame.quit()
