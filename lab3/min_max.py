from solver import Solver
import copy


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

    def print_board(self, board):
        for row in board:
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
            if all(board[row][col] == board[0][col] and
                   board[row][col] != 0 for row in range(len(board))):
                return True
        return False

    def check_diagonals(self, board):
        if all(board[i][i] == board[0][0] and
               board[i][i] != 0 for i in range(len(board))):
            return True

        if all(board[i][len(board) - 1 - i] == board[0][len(board) - 1] and
               board[i][len(board) - 1 - i] != 0 for i in range(len(board))):
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
                if all(board[i + j][col] == board[i][col] and
                       board[i][col] != 0 for j in range(4)):
                    return True

        for i in range(len(board) - 3):
            for j in range(len(board[0]) - 3):
                if all(board[i + k][j + k] == board[i][j] and
                       board[i][j] != 0 for k in range(4)):
                    return True

                if all(board[i + k][j + 3 - k] == board[i][j + 3] and
                       board[i][j + 3] != 0 for k in range(4)):
                    return True

        return False

    def eval(self, position, depth, maximizingPlayer):
        if self.game_over(position):
            if maximizingPlayer:
                return -10 + depth
            else:
                return 10 - depth
        else:
            return 0

    def min_max(self, position, depth, maximizingPlayer):
        if depth == 0 or self.game_over(position):
            return self.eval(position, depth, maximizingPlayer)

        if maximizingPlayer:
            max_value = float('-inf')
            for i in range(len(position)):
                for j in range(len(position[0])):
                    if position[i][j] == 0:
                        new_pos = copy.deepcopy(position)
                        new_pos[i][j] = 'x'
                        value = self.min_max(new_pos, depth - 1, False)
                        if value > max_value:
                            max_value = value
                            max_move = new_pos
            # print(f"Max value at depth {depth} with eval {max_value} after x moved: ")
            # self.print_board(max_move)
            return max_value
        else:
            min_value = float('inf')
            for i in range(len(position)):
                for j in range(len(position[0])):
                    if position[i][j] == 0:
                        new_pos = copy.deepcopy(position)
                        new_pos[i][j] = 'o'
                        value = self.min_max(new_pos, depth - 1, True)
                        if value < min_value:
                            min_value = value
                            min_move = new_pos
            # print(f"Min value at depth {depth} with eval {min_value} after x moved: ")
            # self.print_board(min_move)
            return min_value

    def play(self, depth):
        while not self.game_over(self._board):
            # Player's move
            self.print_board(self._board)
            print("Your move (enter row and column separated by space): ")
            row, col = map(int, input().split())
            if self._board[row][col] == 0:
                self._board[row][col] = 'x'
            else:
                print("Invalid move. Try again.")
                continue

            if self.game_over(self._board):
                print("You won!")
                break

            # Algorithm's move
            print(f"\nAlgorithm's move:")
            self.min_max(self._board, depth, False)

            if self.game_over(self._board):
                print("Algorithm won!")
                break

        self.print_board(self._board)

    def get_parameters(self):
        pass

    def solve(self):
        pass
