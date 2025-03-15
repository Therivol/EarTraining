from util.Settings import Settings
from util.Input import Input
from util.Window import Window
from util.Scenes import Scenes
from util.Assets import Assets
# from util.Audio import Audio
from client.scene.Scene import Scene
from gui.element.Button import Button

from util.Note import Note
from util.Note import Interval
from util.Audio import Audio
from util.Time import Time

import random
import pygame as p


class Intervals(Scene):
    def __init__(self):
        super().__init__("INTERVALS")

        self.play_button = Button(p.Rect(Assets.position_by_percent((192, 64), Settings.get("RESOLUTION"), (0.5, 0.6)
                                                                    ), (192, 64)), "ui/button_1_idle.png", "ui/button_1_active.png")
        
        self.play_text = Assets.font_1.render("PLAY", True, (0, 0, 0))

        self.asc_button = Button(p.Rect(Assets.position_by_percent((192, 64), Settings.get("RESOLUTION"), (0.25, 0.8)
                                                                    ), (192, 64)), "ui/button_1_idle.png", "ui/button_1_active.png")
        
        self.asc_text = Assets.font_1.render("ASC", True, (0, 0, 0))
        self.des_text = Assets.font_1.render("DES", True, (0, 0, 0))
        self.asc_des_text = self.asc_text

        self.harm_button = Button(p.Rect(Assets.position_by_percent((192, 64), Settings.get("RESOLUTION"), (0.75, 0.8)
                                                                    ), (192, 64)), "ui/button_1_idle.png", "ui/button_1_active.png")
        
        self.harm_text = Assets.font_1.render("HARM", True, (0, 0, 0))
        self.int_text = Assets.font_1.render("INT", True, (0, 0, 0))
        self.harm_int_text = self.int_text
        
        self.playing = False
        self.showing = False
        self.harmonic = False
        self.last_play = 0
        self.pause_time = 1

        self.first_note = None
        self.interval = None

        self.current_text = ""
        self.text_object = None
        self.set_showing(False)
        
        self.random_intervals = Interval.perfect_intervals
        self.direction = 1

        self.new_interval()

    def awake(self):
       pass

    def update(self):
        if self.asc_button.update():
            self.direction *= -1
            if self.direction == 1:
                self.asc_des_text = self.asc_text
            else:
                self.asc_des_text = self.des_text

        if self.harm_button.update():
            self.harmonic = not self.harmonic
            if self.harmonic:
                self.harm_int_text = self.harm_text
            else:
                self.harm_int_text = self.int_text


        if (Input.get_key_down(p.K_SPACE) or self.play_button.update()) and not self.playing:
            self.play()

        if Input.get_key_down(p.K_RETURN):
            if self.showing:
                self.new_interval()
                self.play()
                self.set_showing(False)

            else:
                self.set_showing(True)
                

        if self.playing:
            self.last_play += Time.delta()
            if self.last_play > self.pause_time:
                self.last_play = 0
                self.play_interval()
                self.playing = False

        # if self.quit_button.update():
        #     Window.should_close = True

    def get_surface(self):
        surf = p.Surface((Settings.get("RESOLUTION")))
        surf.fill(p.Color(135, 135, 150))
        surf.blit(self.text_object, Assets.position_by_percent(self.text_object.get_size(), Settings.get("RESOLUTION"), (0.5, 0.3)))

        self.play_button.draw(surf)
        surf.blit(self.play_text, (Assets.position_by_percent(self.play_text.get_size(), self.play_button.rect.size, (0.5, 0.5),
                                                    base=self.play_button.rect.topleft)))
        
        self.asc_button.draw(surf)
        surf.blit(self.asc_des_text, (Assets.position_by_percent(self.asc_des_text.get_size(), self.asc_button.rect.size, (0.5, 0.5),
                                                    base=self.asc_button.rect.topleft)))
        
        self.harm_button.draw(surf)
        surf.blit(self.harm_int_text, (Assets.position_by_percent(self.harm_int_text.get_size(), self.harm_button.rect.size, (0.5, 0.5),
                                                    base=self.harm_button.rect.topleft)))

        return surf

    def enter(self):
        pass

    def play(self):
        self.playing = not self.harmonic

        self.first_note.play()

        if self.harmonic:
            self.play_interval()

    def new_interval(self):
        self.first_note = Note(random.choice(Note.note_naturals), 4)
        self.interval = random.choice(self.random_intervals)
                
    def play_interval(self):
        second_note = self.first_note.get_interval(self.interval * self.direction)
        second_note.play()
        self.current_text = Interval.get_name(self.interval)    

    def update_text(self, text: str):
        self.text_object = Assets.font_1.render(text, True, (0, 0, 0))

    def set_showing(self, showing: bool):
        self.showing = showing

        if showing:
            self.update_text(self.current_text)
        else:
            self.update_text("")





