import unittest

# O(h*w) Time and Size
def maximumSumSubmatrix(matrix, size):
    # This problem can be solved in two ways: brute force approach, which is basically sum all the elements of a matriz (size,size), for each (i,j)
	# position; however, this takes O(h*w*size^2) time, since we need to check every element and then sum size^2 elements.
	# If we analyze this solution, we found out that there are a lot of repeating sums that overlap, what if we could create a data structure
	# such that for every position we know the total sum of each element?
	# we use dynamic programming; using an auxiliary data structure with size h*w and initialize with zeroes, we save an accumulative value from (0,0) to that element
	# then, we can create a relationship calculation for each position, because if we know the sum of the elements we can infer the total sum of a square.
	
	# create the matrix of sums
	sums = createSumMatrix(matrix)
	
	# initialise max matrix sum value
	maxSubMatrixSum = float('-inf')
	
	# now we loop over all the elements of the matrix. Bear in mind that we start at (size -1, size -1) corner, to have the first square
	for row in range(size -1, len(matrix)):
		for col in range(size -1, len(matrix[row])):
			total = sums[row][col]
			
			# here, we need to perform our substractions, since we are taking the whole size of the matrix.
			# we need to check if we are touching the top border, left-border or both. For that, we use a boolean
			# value that will tell us if we are touching or not. 
			
			touchesTopBorder = row - size < 0
			if not touchesTopBorder:
				total -= sums[row-size][col]
				
			touchesLeftBorder = col - size < 0
			if not touchesLeftBorder:
				total -= sums[row][col - size]
			
			# if we are not touching neither the top or left border, that means we are substracting twice to the top-left element corner,
			# so we need to add it
			touchesToporLeftBorder = touchesTopBorder or touchesLeftBorder
			if not touchesToporLeftBorder:
				total += sums[row-size][col-size]
			
			maxSubMatrixSum = max(maxSubMatrixSum, total)
		
	return maxSubMatrixSum

def createSumMatrix(matrix):
	# initialise the data structure as zeroes:
	# this is an important operation we need to memorise!
	sums = [[0 for _ in range(len(matrix[row]))] for row in range(len(matrix))]
	
	# create the sums of the matrix, initialise the first element as its equal
	sums[0][0] = matrix[0][0]
	
	# first fill the first row...
	for idx in range(1,len(matrix[0])):
		# we accumulate the sums of the previous and the present matrix element
		sums[0][idx] = sums[0][idx - 1] + matrix[0][idx]
	
	# ... then we sum the first column
	for idx in range(1,len(matrix)):
		sums[idx][0] = sums[idx - 1][0] + matrix[idx][0]
	
	for row in range(1, len(matrix)):
		for col in range(1, len(matrix[row])):
			
			# to have the sum of the elements, we need to be careful, because we don't want to sum the same element
			# twice (imagine a 2x2 matrix, if we slide to the right we will accumulate the top corner element)
			sums[row][col] = sums[row -1][col] + sums[row][col -1] - sums[row -1][col -1] + matrix[row][col]
	
	return sums

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [[5, 3, -1, 5], [-7, 3, 7, 4], [12, 8, 0, 0], [1, -8, -8, 2]]
        size = 2
        expected = 18
        actual = maximumSumSubmatrix(matrix, size)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()