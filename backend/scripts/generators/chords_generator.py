from models.exercise_gen_interface import ExerciseGeneratorInterface
from scripts.util.constants import PERFECT_EIGHT_DOWN, PERFECT_EIGHT_UP
from scripts.util.utility_scripts import create_note_and_append_to_stream, get_next_pitch, fix_last_measure_duration, \
    create_note
from scripts.util.utility_scripts import configure_part

INDEX_FOR_THIRD = 2
INDEX_FOR_FIFTH = 4
INDEX_FOR_SEVENTH = 6
INDEX_FOR_OCTAVE = 7

class ChordGenerator(ExerciseGeneratorInterface):
    def __init__(self, config):
        super().__init__(config)
        self.include_seventh = config.include_seventh
        self.include_octave = config.include_octave

    def generate_exercise(self):
        part = configure_part(self.config)
        for i in range(len(self.pitches)):
            create_note(i, part, self.pitches, self.is_descending, self.mode, self.include_note_as_lyric, self.duration)
            create_note(i + INDEX_FOR_THIRD, part, self.pitches, self.is_descending, self.mode, self.include_note_as_lyric, self.duration)
            create_note(i + INDEX_FOR_FIFTH, part, self.pitches, self.is_descending, self.mode, self.include_note_as_lyric, self.duration)
            self.check_and_add_extra_notes(i, part)

        self.add_last_note(part)
        return part

    def add_last_note(self, part):
        if not self.include_octave:
            create_note(-1, part, self.pitches, self.is_descending, self.mode, self.include_note_as_lyric, self.duration)

    def check_and_add_extra_notes(self, index, part):
        if self.include_seventh:
            create_note(index + INDEX_FOR_SEVENTH, part, self.pitches, self.is_descending, self.mode, self.include_note_as_lyric, self.duration)

        if self.include_octave:
            create_note(index + INDEX_FOR_OCTAVE, part, self.pitches, self.is_descending, self.mode, self.include_note_as_lyric, self.duration)
