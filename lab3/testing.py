import argparse
import sys
import json
import matplotlib.pyplot as plt
import numpy as np
from TicTacToe import TicTacToe


def parse_bool_args(string, arg_name):
    if string == "True":
        return True
    elif string == "False":
        return False
    else:
        raise ValueError(f"Argument {arg_name} can only be True or False!")


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("iter")
    parser.add_argument("min_max_as_x")
    parser.add_argument("depth")
    parser.add_argument("print_results")
    parser.add_argument("--test_name")
    args = parser.parse_args(arguments[1:])

    iter = int(args.iter)
    min_max_as_x = parse_bool_args(args.min_max_as_x, "min_max_as_x")
    depth = int(args.depth)
    print_results = parse_bool_args(args.print_results, "print_results")
    test_name = args.test_name

    results = []
    for i in range(iter):
        game = TicTacToe()
        result = game.play_with_random_bot(min_max_as_x, depth, print_results)
        print(f"Result game {i+1}: {result}")
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

    print(f"Win/lost/draw: {wins}/{lost}/{draws}")

    dict = {
        "params": {
            "iter": iter,
            "min_max_as_x": min_max_as_x,
            "depth": depth,
            "print_results": print_results,
            "test_name": test_name
        },
        "results": {
            "wins": wins,
            "win_per": round((wins / iter), 2),
            "lost": lost,
            "lost_per": round((lost / iter), 2),
            "draws": draws,
            "draws_per": round((draws / iter), 2),
        }
    }

    if test_name is not None:
        json_object = json.dumps(dict, indent=4)
        with open(f"results/{test_name}.json", "w") as file_handle:
            file_handle.write(json_object)

    plt.plot(np.arange(1, iter + 1), results,
             marker='o', linestyle='-', color='b')
    plt.title(f"Results of {test_name}")
    plt.xlabel("Game Iteration")
    plt.ylabel("Game Result")
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    if test_name is not None:
        plt.savefig(f"plots/{test_name}.pdf")
    plt.show()


if __name__ == "__main__":
    main(sys.argv)
