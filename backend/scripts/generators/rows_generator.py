from models.exercise_gen_interface import ExerciseGeneratorInterface
from scripts.util.utility_scripts import *

class RowsGenerator(ExerciseGeneratorInterface):
    def __init__(self, config):
        super().__init__(config)
        self.row_length = config.exercise_size

    def generate_exercise(self):
        for i in range(len(self.pitches) - (self.row_length - 1)):
            for j in range(self.row_length):
                create_note(i + j, self.note_config)
        return self.part