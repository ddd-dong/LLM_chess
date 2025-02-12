import chess
import chess.engine
from typing import Optional,Literal, Dict, Any
from .ai import ChessAI
from __init__ import Config
import os

class ChessGame:
    def __init__(self,opponent: Optional[str] = "stockfish",check_legal_moves:Optional[bool] = True,\
                  elo: Optional[int] = None):
        self.board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci(os.environ.get('STOCKFISH_PATH'))
        self.opponent = opponent
        self.check_legal_moves = check_legal_moves
        if self.opponent == "stockfish":
            self.ai = self.engine
        else:
            pass
            # ToDo: Implement custom AI
        if elo:
            self.engine.configure({"UCI_LimitStrength": True, "UCI_Elo": elo})

    def _ai_move(self,move_str: str):
        if self.opponent == "stockfish":
            return self.engine.play(self.board, chess.engine.Limit(time=2.0))
        else:
            pass
            #To Do

    def make_move(self, move_str:str) -> bool:
        try:
            move = chess.Move.from_uci(move_str)
            if not(move in self.board.legal_moves) and (self.check_legal_moves):
                return False
            self.board.push(move)
            if not self.board.is_game_over():
                result = self._ai_move(move_str)
                self.board.push(result.move)
            return True
        except:
            return False

    def get_state(self):
        return {
            'fen': self.board.fen(),
            'game_over': self.board.is_game_over(),
            'legal_moves': [str(move) for move in self.board.legal_moves]
        }