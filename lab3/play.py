import argparse
import sys

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
    parser.add_argument("min_max_as_x")
    parser.add_argument("depth")
    args = parser.parse_args(arguments[1:])

    min_max_as_x = parse_bool_args(args.min_max_as_x, "min_max_as_x")
    depth = int(args.depth)

    game = TicTacToe()
    game.play_yourself(min_max_as_x, depth)


if __name__ == "__main__":
    main(sys.argv)
