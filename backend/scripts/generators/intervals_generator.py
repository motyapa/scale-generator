from models.exercise_gen_interface import ExerciseGeneratorInterface
from scripts.util.utility_scripts import create_note_and_append_to_stream, fix_last_measure_duration, create_note
from scripts.util.utility_scripts import configure_part

class IntervalsGenerator(ExerciseGeneratorInterface):
    def __init__(self, config):
        super().__init__(config)
        self.interval_size = config.exercise_size

    def generate_exercise(self):
        part = configure_part(self.config)
        for i in range(0, len(self.pitches), self.interval_size):
            create_note(i, part, self.pitches, self.is_descending, self.mode, self.include_note_as_lyric, self.duration)
        return part
