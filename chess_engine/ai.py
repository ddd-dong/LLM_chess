import chess
import chess.engine
from typing import Dict

class ChessAI:
    DIFFICULTY_LEVELS: Dict[str, Dict[str, float]] = {
        'beginner': {'depth': 2, 'time': 0.1, 'skill': 5},
        'intermediate': {'depth': 5, 'time': 0.5, 'skill': 10},
        'advanced': {'depth': 10, 'time': 1.0, 'skill': 15},
        'expert': {'depth': 15, 'time': 2.0, 'skill': 20}
    }

    def __init__(self, engine: chess.engine.SimpleEngine):
        self.engine = engine
        self.difficulty = 'intermediate'
        self._configure_engine()

    def get_move(self, board: chess.Board) -> chess.Move:
        settings = self.DIFFICULTY_LEVELS[self.difficulty]
        result = self.engine.play(
            board,
            chess.engine.Limit(
                time=settings['time'],
                depth=settings['depth']
            ),
            options={'Skill Level': settings['skill']}
        )
        return result.move

    def set_difficulty(self, level: str):
        if level in self.DIFFICULTY_LEVELS:
            self.difficulty = level
            self._configure_engine()

    def _configure_engine(self):
        settings = self.DIFFICULTY_LEVELS[self.difficulty]
        self.engine.configure({
            'Skill Level': settings['skill'],
            'Contempt': 0,
            'Hash': 64,
            'Threads': 1
        })