from models.exercise_gen_interface import ExerciseGeneratorInterface
from scripts.util.constants import rhythm_dict
from scripts.util.utility_scripts import create_note_and_append_to_stream, get_pitches, fix_last_measure_duration
from scripts.util.utility_scripts import configure_part

class IntervalsGenerator(ExerciseGeneratorInterface):
    def __init__(self, config):
        super().__init__(config)
        self.interval_size = config.exercise_size

    def generate_exercise(self):
        part = configure_part(self.config)
        for i in range(0, len(self.pitches), self.interval_size):
            curr_pitch = self.pitches[i]
            create_note_and_append_to_stream(curr_pitch, self.include_note_as_lyric, part, self.duration)

        part.makeMeasures(inPlace=True)
        fix_last_measure_duration(part)
        return part
