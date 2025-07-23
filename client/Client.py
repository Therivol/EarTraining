import pygame as p

import sys

from util.Time import Time
from util.Input import Input
from util.Settings import Settings
from util.Scenes import Scenes
from util.Assets import Assets
from util.Window import Window

from client.scene.Intervals import Intervals
from client.scene.ChordID import Chords
from client.scene.ChordTransitions import ChordTransitions


class Client:
    def __init__(self):
        p.init()
        Time.awake()
        Settings.load()

        self.should_close = False

    def start(self):
        Window.display = p.display.set_mode(Settings.get("RESOLUTION"))
        p.display.set_caption(Settings.get("TITLE"))
        Window.resize(Settings.get("WINDOW SIZE"))

        Scenes.add_scene(Intervals())
        Scenes.add_scene(Chords())
        Scenes.add_scene(ChordTransitions())

        # Scenes.set_scene("INTERVALS")
        # Scenes.set_scene("CHORDS")
        Scenes.set_scene("CHORD TRANSITIONS")

    def poll_events(self):
        Input.update()

        for ev in p.event.get():
            if ev.type == p.QUIT or Window.should_close:
                self.should_close = True

    @staticmethod
    def start_frame():
        Time.start_frame()

    def update(self):
        Scenes.update()

    def draw(self):
        Window.draw()

    def quit(self):
        Settings.save()

        self.should_close = True
        p.quit()
        sys.exit()

    @staticmethod
    def calculate_dt():
        Time.calculate_dt()
