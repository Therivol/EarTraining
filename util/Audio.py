import pygame as p


class Audio:
    p.mixer.init()

    working_dir = "assets/"
    sounds = {}

    @staticmethod
    def play_sound(sound_name: str) -> None:
        file_name = Audio.get_path(sound_name)

        if file_name in Audio.sounds:
            Audio.sounds[file_name].play()
        
        else:
            Audio.new_sound(file_name)
            Audio.sounds[file_name].play()

    @staticmethod
    def new_sound(file_name: str) -> None:
        Audio.sounds[file_name] = p.mixer.Sound(file_name)

    @staticmethod
    def get_path(file_name: str) -> str:
        return Audio.working_dir + file_name