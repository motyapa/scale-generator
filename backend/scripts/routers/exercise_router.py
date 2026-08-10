from models.config import Config
from enums.type_enums import ExerciseType
from scripts.generators import skips_generator, rows_generator, intervals_generator, chords_generator, cycle_generator
from scripts.generators.chords_generator import ChordGenerator
from scripts.generators.cycle_generator import CycleGenerator
from scripts.generators.intervals_generator import IntervalsGenerator
from scripts.util.utility_scripts import fix_last_measure_duration


def route_exercise(config: Config):
    match config.type:
        case ExerciseType.SKIPS: part = skips_generator.create_skips(config)
        case ExerciseType.ROWS: part = rows_generator.create_rows(config)
        case ExerciseType.INTERVALS: part = IntervalsGenerator(config).generate_exercise()
        case ExerciseType.DIATONIC_CHORDS: part = ChordGenerator(config).generate_exercise()
        case ExerciseType.CYCLES: part = CycleGenerator(config).generate_exercise()
    part.makeMeasures(inPlace=True)
    fix_last_measure_duration(part)
    return part