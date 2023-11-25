from min_max import TicTacToe


def main():
    game = TicTacToe(3)
    game.min_max(game._board, 2, True)


if __name__ == "__main__":
    main()
