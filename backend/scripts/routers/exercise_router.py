from models.config import Config
from enums.type_enums import ExerciseType
from scripts.generators.chords_generator import ChordGenerator
from scripts.generators.cycle_generator import CycleGenerator
from scripts.generators.intervals_generator import IntervalsGenerator
from scripts.generators.rows_generator import RowsGenerator
from scripts.generators.skips_generator import SkipsGenerator
from scripts.util.utility_scripts import fix_last_measure_duration


def route_exercise(config: Config):
    match config.type:
        case ExerciseType.SKIPS: part = SkipsGenerator(config).generate_exercise()
        case ExerciseType.ROWS: part = RowsGenerator(config).generate_exercise()
        case ExerciseType.INTERVALS: part = IntervalsGenerator(config).generate_exercise()
        case ExerciseType.DIATONIC_CHORDS: part = ChordGenerator(config).generate_exercise()
        case ExerciseType.CYCLES: part = CycleGenerator(config).generate_exercise()
    part.makeMeasures(inPlace=True)
    fix_last_measure_duration(part)
    return part