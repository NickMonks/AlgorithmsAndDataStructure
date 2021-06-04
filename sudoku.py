import unittest

# O (1) time : it will take a long time, but it will always be constant (since the size of the sudoku is the same, 9x9)
# because there's no n parameters, we can assume is constant
# o(1) space: we re-use the board, so no additional data is stored.
def solveSudoku(board):
	solvePartialSudoku(0, 0, board)
	return board
	
def solvePartialSudoku(row, col, board):
	# recursive function that will backtrack when no number can be filled:
	
	currentRow = row
	currentCol = col
	
	# if the col we are is the last one, go to next row
	# OR if current row and col is the last one, return True
	if currentCol == len(board[row]):
		currentRow += 1
		currentCol = 0
		if currentRow == len(board):
			return True
	
	if board[currentRow][currentCol] == 0:
		# we will call a function to try all different digits options
		# from 1 to 9
		return tryDigitsAtPosition(currentRow, currentCol, board)
	
	# if it's not a 0, recursively call the function with next position
	# we add the +1 because we want to move to the right
	return solvePartialSudoku(currentRow, currentCol + 1, board)

def tryDigitsAtPosition(row, col, board):
	# loop over 1 to 9 (dont include 10)
	for digit in range(1,10):
		if isValidAtPosition(digit, row, col, board):
			board[row][col] = digit
			# we will update the board to the new digit, and then call the solvePartialSudoku with the new update
			# again and again. This is the backtracking section of the algorithm;
			# if is not true then it will return and we will keep loop from 1 to 9
			
			if solvePartialSudoku(row, col +1, board):
				return True
	
	# if no number is valid then we need to return back to previous call stack 
	# (that's why we RETURN On line 21)
	board[row][col] = 0
	return False
		

def isValidAtPosition(value, row, col, board):
	# function that checks if the value we added is valid or not
	# TIP: you can use the not in list() to return boolean. 
	
	rowIsValid = value not in board[row]
	
	# TIP: Use functional programming for this
	# we iterate each subarray of board(which is the row) [[1,2..], [1,2...]]
	# and then evaluate the col value. this will generate a list of each value of the row
	# and we will check if value is in there or not
	colIsValid = value not in map(lambda r: r[col], board)
	
	if not rowIsValid or not colIsValid:
		return False
	
	# Check sub-grid (3x3):
	subgridRowStart = row // 3 # floor the row value, to get the number of the subgrid
	subgridColStart = col // 3
	
	# we define range(3) since we now it will be of size 3
	for rowIdx in range(3):
		for colIdx in range(3):
			rowToCheck = subgridRowStart * 3 + rowIdx
			colToCheck = subgridColStart * 3 + colIdx
			existingValue = board[rowToCheck][colToCheck]
			
			if existingValue == value:
				return False
	
	return True

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7],
        ]
        expected = [
            [7, 8, 5, 4, 3, 9, 1, 2, 6],
            [6, 1, 2, 8, 7, 5, 3, 4, 9],
            [4, 9, 3, 6, 2, 1, 5, 7, 8],
            [8, 5, 7, 9, 4, 3, 2, 6, 1],
            [2, 6, 1, 7, 5, 8, 9, 3, 4],
            [9, 3, 4, 1, 6, 2, 7, 8, 5],
            [5, 7, 8, 3, 9, 4, 6, 1, 2],
            [1, 2, 6, 5, 8, 7, 4, 9, 3],
            [3, 4, 9, 2, 1, 6, 8, 5, 7],
        ]
        actual = solveSudoku(input)
        self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    unittest.main()