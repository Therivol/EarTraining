import pygame as p
from gui.element.UIElement import UIElement
from util.Input import Input
from util.Assets import Assets
# from util.Audio import Audio


class Button(UIElement):
    def __init__(self, rect, idle_surf, active_surf):
        super().__init__()
        self.rect = rect
        self.idle = idle_surf
        self.active = active_surf
        self.current_surf = idle_surf
        self.pressed = False

    def update(self):
        self.pressed = False
        if self.rect.collidepoint(Input.get_mouse_pos()):
            self.current_surf = self.active
            if Input.get_button_down(0):
                # Audio.play_sound("assets/sounds/basic.wav")
                self.pressed = True
        else:
            self.current_surf = self.idle

        return self.pressed

    def draw(self, surface):
        surface.blit(Assets.get_image(self.current_surf), self.rect.topleft)
