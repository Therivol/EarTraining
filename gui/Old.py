import pygame as p
import sys

from util.Time import Time
from util.Input import Input
from util.Settings import Settings
from util.Scenes import Scenes
from util.Assets import Assets

from game.scene.MainMenu import MainMenu
from game.scene.LevelSelect import LevelSelect
from game.scene.LevelGeneral import Level
from game.scene.Pause import Pause


class Window:
    def __init__(self):
        self.shouldClose = False
        self.display = None
        self.view = None
        self.view_destination = (0, 0)
        self.fullscreen = False
        self.monitor_size = [p.display.Info().current_w, p.display.Info().current_h]

    def awake(self):
        self.display = p.display.set_mode(Settings.get("RESOLUTION"), p.RESIZABLE)
        p.display.set_caption(Settings.get("TITLE"))
        p.display.set_icon(Assets.get_image("assets/tiles/1.png"))
        self.resize(Settings.get("WINDOW SIZE"))

        Scenes.add_scene(MainMenu())
        Scenes.add_scene(LevelSelect())
        Scenes.add_scene(Level())
        Scenes.add_scene(Pause())

    def start(self):
        Scenes.set_scene("MAIN MENU")

    def poll_events(self):
        Input.update()

        for ev in p.event.get():
            if ev.type == p.QUIT or Scenes.should_quit:
                self.quit()

            if ev.type == p.VIDEORESIZE:
                self.resize((ev.w, ev.h))

        if Input.get_key_down(p.K_F11):
            self.fullscreen = not self.fullscreen
            if self.fullscreen:
                self.display = p.display.set_mode(self.monitor_size, p.FULLSCREEN)
                self.resize(self.monitor_size)
            else:
                self.display = p.display.set_mode(Settings.get("WINDOW SIZE"), p.RESIZABLE)

    def early_update(self):
        pass

    def update(self):
        Scenes.update()

    def late_update(self):
        pass

    def draw(self):

        self.view.blit(p.transform.scale(Scenes.get_surface(), self.view.get_size()), (0, 0))

        self.display.blit(self.view, self.view_destination)

        p.display.update()

    def quit(self):
        Settings.save()

        self.shouldClose = True
        p.quit()
        sys.exit()

    def resize(self, size):
        aspect = Settings.get("ASPECT RATIO")
        if size[1] * aspect > size[0]:
            self.view = p.Surface((size[0], size[0] / aspect))
        else:
            self.view = p.Surface((size[1] * aspect, size[1]))

        self.view_destination = (self.display.get_width() / 2 - self.view.get_width() / 2,
                                 self.display.get_height() / 2 - self.view.get_height() / 2)

    @staticmethod
    def calculate_dt():
        Time.calculate_dt()
