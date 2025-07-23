
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
import time
import pygame as p



class ChordTransitions(Scene):
    def __init__(self):
        super().__init__("CHORD TRANSITIONS")
        
        self.current_text = None
        self.next_text = None
        self.timer_text = None
        
        self.chord_types = ["Em", "Em7", "E", "Am", "A", "G", "Gtype2", "G7", "F", "C", "Dm", "D", "E7", "A7", "Amaj7", 
                            "D7", "Dmaj7", "Cadd9", "F#m", "F#", "B", "Bm", "Bm7", "Bmaj7", "B7 (barre)", "B7", "Bmaj7"]
        
        self.current_chord = "NULL"
        self.next_chord = random.choice(self.chord_types)
        
        self.bpm = 80
        self.measure_length = 4
        self.delta_beat = 60 / self.bpm
        self.last_beat = time.time()
        
        self.current_beat = 0
        
        self.new_chord()
        self.update_time_text()
        
    def update(self):
        if (time.time() > self.last_beat + self.delta_beat):
            # next beat
            self.last_beat += self.delta_beat
            
            self.current_beat += 1
            if (self.current_beat + 1 > self.measure_length):
                self.current_beat = 0
                self.new_chord()
                
            self.update_time_text()
        
        
    def new_chord(self):
        self.current_chord = self.next_chord
        self.next_chord = random.choice(self.chord_types)
        
        self.update_chord_text()
        
        
    def get_surface(self):
        surf = p.Surface((Settings.get("RESOLUTION")))
        surf.fill(p.Color(135, 135, 150))
        surf.blit(self.timer_text, Assets.position_by_percent(self.timer_text.get_size(), Settings.get("RESOLUTION"), (0.5, 0.75)))
        surf.blit(self.current_text, Assets.position_by_percent(self.current_text.get_size(), Settings.get("RESOLUTION"), (0.5, 0.5)))
        surf.blit(self.next_text, Assets.position_by_percent(self.next_text.get_size(), Settings.get("RESOLUTION"), (0.5, 0.25)))


        return surf

        
    def update_chord_text(self):
        self.current_text = Assets.font_2.render(self.current_chord, True, (0, 0, 0))
        self.next_text = Assets.font_1.render("Next: " + self.next_chord, True, (0, 0, 0))
        
    def update_time_text(self):
        self.timer_text = Assets.font_1.render(str(self.current_beat + 1), True, (0, 0, 0))