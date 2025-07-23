from util.Audio import Audio

class Note:

    note_names = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
    note_flats = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
    note_sharps = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    note_naturals = ["C", "D", "E", "F", "G", "A", "B"]

    notes = {name : num for num, name in enumerate(note_names)}

    @staticmethod
    def get_name(degree):
        return Note.note_names[degree]
    
    @staticmethod
    def get_degree(name):
        return Note.notes[name]
    
    @staticmethod
    def by_degree(degree, octave):
        return Note(Note.get_name(degree), octave)

    def __init__(self, name, octave):
        self.name = name
        self.degree = Note.notes[name]

        self.octave = octave

    def __hash__(self):
        return self.octave * 12 + self.degree

    def get_interval(self, interval):
        new_degree = Note.get_degree(self.name) + interval
        new_octave = (new_degree // 12) + self.octave
        new_note = Note.get_name(new_degree % 12)

        return Note(new_note, new_octave)
    
    def play(self):
        Audio.play_sound(self.to_file())
    
    def to_file(self):
        return "notes/" + str(self.note_flats[self.degree]) + str(self.octave) + ".wav"

    def __str__(self):
        return self.name + str(self.octave)
    
    def __repr__(self):
        return self.name
        

class Interval:
    FIRST = 0
    UNISON = FIRST
    MINOR_SECOND = 1
    MAJOR_SECOND = 2
    MINOR_THIRD = 3
    MAJOR_THIRD = 4
    PERFECT_FOURTH = 5
    TRITONE = 6
    PERFECT_FIFTH = 7
    MINOR_SIXTH = 8
    MAJOR_SIXTH = 9
    MINOR_SEVENTH = 10
    MAJOR_SEVENTH = 11
    OCTAVE = 12
    
    MAJOR = [FIRST, MAJOR_THIRD, PERFECT_FIFTH]
    MINOR = [FIRST, MINOR_THIRD, PERFECT_FIFTH]
    SEVENTH = [FIRST, MAJOR_THIRD, PERFECT_FIFTH, MINOR_SEVENTH]
    
    chord_types = {"MAJOR": MAJOR, "MINOR": MINOR, "7": SEVENTH}

    intervals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    interval_names = ["1st (Unison)", "Minor 2nd", "Major 2nd", "Minor 3rd", "Major 3rd", "Perfect 4th", "Tritone", 
                 "Perfect 5th", "Minor 6th", "Major 6th", "Minor 7th", "Major 7th", "Octave"]
    
    interval_dict = {name : num for num, name in enumerate(interval_names)}

    perfect_intervals = [FIRST, PERFECT_FOURTH, PERFECT_FIFTH, OCTAVE]
    consonant_intervals = [MINOR_THIRD, MAJOR_THIRD, MINOR_SIXTH, MAJOR_SIXTH]
    less_consonant_intervals = [MINOR_SECOND, MAJOR_SECOND, MINOR_SEVENTH, MAJOR_SEVENTH]
    all_intervals = [FIRST, MINOR_SECOND, MAJOR_SECOND, MINOR_THIRD, MAJOR_THIRD, PERFECT_FOURTH, TRITONE, 
                     PERFECT_FIFTH, MINOR_SIXTH, MAJOR_SIXTH, MINOR_SEVENTH, MAJOR_SEVENTH, OCTAVE]


    @staticmethod
    def get_name(interval):
        return Interval.interval_names[abs(interval)]
    
    @staticmethod
    def get_chord(chord_type: str):
        return Interval.chord_types[chord_type.upper()]

