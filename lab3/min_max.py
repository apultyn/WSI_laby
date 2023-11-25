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

    def game_over(self, board):
        return (
            self.check_rows(board) or
            self.check_columns(board) or
            self.check_diagonals(board) or
            self.check_four_in_a_row(board)
        )

    def check_rows(self, board):
        for row in board:
            if all(square == row[0] and square != 0 for square in row):
                return True
        return False

    def check_columns(self, board):
        for col in range(len(board[0])):
            if all(board[row][col] == board[0][col] and board[row][col] != 0 for row in range(len(board))):
                return True
        return False

    def check_diagonals(self, board):
        if all(board[i][i] == board[0][0] and board[i][i] != 0 for i in range(len(board))):
            return True

        if all(board[i][len(board) - 1 - i] == board[0][len(board) - 1] and board[i][len(board) - 1 - i] != 0 for i in range(len(board))):
            return True

        return False

    def check_four_in_a_row(self, board):
        if len(board) <= 3:
            return False

        for row in board:
            for i in range(len(row) - 3):
                if all(row[i + j] == row[i] and row[i] != 0 for j in range(4)):
                    return True

        for col in range(len(board[0])):
            for i in range(len(board) - 3):
                if all(board[i + j][col] == board[i][col] and board[i][col] != 0 for j in range(4)):
                    return True

        for i in range(len(board) - 3):
            for j in range(len(board[0]) - 3):
                if all(board[i + k][j + k] == board[i][j] and board[i][j] != 0 for k in range(4)):
                    return True

                if all(board[i + k][j + 3 - k] == board[i][j + 3] and board[i][j + 3] != 0 for k in range(4)):
                    return True

        return False

    def min_max(self, position, depth, maximazingPlayer):
        if depth == 0 or self.game_over():
            pass

    def get_parameters(self):
        pass

    def solve(self):
        pass
