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
        return (
            self.check_rows() or
            self.check_columns() or
            self.check_diagonals() or
            self.check_four_in_a_row()
        )

    def check_rows(self):
        for row in self._board:
            if all(square == row[0] and square != 0 for square in row):
                return True
        return False

    def check_columns(self):
        for col in range(len(self._board[0])):
            if all(self._board[row][col] == self._board[0][col] and self._board[row][col] != 0 for row in range(len(self._board))):
                return True
        return False

    def check_diagonals(self):
        if all(self._board[i][i] == self._board[0][0] and self._board[i][i] != 0 for i in range(len(self._board))):
            return True

        if all(self._board[i][len(self._board) - 1 - i] == self._board[0][len(self._board) - 1] and self._board[i][len(self._board) - 1 - i] != 0 for i in range(len(self._board))):
            return True

        return False

    def check_four_in_a_row(self):
        if len(self._board) <= 3:
            return False

        for row in self._board:
            for i in range(len(row) - 3):
                if all(row[i + j] == row[i] and row[i] != 0 for j in range(4)):
                    return True

        for col in range(len(self._board[0])):
            for i in range(len(self._board) - 3):
                if all(self._board[i + j][col] == self._board[i][col] and self._board[i][col] != 0 for j in range(4)):
                    return True

        for i in range(len(self._board) - 3):
            for j in range(len(self._board[0]) - 3):
                if all(self._board[i + k][j + k] == self._board[i][j] and self._board[i][j] != 0 for k in range(4)):
                    return True

                if all(self._board[i + k][j + 3 - k] == self._board[i][j + 3] and self._board[i][j + 3] != 0 for k in range(4)):
                    return True

        return False

    def min_max(self, position, depth, maximazingPlayer):
        pass

    def get_parameters(self):
        pass

    def solve(self):
        pass
