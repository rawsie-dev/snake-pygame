import pygame
import Var

class EventHandler:
    def __init__(self) -> None:
        EventHandler.events = pygame.event.get()
    def run():
        EventHandler.events = pygame.event.get()
    def clicked() -> bool:
        for e in EventHandler.events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                return True
        return False

UNSELECTED = (0, 100, 0)
SELECTED = "white"
BLACK = "black"
BUTTONSTATES = {
    True:SELECTED,
    False:UNSELECTED
}

class UI:
    @staticmethod
    def init(screen):
        UI.font = pygame.font.Font(None, 30)
        UI.sfont = pygame.font.Font(None, 20)
        UI.lfont = pygame.font.Font(None, 40)
        UI.xlfont = pygame.font.Font(None, 50)
        UI.center = (screen.get_size()[0]//2, screen.get_size()[1]//2)
        UI.half_width = screen.get_size()[0]//2
        UI.half_height = screen.get_size()[1]//2

        UI.fonts = {
            'sm':UI.sfont,
            'm':UI.font,
            'l':UI.lfont,
            'xl':UI.xlfont
        }

class Menu:
    def __init__(self, screen, sliders) -> None:
        self.screen = screen
        self.sliders = sliders

    def run(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()

        for slider in self.sliders:
            if slider.container_rect.collidepoint(mouse_pos):
                if mouse[0]:
                    slider.grabbed = True
            if not mouse[0]:
                slider.grabbed = False
            if slider.button_rect.collidepoint(mouse_pos):  
                slider.hover()
            if slider.grabbed:
                slider.move_slider(mouse_pos)
                slider.hover()
            else:
                slider.hovered = False
            slider.render(self.screen)
            slider.display_value(self.screen)
    

class Label:
    def __init__(self, font: str, content: str, pos: tuple, value = "blue", selected: bool = False) -> None:
        self.font = font
        self.selected = selected
        self.content = content

        self.value = value

        self.text = UI.fonts[self.font].render(content, True, (0, 0, 0), None)
        self.text_rect = self.text.get_rect(center = pos)
    def render(self, screen):
        screen.blit(self.text, self.text_rect)

        

class Slider:
    def __init__(self, pos: tuple, size: tuple, initial_val: float, min: int, max: int, volume = False, pause = False) -> None:
        self.pos = pos
        self.size = size
        self.hovered = False
        self.grabbed = False

        self.slider_left_pos = self.pos[0] - (size[0]//2)
        self.slider_right_pos = self.pos[0] + (size[0]//2)
        self.slider_top_pos = self.pos[1] - (size[1]//2)

        self.min = min
        self.max = max
        # self.initial_val = (self.slider_right_pos-self.slider_left_pos)*initial_val # <- percentage
        self.initial_val = initial_val
        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.slider_left_pos + (self.slider_right_pos-self.slider_left_pos)/(self.max - self.min)*(self.initial_val - self.min) + (-5 if volume else 0), self.slider_top_pos, 10, self.size[1])

        # label
        self.text = UI.fonts['l'].render(str(int(self.get_value())), True, (0, 0, 0), None)
        # self.label_rect = self.text.get_rect(center = (self.pos[0], self.slider_top_pos - 15))
        self.volume = volume
        self.label_rect = self.text.get_rect(center = (self.slider_left_pos + ((-25 if not volume else -40) if not pause else self.size[0] + 30), self.pos[1] + 2))

        
    def move_slider(self, mouse_pos):
        pos = mouse_pos[0]
        if pos < self.slider_left_pos:
            pos = self.slider_left_pos
        if pos > self.slider_right_pos:
            pos = self.slider_right_pos
        self.button_rect.centerx = pos
    def hover(self):
        self.hovered = True
    def render(self, screen):
        pygame.draw.rect(screen, "darkgray", self.container_rect)
        pygame.draw.rect(screen, BUTTONSTATES[self.hovered], self.button_rect)
    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        button_val = self.button_rect.centerx - self.slider_left_pos

        return (button_val/val_range)*(self.max-self.min)+self.min
    def display_value(self, screen):
        self.text = UI.fonts['l'].render(str(int(self.get_value())), True, ("black" if Var.settings else "white"), None)
        screen.blit(self.text, self.label_rect)

    def update_value(self, new_value):
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        self.button_rect.centerx = self.slider_left_pos + val_range/(self.max - self.min) * new_value









