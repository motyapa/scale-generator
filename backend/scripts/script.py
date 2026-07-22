from music21 import *

from backend.models.config import Config
from backend.scripts.routers import exercise_router

if __name__ == '__main__':
    score = stream.Score()
    part1_config = Config('Rows', 'A#', 'MAJOR', True)
    part1 = exercise_router.route_exercise(part1_config)
    score.insert(0, part1)
    score.show()





