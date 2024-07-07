class NQueen:
    def __init__(self, N):
        self.N = N

    def print_solution(self, board):
        for row in board:
            print(" ".join(map(str, row)))

    def is_safe(self, board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve_nq_util(self, board, col):
        if col >= self.N:
            return True

        for i in range(self.N):
            if self.is_safe(board, i, col):
                board[i][col] = 1
                if self.solve_nq_util(board, col + 1):
                    return True
                board[i][col] = 0  # BACKTRACK

        return False

    def solve_nq(self):
        board = [[0] * self.N for _ in range(self.N)]
        if not self.solve_nq_util(board, 0):
            print(f"Solution does not exist for {self.N} queens")
            return False
        print(f"Solution found for {self.N} queens")
        self.print_solution(board)
        return True


if __name__ == "__main__":
    n = int(input("Number of queens to place: "))
    queen = NQueen(n)
    queen.solve_nq()