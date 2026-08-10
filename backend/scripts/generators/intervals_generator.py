from models.exercise_gen_interface import ExerciseGeneratorInterface
from scripts.util.utility_scripts import create_note

class IntervalsGenerator(ExerciseGeneratorInterface):
    def __init__(self, config):
        super().__init__(config)
        self.interval_size = config.exercise_size

    def generate_exercise(self):
        for i in range(0, len(self.pitches), self.interval_size):
            create_note(i, self.note_config)
        return self.part
