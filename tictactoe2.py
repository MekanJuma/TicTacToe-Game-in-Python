class TicTacToe:
    def __init__(self, size=3):
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]
        self.current_player = "X"
        self.moves_count = 0

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * (self.size * 4 - 1))

    def check_win(self):
        lines = []

        for i in range(self.size):
            lines.append(self.board[i])  # Rows
            lines.append([self.board[j][i] for j in range(self.size)])  # Columns

        lines.append([self.board[i][i] for i in range(self.size)])
        lines.append([self.board[i][self.size - 1 - i] for i in range(self.size)])

        for line in lines:
            if all(cell == self.current_player for cell in line):
                return True
        return False

    def check_draw(self):
        return self.moves_count == self.size**2

    def play_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.moves_count += 1
            if self.check_win():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                return True
            if self.check_draw():
                self.print_board()
                print("It's a draw!")
                return True
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("This position is already taken.")
        return False

    def get_player_input(self):
        while True:
            try:
                row, col = map(int, input(f"Player {self.current_player}, enter row and column numbers (0-{self.size-1}) separated by space: ").split())
                if 0 <= row < self.size and 0 <= col < self.size:
                    return row, col
                else:
                    print(f"Please enter numbers in the range 0-{self.size-1}.")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by space.")

    def start_game(self):
        while True:
            self.print_board()
            row, col = self.get_player_input()
            if self.play_move(row, col):
                break

if __name__ == "__main__":
    game_size = int(input("Enter the Tic Tac Toe board size (default 3): ") or 3)
    game = TicTacToe(game_size)
    game.start_game()
