from min_max import TicTacToe


def test_board_3():
    game = TicTacToe(3)
    assert game._board == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]


def test_board_5():
    game = TicTacToe(5)
    assert game._board == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]


def test_game_over_3_blank():
    game = TicTacToe(3)
    game._board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert game.game_over() is False


def test_game_over_3_full_false():
    game = TicTacToe(3)
    game._board = [
        ['x', 'x', 'o'],
        ['o', 'o', 'x'],
        ['x', 'o', 'x']
    ]
    assert game.game_over() is False


def test_game_over_3_some_false():
    game = TicTacToe(3)
    game._board = [
        ['x', 0, 'o'],
        [0, 'o', 'x'],
        [0, 'o', 0]
    ]
    assert game.game_over() is False


def test_game_over_3_horizontal_true():
    game = TicTacToe(3)
    game._board = [
        ['x', 'x', 'x'],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert game.game_over() is True


def test_game_over_3_vertical_true():
    game = TicTacToe(3)
    game._board = [
        [0, 'o', 0],
        [0, 'o', 0],
        [0, 'o', 0]
    ]
    assert game.game_over() is True


def test_game_over_3_diagonal_true():
    game = TicTacToe(3)
    game._board = [
        [0, 0, 'x'],
        [0, 'x', 0],
        ['x', 0, 0]
    ]
    assert game.game_over() is True
