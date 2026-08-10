from models.exercise_gen_interface import ExerciseGeneratorInterface
from scripts.util.constants import PERFECT_EIGHT_DOWN, PERFECT_EIGHT_UP
from scripts.util.utility_scripts import create_note_and_append_to_stream, get_next_pitch, fix_last_measure_duration
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
        for i in range(0, len(self.pitches)):
            self.create_note(i, part)
            self.create_note(i + INDEX_FOR_THIRD, part)
            self.create_note(i + INDEX_FOR_FIFTH, part)

            if self.include_seventh:
                self.create_note(i + INDEX_FOR_SEVENTH, part)

            if self.include_octave:
                self.create_note(i + INDEX_FOR_OCTAVE, part)

        self.add_last_note(part)
        return part

    def create_note(self, index, part):
        pitch = get_next_pitch(index, self.pitches, self.is_descending, self.mode)
        create_note_and_append_to_stream(pitch, self.include_note_as_lyric, part, self.duration)

    def add_last_note(self, part):
        if not self.include_octave:
            if self.is_descending:
                final_note = self.pitches[-1].transpose(PERFECT_EIGHT_DOWN)
            else:
                final_note = self.pitches[-1].transpose(PERFECT_EIGHT_UP)
            create_note_and_append_to_stream(final_note, self.include_note_as_lyric, part, self.duration)


