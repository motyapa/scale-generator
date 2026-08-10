from models.exercise_gen_interface import ExerciseGeneratorInterface
from scripts.util.constants import INDEX_FOR_OCTAVE
from scripts.util.utility_scripts import create_note, add_last_note

INDEX_FOR_THIRD = 2
INDEX_FOR_FIFTH = 4
INDEX_FOR_SEVENTH = 6

class ChordGenerator(ExerciseGeneratorInterface):
    def __init__(self, config):
        super().__init__(config)
        self.include_seventh = config.include_seventh
        self.include_octave = config.include_octave

    def generate_exercise(self):
        for i in range(len(self.pitches)):
            create_note(i, self.note_config)
            create_note(i + INDEX_FOR_THIRD, self.note_config)
            create_note(i + INDEX_FOR_FIFTH, self.note_config)
            self.check_and_add_extra_notes(i, self.note_config)
            
        if not self.include_octave:
            add_last_note(self.note_config)
        return self.part

    def check_and_add_extra_notes(self, index, note_config):
        if self.include_seventh:
            create_note(index + INDEX_FOR_SEVENTH, note_config)

        if self.include_octave:
            create_note(index + INDEX_FOR_OCTAVE, note_config)
