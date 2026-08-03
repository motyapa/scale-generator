from enums.rhythm_enums import RhythmType

rhythm_dict = {
    RhythmType.WHOLE: 4,
    RhythmType.HALF: 2,
    RhythmType.QUARTER: 1,
    RhythmType.EIGHTH: 0.5,
    RhythmType.SIXTEENTH: 0.25,
    RhythmType.TRIPLET: 1/3,
}

MAJOR = "Major"
MINOR = "Minor"
PERFECT_EIGHT_UP = "P8"
PERFECT_EIGHT_DOWN = "P-8"
FOUR_FOUR_SIGNATURE = "4/4"
MAJOR_TWO_UP = "M2"
MAJOR_TWO_DOWN = "M-2"
MINOR_TWO_UP = "m2"