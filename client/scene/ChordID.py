
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

class Chords(Scene):
    def __init__(self):
        super().__init__("CHORDS")
        
        self.text_object = None
        self.showing = True
        
        self.current_text = "NULL"
        
        self.chord_types = ["major", "minor"]
        
        self.notes = []
        
        self.root = None
        self.set_showing(False)
        
        # self.new_chord()
        
    def enter(self):
        self.new_chord()
        
    def update(self):
        
        if (Input.get_key_down(p.K_SPACE)):
            self.play_current_chord()
        
        if (Input.get_key_down(p.K_RETURN)):
            self.showing = not self.showing
            
            if self.showing:
                self.play_root()
                self.set_showing(True)

            else:
                self.set_showing(False)
                self.new_chord()
                
                
    def get_surface(self):
        surf = p.Surface((Settings.get("RESOLUTION")))
        surf.fill(p.Color(135, 135, 150))
        surf.blit(self.text_object, Assets.position_by_percent(self.text_object.get_size(), Settings.get("RESOLUTION"), (0.5, 0.5)))


        return surf

        
    def update_text(self, text: str):
        self.text_object = Assets.font_1.render(text, True, (0, 0, 0))
        
    def set_showing(self, showing: bool):
        self.showing = showing

        if showing:
            self.update_text(self.current_text)
        else:
            self.update_text("")
            
    def new_chord(self):
        
        self.root = Note.by_degree(random.randint(0, 11), 4)
        
        chord_type = random.choice(self.chord_types)
        self.notes = [self.root.get_interval(interval) for interval in Interval.get_chord(chord_type)]
        
        # print(self.notes)
        
        self.current_text = self.root.name + " " + chord_type
        
        self.play_current_chord()
        
        
    def play_current_chord(self):
        for note in self.notes:
            note.play()
        
    def play_root(self):
        if (self.root):
            self.root.play()
        
