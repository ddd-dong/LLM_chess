# Flask Chess Game

A web-based chess game where users can play against an AI opponent. The game logic runs server-side using Flask, with a JavaScript frontend for the user interface.

## Architecture

### Backend (Flask)
- Game state management
- Chess move validation
- AI opponent logic
- RESTful API endpoints
- WebSocket for real-time updates

### Frontend (JavaScript)
- Chess board visualization
- Move input handling
- Real-time game state updates
- User interface elements

## Technical Stack

- **Backend**: 
  - Flask
  - python-chess (chess logic)
  - Stockfish (chess engine)
  - Flask-SocketIO (WebSocket)
  
- **Frontend**:
  - chessboard.js (board visualization)
  - Socket.IO client
  - vanilla JavaScript

## Project Structure
```
chess-website/
├── README.md
├── requirements.txt
├── __init__.py
├── app.py
├── stockfish
│   ├── stockfish-windows-x86-64-avx2.exe
│   ├──...
├── chess_engine/
│   ├── __init__.py
│   ├── game.py
│   └── ai.py
├── static/
│   ├── css/
│   └── js/
└── templates/
```

## Implementation Plan

1. **Phase 1: Core Setup**
   - Initialize Flask project structure
   - Set up basic routing
   - Create chess game class
   - Implement move validation

2. **Phase 2: Game Logic**
   - Integrate python-chess library
   - Implement game state management
   - Add Stockfish integration
   - Create API endpoints

3. **Phase 3: Frontend**
   - Set up chessboard.js
   - Implement move submission
   - Add game state visualization
   - Create user interface

4. **Phase 4: Real-time Updates**
   - Integrate WebSocket
   - Add move broadcasting
   - Implement game state sync

## API Endpoints

- `POST /game/new` - Start new game
- `POST /game/move` - Submit move
- `GET /game/state` - Get current state
- `POST /game/resign` - Resign game

## WebSocket Events

- `connect` - Client connection
- `move` - Move updates
- `game_state` - State changes
- `disconnect` - Client disconnection