let board = null;
let socket = null;
let gameId = null;
let lastMove = null;

function onDragStart(source, piece) {
    return true; // Allow any piece to move
}

function highlightSquare(square) {
    const $square = $('#board .square-' + square);
    $square.addClass('highlight-square');
}

function removeHighlights() {
    $('#board .square-55d63').removeClass('highlight-square');
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
        updateStatus(data.state);
    });
}

function updateStatus(state) {
    const statusEl = document.getElementById('status');
    board.position(state.fen);
    
    removeHighlights();
    if (state.last_move) {
        const [source, target] = [
            state.last_move.slice(0,2),
            state.last_move.slice(2,4)
        ];
        highlightSquare(source);
        highlightSquare(target);
    }
    
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

window.onload = function() {
    const config = {
        draggable: true,
        position: 'start',
        onDragStart: onDragStart,
        onDrop: onDrop,
        pieceTheme: 'https://chessboardjs.com/img/chesspieces/wikipedia/{piece}.png'
    };
    
    board = Chessboard('board', config);
    socket = io();
    
    socket.on('game_update', function(data) {
        if (data.game_id === gameId) {
            updateStatus(data.state);
        }
    });
    
    document.getElementById('newGame').addEventListener('click', startNewGame);
    startNewGame();
};