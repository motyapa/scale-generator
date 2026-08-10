from models.exercise_gen_interface import ExerciseGeneratorInterface
from scripts.util.constants import rhythm_dict
from scripts.util.utility_scripts import create_note_and_append_to_stream, get_pitches, fix_last_measure_duration, \
    get_next_pitch
from scripts.util.utility_scripts import configure_part

class CycleGenerator(ExerciseGeneratorInterface):
    def __init__(self, config):
        super().__init__(config)
        self.cycle_size = config.exercise_size

    def generate_exercise(self):
        part = configure_part(self.config)
        for i in range(len(self.pitches)):
            for j in range(self.cycle_size):
                next_index = i + j
                next_pitch = get_next_pitch(next_index, self.pitches, self.is_descending, self.mode)
                create_note_and_append_to_stream(next_pitch, self.include_note_as_lyric, part, self.duration)
            for j in range(self.cycle_size, -1, -1):
                next_index = i + j
                next_pitch = get_next_pitch(next_index, self.pitches, self.is_descending, self.mode)
                create_note_and_append_to_stream(next_pitch, self.include_note_as_lyric, part, self.duration)

        part.makeMeasures(inPlace=True)
        fix_last_measure_duration(part)
        return part