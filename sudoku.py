from pprint import pprint

def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    # index addressing is 0-8
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    return None, None     # if no space is empty


def is_valid(puzzle, guess, row, col):
    # figure out whether a guess at the row, col is valid or not
    # returns True if is valid, False otherwise

    # check row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # check col
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # check 3*3 matrices
    # get where the 3*3 square matrix starts and
    # iterate over the 3 values in the row/col
    row_start = (row // 3) * 3
    col_start = (col // 3) *3
    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False
    # if we get here, checks are passed
    return True



def solve_sudoku(puzzle):
    # solve sudoku using backtracking:
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether solution exist or not
    # mutates puzzle to be the solution (if solution exists)

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True
    
    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):
        # step 3: check if this is valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, them place that guess on the puzzle
            puzzle[row][col] = guess
            # step 4: recursively call our function 
            if solve_sudoku(puzzle):
                return True
        
        # step 5: if not valid OR if our guess does not solve the puzzle
        puzzle[row][col] = -1 # reset the guess
    
    # step 6: if none of the numbers we tried work, the puzzle is UNSOLVABLE!!
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)