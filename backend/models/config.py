from dataclasses import dataclass

from backend.enums.rhythm_enums import RhythmType
from backend.enums.type_enums import ExerciseType


@dataclass
class Config:
    type: ExerciseType
    key: str
    mode: str
    include_note_as_lyric: bool
    exercise_size: int
    rhythm: RhythmType
    octave_one: int
    octave_two: int
    include_seventh: bool
    include_octave: bool