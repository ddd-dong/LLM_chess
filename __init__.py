from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        load_dotenv()
        self.opponent_list = ["stockfish", "LLM_easy", "LLM_hard"]
CONFIG = Config()

if __name__ == '__main__':
    CONFIG.__init__()
    print("Stockfish path:",os.environ.get('STOCKFISH_PATH'))