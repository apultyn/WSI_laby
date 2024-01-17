import argparse
import sys
import json

from frozen_lake import FrozenLake


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("map_file")
    parser.add_argument("close_bonus")
    parser.add_argument("slippery_rate")
    parser.add_argument("epochs")
    parser.add_argument("learning_rate")
    parser.add_argument("discount_factor")
    parser.add_argument("epsilon")
    parser.add_argument("--test_name")
    args = parser.parse_args(arguments[1:])

    map_file = args.map_file
    close_bonus = None

    if args.close_bonus == "True":
        close_bonus = True
    elif args.close_bonus == "False":
        close_bonus = False

    slippery_rate = float(args.slippery_rate)
    epochs = int(args.epochs)
    learning_rate = float(args.learning_rate)
    discount_factor = float(args.discount_factor)
    epsilon = float(args.epsilon)
    test_name = args.test_name

    frozenLake = FrozenLake(map_file, close_bonus, slippery_rate)
    frozenLake.train(epochs, learning_rate,
                     discount_factor, epsilon, test_name)

    if test_name:
        dict = {
            "test_name": test_name,
            "map_file": map_file,
            "close_bonus": close_bonus,
            "slippery_rate": slippery_rate,
            "epochs": epochs,
            "learning_rate": learning_rate,
            "discount_factor": discount_factor,
            "epsilon": epsilon
        }
        json_filename = f"results/{test_name}_params.json"
        with open(json_filename, 'w') as json_file:
            json.dump(dict, json_file, indent=4)


if __name__ == "__main__":
    main(sys.argv)
