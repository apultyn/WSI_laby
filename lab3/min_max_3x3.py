import copy


class TicTacToe3x3:
    def __init__(self):
        self.board = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']
        ]

    def eval(self, position, maxPlayer):
        if (
            self.check_vert(position) or
            self.check_hori(position) or
            self.check_diag(position)
        ):
            if maxPlayer:
                return -1
            else:
                return 1
        return 0

    def check_vert(self, position):
        for row in position:
            if ((row[0] == row[1] == row[2]) and row[0] != '_'):
                return True
        return False

    def check_hori(self, position):
        for i in range(3):
            if ((position[i][0] == position[i][1] == position[i][2]) and position[i][0] != '_'):
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
        return moves

    def minimax(self, position, maxPlayer):
        moves = self.get_moves(position)
        if moves == []:
            return self.eval(position, maxPlayer)

        if maxPlayer:
            max_eval = float('-inf')
            for move in moves:
                new_pos = copy.deepcopy(position)
                new_pos[move[0]][move[1]] = 'x'

                eval = self.minimax(new_pos, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in moves:
                new_pos = copy.deepcopy(position)
                new_pos[move[0]][move[1]] = 'o'

                eval = self.minimax(new_pos, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def find_best_move(self, position, maxPlayer):
        moves = self.get_moves(position)
        if moves == []:
            return None

        best_pos = []
        if maxPlayer:
            max_eval = float('-inf')
            for move in moves:
                new_pos = copy.deepcopy(position)
                new_pos[move[0]][move[1]] = 'x'

                eval = self.minimax(new_pos, False)
                if eval > max_eval:
                    max_eval = eval
                    best_pos = new_pos
        else:
            min_eval = float('inf')
            for move in moves:
                new_pos = copy.deepcopy(position)
                new_pos[move[0]][move[1]] = 'o'

                eval = self.minimax(new_pos, True)
                if eval < min_eval:
                    min_eval = eval
                    best_pos = new_pos
        return best_pos

    def print_board(self):
        for row in self.board:
            for square in row:
                print(f"{square} ", end="")
            print()

    def play(self):
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

            if self.eval(self.board, False) == -1:
                print("You won!")
                break

            print("Algorithm's move:")
            self.board = self.find_best_move(self.board, False)

            if self.board is None:
                print("Draw")
                break

            if self.eval(self.board, True) == 1:
                print("Algorithm won!")
                break

        self.print_board()
