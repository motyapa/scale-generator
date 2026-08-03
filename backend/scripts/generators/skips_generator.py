from scripts.util.constants import rhythm_dict, MAJOR, MAJOR_TWO_DOWN, MINOR_TWO_UP, MAJOR_TWO_UP
from scripts.util.utility_scripts import create_note_and_append_to_stream, get_pitches, get_next_pitch
from scripts.util.utility_scripts import configure_part

def create_skips(config):
    include_note_as_lyric = config.include_note_as_lyric
    part = configure_part(config)
    pitches = get_pitches(config)[:-1]

    interval_of = config.exercise_size
    duration = rhythm_dict[config.rhythm]
    is_descending = config.octave_one > config.octave_two

    for i, curr_pitch in enumerate(pitches):
        next_index = i + interval_of
        next_pitch = get_next_pitch(next_index, pitches, is_descending)

        create_note_and_append_to_stream(curr_pitch, include_note_as_lyric, part, duration)
        create_note_and_append_to_stream(next_pitch, include_note_as_lyric, part, duration)

    starting_note = pitches[-1]
    final_note = find_final_note(config.mode, is_descending, starting_note)

    create_note_and_append_to_stream(final_note, include_note_as_lyric, part, duration)

    part.makeMeasures(inPlace=True)
    return part

def find_final_note(mode, is_descending, starting_note):
    if mode == MAJOR:
        if is_descending:
            final_note = starting_note.transpose(MAJOR_TWO_DOWN)
        else:
            final_note = starting_note.transpose(MINOR_TWO_UP)
    else:
        if is_descending:
            final_note = starting_note.transpose(MAJOR_TWO_DOWN)
        else:
            final_note = starting_note.transpose(MAJOR_TWO_UP)
    return final_note