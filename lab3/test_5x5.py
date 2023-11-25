from min_max import TicTacToe


def test_board_5():
    game = TicTacToe(5)
    assert game._board == [
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_']
    ]


def test_game_over_blank():
    game = TicTacToe(5)
    game._board = [
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_']
    ]
    assert game.game_over(game._board) is False


def test_game_over_full_false():
    game = TicTacToe(5)
    game._board = [
        ['x', 'x', 'o', 'o', 'x'],
        ['o', 'x', 'o', 'x', 'o'],
        ['x', 'o', 'x', 'o', 'x'],
        ['x', 'o', 'x', 'o', 'x'],
        ['o', 'x', 'x', 'o', 'o']
    ]
    assert game.game_over(game._board) is False


def test_game_over_some_false():
    game = TicTacToe(3)
    game._board = [
        ['x', '_', 'o', 'o', 'x'],
        ['o', 'x', 'o', '_', 'o'],
        ['x', 'o', 'x', 'o', 'x'],
        ['x', '_', 'x', '_', 'x'],
        ['o', 'x', 'x', 'o', 'o']
    ]
    assert game.game_over(game._board) is False


def test_game_over_horizontal_true():
    game = TicTacToe(3)
    game._board = [
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_'],
        ['o', 'o', 'o', 'o', '_']
    ]
    assert game.game_over(game._board) is True


def test_game_over_vertical_true():
    game = TicTacToe(3)
    game._board = [
        ['_', '_', '_', '_', 'o'],
        ['_', '_', '_', '_', 'o'],
        ['_', '_', '_', '_', 'o'],
        ['_', '_', '_', '_', 'o'],
        ['_', '_', '_', '_', '_']
    ]
    assert game.game_over(game._board) is True


def test_game_over_diagonal_true():
    game = TicTacToe(3)
    game._board = [
        ['_', 'x', '_', '_', '_'],
        ['_', '_', 'x', '_', '_'],
        ['_', '_', '_', 'x', '_'],
        ['_', '_', '_', '_', 'x'],
        ['_', '_', '_', '_', '_']
    ]
    assert game.game_over(game._board) is True


def test_game_over_full_true():
    game = TicTacToe(5)
    game._board = [
        ['x', 'x', 'o', 'o', 'x'],
        ['o', 'x', 'o', 'x', 'o'],
        ['x', 'o', 'x', 'o', 'x'],
        ['x', 'o', 'x', 'x', 'x'],
        ['o', 'x', 'x', 'o', 'o']
    ]
    assert game.game_over(game._board) is True


def test_game_over_some_true():
    game = TicTacToe(3)
    game._board = [
        ['x', '_', 'o', 'o', 'x'],
        ['_', 'x', 'o', '_', 'o'],
        ['x', 'o', 'x', 'o', 'x'],
        ['x', '_', 'x', 'x', 'x'],
        ['o', 'x', 'x', 'o', 'o']
    ]
    assert game.game_over(game._board) is True
