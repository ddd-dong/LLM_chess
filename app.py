from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import chess
import chess.engine
from chess_engine.game import ChessGame
from __init__ import CONFIG


CONFIG.__init__()
app = Flask(__name__)
socketio = SocketIO(app)

# Store active games (in practice, use a proper database)
games = {}

@app.route('/')
def home():
    return render_template('chess.html')

@app.route('/game/new', methods=['POST'])
def new_game():
    game_id = len(games)
    games[game_id] = ChessGame(check_legal_moves=False)
    return jsonify({'game_id': game_id, 'state': games[game_id].get_state()})

@app.route('/game/move', methods=['POST'])
def make_move():
    data = request.json
    game = games.get(data['game_id'])
    if game and game.make_move(data['move']):
        state = game.get_state()
        socketio.emit('game_update', {'game_id': data['game_id'], 'state': state})
        return jsonify({'success': True, 'state': state})
    return jsonify({'success': False})

if __name__ == '__main__':
    socketio.run(app, debug=True)