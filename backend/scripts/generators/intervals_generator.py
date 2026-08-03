from scripts.util.constants import rhythm_dict
from scripts.util.utility_scripts import create_note_and_append_to_stream, get_pitches
from scripts.util.utility_scripts import configure_part

def create_intervals(config):
    include_note_as_lyric = config.include_note_as_lyric
    part = configure_part(config)
    pitches = get_pitches(config)
    interval_of = config.exercise_size
    duration = rhythm_dict[config.rhythm]

    for i in range(0, len(pitches), interval_of):
        curr_pitch = pitches[i]
        create_note_and_append_to_stream(curr_pitch, include_note_as_lyric, part, duration)

    part.makeMeasures(inPlace=True)
    return part