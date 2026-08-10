from models.config import Config
from enums.type_enums import ExerciseType
from scripts.generators import skips_generator, rows_generator, intervals_generator, chords_generator, cycle_generator
from scripts.generators.chords_generator import ChordGenerator
from scripts.generators.cycle_generator import CycleGenerator


def route_exercise(config: Config):
    match config.type:
        case ExerciseType.SKIPS: return skips_generator.create_skips(config)
        case ExerciseType.ROWS: return rows_generator.create_rows(config)
        case ExerciseType.INTERVALS: return intervals_generator.create_intervals(config)
        case ExerciseType.DIATONIC_CHORDS: return ChordGenerator(config).generate_exercise()
        case ExerciseType.CYCLES: return CycleGenerator(config).generate_exercise()