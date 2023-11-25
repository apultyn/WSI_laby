from min_max import TicTacToe


def test_board():
    game = TicTacToe(3)
    assert game._board == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]


def test_game_over_blank():
    game = TicTacToe(3)
    game._board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert game.game_over(game._board) is False


def test_game_over_full_false():
    game = TicTacToe(3)
    game._board = [
        ['x', 'x', 'o'],
        ['o', 'o', 'x'],
        ['x', 'o', 'x']
    ]
    assert game.game_over(game._board) is False


def test_game_over_some_false():
    game = TicTacToe(3)
    game._board = [
        ['x', 0, 'o'],
        [0, 'o', 'x'],
        [0, 'o', 0]
    ]
    assert game.game_over(game._board) is False


def test_game_over_horizontal_true():
    game = TicTacToe(3)
    game._board = [
        ['x', 'x', 'x'],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert game.game_over(game._board) is True


def test_game_over_vertical_true():
    game = TicTacToe(3)
    game._board = [
        [0, 'o', 0],
        [0, 'o', 0],
        [0, 'o', 0]
    ]
    assert game.game_over(game._board) is True


def test_game_over_diagonal_true():
    game = TicTacToe(3)
    game._board = [
        [0, 0, 'x'],
        [0, 'x', 0],
        ['x', 0, 0]
    ]
    assert game.game_over(game._board) is True
