from solver import Solver


class TicTacToe(Solver):
    def __init__(self, size):
        if size < 3:
            raise ValueError("Board can't be smaller than 3x3")
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

    def game_over(self):
        return (self.check_rows() or
                self.check_columns() or
                self.check_diagonals())

    def check_rows(self):
        for row in self._board:
            if all(square == row[0] and square != 0 for square in row):
                return True
        return False

    def check_columns(self):
        for col in range(len(self._board[0])):
            if all(self._board[row][col] == self._board[0][col] and
                   self._board[row][col] != 0
                   for row in range(len(self._board))):
                return True
        return False

    def check_diagonals(self):
        # Check main diagonal
        if all(self._board[i][i] == self._board[0][0] and
               self._board[i][i] != 0 for i in range(len(self._board))):
            return True

        # Check secondary diagonal
        if all(self._board[i][len(self._board) - 1 - i] ==
               self._board[0][len(self._board) - 1] and
               self._board[i][len(self._board) - 1 - i] != 0
               for i in range(len(self._board))):
            return True

        return False

    def min_max(self, position, depth, maximazingPlayer):
        pass

    def get_parameters(self):
        pass

    def solve(self):
        pass
