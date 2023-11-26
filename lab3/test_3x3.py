from min_max import TicTacToe


def test_board():
    game = TicTacToe(3)
    assert game._board == [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]


def test_game_over_blank():
    game = TicTacToe(3)
    game._board = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]
    assert game.game_won(game._board) is False


def test_game_over_full_false():
    game = TicTacToe(3)
    game._board = [
        ['x', 'x', 'o'],
        ['o', 'o', 'x'],
        ['x', 'o', 'x']
    ]
    assert game.game_won(game._board) is False


def test_game_over_some_false():
    game = TicTacToe(3)
    game._board = [
        ['x', '_', 'o'],
        ['_', 'o', 'x'],
        ['_', 'o', '_']
    ]
    assert game.game_won(game._board) is False


def test_game_over_horizontal_true():
    game = TicTacToe(3)
    game._board = [
        ['x', 'x', 'x'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]
    assert game.game_won(game._board) is True


def test_game_over_vertical_true():
    game = TicTacToe(3)
    game._board = [
        ['_', 'o', '_'],
        ['_', 'o', '_'],
        ['_', 'o', '_']
    ]
    assert game.game_won(game._board) is True


def test_game_over_diagonal_true():
    game = TicTacToe(3)
    game._board = [
        ['_', '_', 'x'],
        ['_', 'x', '_'],
        ['x', '_', '_']
    ]
    assert game.game_won(game._board) is True
