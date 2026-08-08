from scripts.util.constants import rhythm_dict
from scripts.util.utility_scripts import create_note_and_append_to_stream, get_pitches, fix_last_measure_duration, \
    get_next_pitch
from scripts.util.utility_scripts import configure_part

def create_cycles(config):
    include_note_as_lyric = config.include_note_as_lyric
    part = configure_part(config)
    pitches = get_pitches(config)
    cycle_size = config.exercise_size
    duration = rhythm_dict[config.rhythm]
    is_descending = config.octave_one > config.octave_two

    for i in range(len(pitches)):
        for j in range(cycle_size):
            next_index = i + j
            next_pitch = get_next_pitch(next_index, pitches, is_descending, config.mode)
            create_note_and_append_to_stream(next_pitch, include_note_as_lyric, part, duration)
        for j in range(cycle_size, -1, -1):
            next_index = i + j
            next_pitch = get_next_pitch(next_index, pitches, is_descending, config.mode)
            create_note_and_append_to_stream(next_pitch, include_note_as_lyric, part, duration)

    part.makeMeasures(inPlace=True)
    fix_last_measure_duration(part)
    return part