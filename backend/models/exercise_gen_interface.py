from abc import ABC, abstractmethod

from music21.stream import Part

from models.note_config import NoteConfig
from scripts.util.constants import rhythm_dict
from scripts.util.utility_scripts import get_pitches, configure_part


class ExerciseGeneratorInterface(ABC):
    def __init__(self, config):
        self.include_note_as_lyric = config.include_note_as_lyric
        self.pitches = get_pitches(config)
        self.duration = rhythm_dict[config.rhythm]
        self.is_descending = config.octave_one > config.octave_two
        self.mode = config.mode
        self.config = config
        self.part = configure_part(self.config)
        self.note_config = NoteConfig(self.part, self.pitches, self.is_descending, self.mode, self.include_note_as_lyric, self.duration)

    @abstractmethod
    def generate_exercise(self) -> Part: pass