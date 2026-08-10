from dataclasses import dataclass

from music21.pitch import Pitch
from music21.stream import Part


@dataclass
class NoteConfig:
    part: Part
    pitches: list[Pitch]
    is_descending: bool
    mode: str
    include_name_as_lyric: bool
    note_duration: int
