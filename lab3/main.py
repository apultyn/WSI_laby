from TicTacToe import TicTacToe


def main():
    results = []
    for i in range(10):
        game = TicTacToe()
        result = game.play_with_random_bot(True, 1, False)
        print(f"Result game {i+1}: {result}")
        results.append(result)
    print(results)


if __name__ == "__main__":
    main()
