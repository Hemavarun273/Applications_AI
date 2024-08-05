
def is_valid(board, row, col, num):
    # Check if the number is already in the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number is already in the column
    for j in range(9):
        if board[j][col] == num:
            return False

    # Check if the number is in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    # Find the first empty cell in the board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    # Find an empty location
    empty_location = find_empty_location(board)

    # If there are no empty locations, the Sudoku is solved
    if not empty_location:
        return True

    # Unpack the row and column values
    row, col = empty_location

    # Try placing a number from 1 to 9 in the empty cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Place the number if it's valid
            board[row][col] = num

            # Recursively try to solve the rest of the Sudoku
            if solve_sudoku(board):
                return True

            # If placing the number doesn't lead to a solution, backtrack
            board[row][col] = 0

    # No number from 1 to 9 can be placed in the current cell
    return False

def print_sudoku(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(board[i][j], end=" ")
        print()

# Example Sudoku puzzle
sudoku_board = [
  [5, 3, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Input Sudoku puzzle:")
print_sudoku(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku:")
    print_sudoku(sudoku_board)
else:
    print("\nNo solution exists.")
