import unittest

# O (n) Space & Time
def zigzagTraverse(array):
    	
	height = len(array) -1
	width = len(array[0]) -1
	
	result = []
	row, col = 0, 0
	
	goingDown = True
	
	while not isOutOfBounds(row,col, height, width):
		result.append(array[row][col])
		
		if goingDown:
			if col == 0 or row == height:
				
				# Change the direction to going up
				goingDown = False
				if row == height:
					# if we reach the last row, we move in the column direction
					col += 1
				else:
					# if we are in the col = 0, we move the row 
					row += 1
			
			else:
				# Because we're going down, we reduce the col to one and increase the row by one
				row += 1
				col -= 1
		else:
			# we're going up
			if row == 0 or col == width:
				goingDown = True
				
				if col == width:
					row += 1
				else:
					col +=1
			
			else:
				row -= 1
				col += 1
	
	return result

# O(1) time 
def isOutOfBounds(row,col, height, width):
	return row < 0 or row > height or col < 0 or col > width
			

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
        self.assertEqual(zigzagTraverse(test), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

if __name__ == "__main__":
    unittest.main()