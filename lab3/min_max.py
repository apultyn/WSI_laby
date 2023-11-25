from solver import Solver


class TicTacToe(Solver):
    def __init__(self, size):
        self._board = []
        for _ in range(size):
            row = []
            for _ in range(size):
                row.append(0)
            self._board.append(row)

    def print_board(self):
        for row in self._board:
            for square in row:
                print(f"{square} ", end="")
            print()

    def get_parameters(self):
        pass

    def solve(self):
        pass
