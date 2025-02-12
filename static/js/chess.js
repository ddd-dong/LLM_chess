let board = null;
let socket = io();
let gameId = null;

function onDragStart(source, piece) {
    return piece.search(/^w/) !== -1;
}

function onDrop(source, target) {
    fetch('/game/move', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            game_id: gameId,
            move: source + target
        })
    })
    .then(response => response.json())
    .then(data => {
        if (!data.success) {
            return 'snapback';
        }
        updateStatus(data.state);
    });
}

function updateStatus(state) {
    const statusEl = document.getElementById('status');
    board.position(state.fen);
    
    if (state.game_over) {
        statusEl.textContent = state.winner ? 
            `Game Over! ${state.winner} wins!` : 'Game Over! Draw!';
    } else {
        statusEl.textContent = state.in_check ? 'Check!' : 'Your turn';
    }
}

function startNewGame() {
    fetch('/game/new', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            gameId = data.game_id;
            board.start();
            updateStatus(data.state);
        });
}

socket.on('game_update', function(data) {
    if (data.game_id === gameId) {
        updateStatus(data.state);
    }
});

window.onload = function() {
    const config = {
        draggable: true,
        position: 'start',
        onDragStart: onDragStart,
        onDrop: onDrop,
        pieceTheme: 'https://chessboardjs.com/img/chesspieces/wikipedia/{piece}.png'
    };
    
    board = Chessboard('board', config);
    document.getElementById('newGame').addEventListener('click', startNewGame);
    startNewGame();
};