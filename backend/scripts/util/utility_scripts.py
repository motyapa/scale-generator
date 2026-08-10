from music21 import *
from music21.duration import Duration

from enums.mode_enums import ModeType
from models.note_config import NoteConfig
from scripts.util.constants import MAJOR, MINOR, PERFECT_EIGHT_DOWN, PERFECT_EIGHT_UP, FOUR_FOUR_SIGNATURE, \
    INDEX_FOR_OCTAVE


def create_note(next_index, note_config: NoteConfig):
    note_pitch = get_next_pitch(next_index, note_config)
    create_note_and_append_to_stream(note_pitch, note_config)

def create_note_and_append_to_stream(note_pitch, note_config):
    created_note = note.Note(note_pitch)
    created_note.duration = Duration(note_config.note_duration)
    if note_config.include_name_as_lyric: created_note.lyric = created_note.name.replace("-", "b")
    note_config.part.append(created_note)

def configure_part(config):
    part = stream.Part()
    part.partName = " "
    music_key = get_key(config)
    part.keySignature = music_key
    part.append(meter.TimeSignature(FOUR_FOUR_SIGNATURE))
    return part

def get_pitches(config):
    octave_one = str(config.octave_one)
    octave_two = str(config.octave_two)

    scale_obj = get_scale(config)

    return scale_obj.getPitches(
        config.key + octave_one,
        config.key + octave_two
    )

def get_scale(config):
    match config.mode:
        case ModeType.MAJOR: return scale.MajorScale(config.key)
        case ModeType.MINOR: return scale.MinorScale(config.key)
        case ModeType.MAJOR_PENTATONIC:
            major = scale.MajorScale(config.key)
            notes = major.getPitches(config.key + "4", config.key + "5")
            return scale.ConcreteScale(
                config.key, [notes[0], notes[1], notes[2], notes[4], notes[5]]
            )
        case ModeType.MINOR_PENTATONIC:
            minor = scale.MinorScale(config.key)
            notes = minor.getPitches(config.key + "4", config.key + "5")
            return scale.ConcreteScale(
                config.key, [notes[0], notes[2], notes[3], notes[4], notes[6]]
            )
    return scale.MajorScale("C")

def get_key(config):
    if MAJOR in config.mode.value:
        mode = MAJOR
    else:
        mode = MINOR
    return key.Key(config.key, mode)

def get_next_pitch(next_index, note_config: NoteConfig):
    if note_config.mode == ModeType.MINOR_PENTATONIC or note_config.mode == ModeType.MAJOR_PENTATONIC:
        index_transpose = 5
    else:
        index_transpose = 7
    pitches_length = len(note_config.pitches)
    if next_index < pitches_length:
        next_pitch = note_config.pitches[next_index]
    elif note_config.is_descending:
        next_pitch = note_config.pitches[next_index - index_transpose].transpose(PERFECT_EIGHT_DOWN)
    else:
        next_pitch = note_config.pitches[next_index - index_transpose].transpose(PERFECT_EIGHT_UP)
    return next_pitch

def fix_last_measure_duration(part):
    for measure in part.getElementsByClass("Measure"):
        remaining = measure.barDuration.quarterLength - measure.duration.quarterLength

        if remaining > 0:
            last_note = measure.notes[-1]
            last_note.duration.quarterLength += remaining

def add_last_note(note_config):
    create_note(len(note_config.pitches) - 1 + INDEX_FOR_OCTAVE, note_config)