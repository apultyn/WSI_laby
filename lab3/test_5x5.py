from min_max import TicTacToe


def test_board_5():
    game = TicTacToe(5)
    assert game._board == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]


def test_game_over_blank():
    game = TicTacToe(5)
    game._board = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
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
        ['x', 0, 'o', 'o', 'x'],
        ['o', 'x', 'o', 0, 'o'],
        ['x', 'o', 'x', 'o', 'x'],
        ['x', 0, 'x', 0, 'x'],
        ['o', 'x', 'x', 'o', 'o']
    ]
    assert game.game_over(game._board) is False


def test_game_over_horizontal_true():
    game = TicTacToe(3)
    game._board = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        ['o', 'o', 'o', 'o', 0]
    ]
    assert game.game_over(game._board) is True


def test_game_over_vertical_true():
    game = TicTacToe(3)
    game._board = [
        [0, 0, 0, 0, 'o'],
        [0, 0, 0, 0, 'o'],
        [0, 0, 0, 0, 'o'],
        [0, 0, 0, 0, 'o'],
        [0, 0, 0, 0, 0]
    ]
    assert game.game_over(game._board) is True


def test_game_over_diagonal_true():
    game = TicTacToe(3)
    game._board = [
        [0, 'x', 0, 0, 0],
        [0, 0, 'x', 0, 0],
        [0, 0, 0, 'x', 0],
        [0, 0, 0, 0, 'x'],
        [0, 0, 0, 0, 0]
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
        ['x', 0, 'o', 'o', 'x'],
        [0, 'x', 'o', 0, 'o'],
        ['x', 'o', 'x', 'o', 'x'],
        ['x', 0, 'x', 'x', 'x'],
        ['o', 'x', 'x', 'o', 'o']
    ]
    assert game.game_over(game._board) is True
