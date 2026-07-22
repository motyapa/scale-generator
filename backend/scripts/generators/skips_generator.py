from typing_inspection.typing_objects import is_deprecated

from backend.scripts.util.utility_scripts import create_note_and_append_to_stream, get_pitches, rhythm_dict, \
    get_next_pitch
from backend.scripts.util.utility_scripts import configure_part

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

    if config.mode == 'Major':
        if is_descending:
            final_note = pitches[-1].transpose("M-2")
        else:
            final_note = pitches[-1].transpose('m2')
    else:
        if is_descending:
            final_note = pitches[-1].transpose('M-2')
        else:
            final_note = pitches[-1].transpose('M2')

    create_note_and_append_to_stream(final_note, include_note_as_lyric, part, duration)

    part.makeMeasures(inPlace=True)
    return part