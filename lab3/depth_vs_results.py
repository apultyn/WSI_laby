from TicTacToe import TicTacToe
import matplotlib.pyplot as plt


def main():
    win_plot = []
    lost_plot = []
    draw_plot = []
    for depth in range(1, 9):
        results = []
        for i in range(500):
            game = TicTacToe()
            result = game.play_with_random_bot(True, depth, False)
            print(f"{depth}# Result game {i+1}: {result}")
            results.append(result)
        wins = 0
        lost = 0
        draws = 0

        for result in results:
            if result == 1:
                wins += 1
            elif result == 0:
                draws += 1
            elif result == -1:
                lost += 1
        win_plot.append(wins)
        lost_plot.append(lost)
        draw_plot.append(draws)

    plt.plot(range(1, 9), win_plot, label='Wins')
    plt.plot(range(1, 9), lost_plot, label='Losses')
    plt.plot(range(1, 9), draw_plot, label='Draws')

    plt.xlabel('Depth')
    plt.ylabel('Number of Games')
    plt.title('Min-Max as x')
    plt.legend()
    plt.savefig("plots/depth_vs_results_x_500.pdf")
    plt.show()

    win_plot = []
    lost_plot = []
    draw_plot = []
    for depth in range(1, 9):
        results = []
        for i in range(500):
            game = TicTacToe()
            result = game.play_with_random_bot(False, depth, False)
            print(f"{depth}# Result game {i+1}: {result}")
            results.append(result)
        wins = 0
        lost = 0
        draws = 0

        for result in results:
            if result == 1:
                wins += 1
            elif result == 0:
                draws += 1
            elif result == -1:
                lost += 1
        win_plot.append(wins)
        lost_plot.append(lost)
        draw_plot.append(draws)

    plt.plot(range(1, 9), win_plot, label='Wins')
    plt.plot(range(1, 9), lost_plot, label='Losses')
    plt.plot(range(1, 9), draw_plot, label='Draws')

    plt.xlabel('Depth')
    plt.ylabel('Number of Games')
    plt.title('Min-Max as o')
    plt.legend()
    plt.savefig("plots/depth_vs_results_o_500.pdf")
    plt.show()


if __name__ == "__main__":
    main()
