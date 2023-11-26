from TicTacToe import TicTacToe


def main():
    game = TicTacToe()
    # game.play_yourself(depth=2)

    print(game.play_with_random_bot(True, 10))


if __name__ == "__main__":
    main()
