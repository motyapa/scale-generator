from music21 import *
from music21.duration import Duration

from backend.enums.rhythm_enums import RhythmType


def create_note_and_append_to_stream(note_pitch, include_name_as_lyric, note_stream, note_duration):
    created_note = note.Note(note_pitch)
    created_note.duration = Duration(note_duration)
    if include_name_as_lyric: created_note.lyric = created_note.name.replace("-", "b")
    note_stream.append(created_note)

def configure_part(config):
    part = stream.Part()
    part.partName = " "
    music_key = get_key(config)
    part.keySignature = music_key
    part.append(meter.TimeSignature('4/4'))
    return part

def get_pitches(config):
    octave_one = str(config.octave_one)
    octave_two = str(config.octave_two)
    key_of = config.key
    music_key = get_key(config)
    pitches = music_key.getPitches(key_of + octave_one, key_of + octave_two)
    return pitches

def get_key(config):
    key_of = config.key
    mode = config.mode
    return key.Key(key_of, mode)

def get_next_pitch(next_index, pitches, is_descending):
    pitches_length = len(pitches)
    if next_index < pitches_length:
        next_pitch = pitches[next_index]
    elif is_descending:
        next_pitch = pitches[next_index - 7].transpose('P-8')
    else:
        next_pitch = pitches[next_index - 7].transpose('P8')
    return next_pitch

rhythm_dict = {
    RhythmType.WHOLE: 4,
    RhythmType.HALF: 2,
    RhythmType.QUARTER: 1,
    RhythmType.EIGHTH: 0.5,
    RhythmType.SIXTEENTH: 0.25,
    RhythmType.TRIPLET: 1/3,
}
