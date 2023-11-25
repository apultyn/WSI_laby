from min_max import TicTacToe


def main():
    game = TicTacToe(3)
    game.play(depth=3)


if __name__ == "__main__":
    main()
