from backend.scripts.util.utility_scripts import create_note_and_append_to_stream, get_pitches, rhythm_dict, \
    get_next_pitch
from backend.scripts.util.utility_scripts import configure_part

def create_rows(config):
    include_note_as_lyric = config.include_note_as_lyric
    part = configure_part(config)
    pitches = get_pitches(config)[:-1]
    pitches_length = len(pitches)
    row_length = config.exercise_size
    duration = rhythm_dict[config.rhythm]

    is_descending = config.octave_one > config.octave_two

    for i in range(pitches_length - (row_length - 2)):
        for j in range(row_length):
            next_index = i + j
            next_pitch = get_next_pitch(next_index, pitches, is_descending)
            create_note_and_append_to_stream(next_pitch, include_note_as_lyric, part, duration)

    part.makeMeasures(inPlace=True)
    return part