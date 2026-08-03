from scripts.util.constants import rhythm_dict, PERFECT_EIGHT_DOWN, PERFECT_EIGHT_UP
from scripts.util.utility_scripts import create_note_and_append_to_stream, get_pitches, \
    get_next_pitch
from scripts.util.utility_scripts import configure_part

def create_chords(config):
    include_note_as_lyric = config.include_note_as_lyric
    part = configure_part(config)
    pitches = get_pitches(config)
    duration = rhythm_dict[config.rhythm]
    pitches_length = len(pitches)
    include_seventh = config.include_seventh
    include_octave = config.include_octave

    is_descending = config.octave_one > config.octave_two

    for i in range(0, pitches_length):
        curr_pitch = pitches[i]

        third = get_next_pitch(i + 2, pitches, is_descending)
        fifth = get_next_pitch(i + 4, pitches, is_descending)

        create_note_and_append_to_stream(curr_pitch, include_note_as_lyric, part, duration)
        create_note_and_append_to_stream(third, include_note_as_lyric, part, duration)
        create_note_and_append_to_stream(fifth, include_note_as_lyric, part, duration)

        if include_seventh:
            seventh = get_next_pitch(i + 6, pitches, is_descending)
            create_note_and_append_to_stream(seventh, include_note_as_lyric, part, duration)

        if include_octave:
            octave = get_next_pitch(i + 7, pitches, is_descending)
            create_note_and_append_to_stream(octave, include_note_as_lyric, part, duration)

    if not include_octave:
        if is_descending: final_note = pitches[-1].transpose(PERFECT_EIGHT_DOWN)
        else: final_note = pitches[-1].transpose(PERFECT_EIGHT_UP)
        create_note_and_append_to_stream(final_note, include_note_as_lyric, part, duration)

    part.makeMeasures(inPlace=True)
    return part
