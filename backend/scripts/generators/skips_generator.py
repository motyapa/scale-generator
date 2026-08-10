from models.exercise_gen_interface import ExerciseGeneratorInterface
from scripts.util.utility_scripts import create_note, add_last_note


class SkipsGenerator(ExerciseGeneratorInterface):
    def __init__(self, config):
        super().__init__(config)
        self.interval_of = config.exercise_size

    def generate_exercise(self):
        for i in range(len(self.pitches)):
            create_note(i, self.note_config)
            create_note(i + self.interval_of, self.note_config)
        add_last_note(self.note_config)
        return self.part

