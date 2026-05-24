import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
pygame.display.set_caption('Snake Game')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.SRCALPHA
image_folder = ["", "Default", "Bonesaw", "Frisk"]
sprite_head = None
sprite_body = None 
sprite_turn = None 
sprite_tail = None 
sprite_apple = None 
sprite_bad_apple = None 
sprite_pause_button = None
snake_skin = 1  # 0, 1, 2 or 3

music_settings = "Assets/Music/Menu (Full).mp3"
music_game = ["Assets/Music/Ascension to Heaven.opus", "Assets/Music/Freedom Dive.opus", "Assets/Music/Nhelv.opus", "Assets/Music/Unwelcome School.opus", "Assets/Music/Hopes And Dreams.mp3"]
music_frisk = ["Assets/Music/Hopes And Dreams.mp3", "Assets/Music/Death By Glamour.mp3", "Assets/Music/BAATH.mp3"]
music_bad_apple = "Assets/Music/Bad Apple.mp3"
music_death = "Assets/Music/Death.mp3"
music_game_over = "Assets/Music/Determination.mp3"
music_rick_roll = "Assets/Music/Rick Roll.mp3"
music_win = "Assets/Music/Win.mp3"
music_click = "Assets/Music/Button Click.mp3"
music_apple_eat = "Assets/Music/Apple Eating.mp3"

music_frisk_index = 0
music_index = 0

# customizable
TILE_WIDTH = 25
TILE_HEIGHT = 20
TILE_SIZE = min(500//(TILE_HEIGHT + 3), 600//(TILE_WIDTH + 3))//3 * 3

wrong_direction = 2
direction = 0

snake_size = TILE_SIZE

FPS = 120
fpsClock = pygame.time.Clock()

speed = 10

highScore = 0

title_screen = True
running = True
settings = False
retry = True

score = 0

dizzy = 0 # Challenge mode Bad Apple
applePoison = 0
apple_x = 0
apple_y = 0
appleDirection = 0
radius_of_apple = 0

mineList = []

move_queue = []

desc = "Standard snake game"
rule = ""
Mode = 0

colorUnselect = (152,251,152)
colorSelect = (96,180,108)

colorPlay = (123,116,108)

settings_page = 1
challenge = [0, 0, 0, 0, 0, 0]
text_poison = "Poison"
text_poison_position = (432, 322)

frame_counter = 0
gamepause = False

snake_body = []
apple_array = []

top_indent = 0
left_indent = 0

win_the_game = False

bad_apple_frame_counter = 0
bad_apple_frame = None
bad_apple_last_frame = -1
bad_apple = False
poison_streak = 0
poison_streak_goal = 0
loss = 0

snake_red = 255
snake_green = 0
snake_blue = 0
snake_rgb_frame_counter = 0
snake_rgb_last_frame = -2
snake_rgb = False
snake_rgb_visits = 0
snake_epilepsy = False

history_keys_pressed = [-1 for _ in range(10)]
snake_rgb_key_code = [1073741906, 1073741906, 1073741905, 1073741905, 1073741904, 1073741903, 1073741904, 1073741903, 98, 97]

sound_death = None
sound_click = None
sound_apple_eat = None

mute_music = False
mute_sfx = False
volume = 50

scrolled_page_2 = False
scrolled_page_3 = False

scroll_off = -2000
scroll_x_page_2 = scroll_off
scroll_x_page_3 = scroll_off