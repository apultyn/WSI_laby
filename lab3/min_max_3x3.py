import copy
import numpy as np


class TicTacToe3x3:
    def __init__(self):
        self.board = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']
        ]

    def game_over(self, position):
        return (
            self.check_vert(position) or
            self.check_hori(position) or
            self.check_diag(position) or
            self.get_moves(position) == []
        )

    def eval(self, position, depth, maxPlayer):
        if (
            self.check_vert(position) or
            self.check_hori(position) or
            self.check_diag(position)
        ):
            if maxPlayer:
                return -10 - depth
            else:
                return 10 + depth
        return 0

    def check_vert(self, position):
        for i in range(3):
            if ((position[0][i] == position[1][i] == position[2][i]) and position[0][i] != '_'):
                return True
        return False

    def check_hori(self, position):
        for row in position:
            if ((row[0] == row[1] == row[2]) and row[0] != '_'):
                return True
        return False

    def check_diag(self, position):
        return (
            ((position[0][0] == position[1][1] == position[2][2]) or
             (position[0][2] == position[1][1] == position[2][0])) and (position[1][1] != '_')
        )

    def get_moves(self, position):
        moves = []
        for i in range(3):
            for j in range(3):
                if position[i][j] == '_':
                    moves.append((i, j))
        np.random.shuffle(moves)
        return moves

    def minimax(self, position, depth, maxPlayer):
        if self.game_over(position):
            return self.eval(position, depth, maxPlayer)

        moves = self.get_moves(position)
        if maxPlayer:
            max_eval = float('-inf')
            for move in moves:
                new_pos = copy.deepcopy(position)
                new_pos[move[0]][move[1]] = 'x'

                eval = self.minimax(new_pos, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in moves:
                new_pos = copy.deepcopy(position)
                new_pos[move[0]][move[1]] = 'o'

                eval = self.minimax(new_pos, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def find_best_move(self, position, depth, maxPlayer):
        moves = self.get_moves(position)
        best_pos = []
        if maxPlayer:
            max_eval = float('-inf')
            for move in moves:
                new_pos = copy.deepcopy(position)
                new_pos[move[0]][move[1]] = 'x'

                eval = self.minimax(new_pos, depth - 1, False)
                if eval > max_eval:
                    max_eval = eval
                    best_pos = new_pos
        else:
            min_eval = float('inf')
            for move in moves:
                new_pos = copy.deepcopy(position)
                new_pos[move[0]][move[1]] = 'o'

                eval = self.minimax(new_pos, depth - 1, True)
                if eval < min_eval:
                    min_eval = eval
                    best_pos = new_pos
        return best_pos

    def print_board(self):
        for row in self.board:
            for square in row:
                print(f"{square} ", end="")
            print()

    def play(self, depth):
        if depth > 8:
            depth = 8
        while not self.get_moves(self.board) == []:
            self.print_board()
            answer = input("Your move: ")
            row = int(answer[0])
            col = int(answer[2])

            if self.board[row][col] == '_':
                self.board[row][col] = 'x'
            else:
                print("Invalid move. Try again.")
                continue

            depth -= 1

            if self.game_over(self.board):
                result = self.eval(self.board, depth, False)
                if result > 0:
                    print("You won!")
                    break
                elif result == 0:
                    print("Draw!")
                    break

            print("Algorithm's move:")
            self.board = self.find_best_move(self.board, depth, False)
            depth -= 1

            if self.game_over(self.board):
                if self.eval(self.board, depth, True) < 0:
                    print("Algorithm won!")
                    break

        self.print_board()
