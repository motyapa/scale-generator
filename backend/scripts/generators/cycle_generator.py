from models.exercise_gen_interface import ExerciseGeneratorInterface
from scripts.util.utility_scripts import create_note

class CycleGenerator(ExerciseGeneratorInterface):
    def __init__(self, config):
        super().__init__(config)
        self.cycle_size = config.exercise_size

    def generate_exercise(self):
        for i in range(len(self.pitches)):
            for j in range(self.cycle_size):
                create_note(i + j, self.note_config)
            for j in range(self.cycle_size, -1, -1):
                create_note(i + j, self.note_config)
        return self.part