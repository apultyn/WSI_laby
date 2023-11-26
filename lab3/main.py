from min_max import TicTacToe
from min_max_3x3 import TicTacToe3x3


def main():
    game = TicTacToe(3)
    game.play(depth=10)

    # game2 = TicTacToe3x3()
    # game2.play(depth=10)

if __name__ == "__main__":
    main()
