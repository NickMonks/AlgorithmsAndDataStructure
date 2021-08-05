import unittest

def minimumPassesOfMatrix(matrix):
    # To solve this problem, we need to understand the following: we want to flip the negative values if 
	# we have any negative numbers. What we really want to find is, on the first pass, find ALL positive
	# numbers (>0), and then when we find a negative value, save it in a data structure and flip it to positive.
	# Once the queue is emptied, we have done a pass, and we go to the other queue and do another pass
	# we will use a queue of (x,y) tuple, storing the positive values first and then the adjacent negative values on a SECOND
	# queue. once the current queue (the one we pop) is empty, we swap the current to be the next, and the next (the one where we enqueue values) to be current
	# and adding +1 every time. At the end, we need to do -1 because last pass is basically taking the last changed value, but in reality is positive
	
	# we can solve this problem with one queue tho; basically calculating the size of the queue at the beginning, and doing size-=1 every time
	# we pop. once size=0, we define passes+=1 and size be equal to current size.
	
	passes = convertNegatives(matrix)
	
	# ensure we dont have any negative values in the matrix	
	return passes - 1 if not containsNegatives(matrix) else -1

def convertNegatives(matrix):
	nextPassQueue = getAllPositivePositions(matrix)
	passes = 0
	
	while len(nextPassQueue) >0:
		# initialise the current queue values
		currentPassQueue = nextPassQueue
		nextPassQueue = []
		
		while len(currentPassQueue) > 0:
			# note that we are using a normal array, and therefore the time complexity is actually O(N)
			# but we can assume we are using a queue for now
			currentRow, currentCol = currentPassQueue.pop(0)
			adjacentPositions = getAdjacentPositions(currentRow, currentCol, matrix)
			
			for position in adjacentPositions:
				row, col = position
				value = matrix[row][col]
				if value < 0:
					matrix[row][col] = value * -1
					nextPassQueue.append([row, col])
		
		passes += 1
	return passes

def getAllPositivePositions(matrix):
	# append positve values 
	positivePositions = []
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			value = matrix[row][col]
			if value > 0:
				positivePositions.append([row, col])

	return positivePositions

def getAdjacentPositions(row, col, matrix):
	adjacentPositions = []
	
	if row > 0:
		adjacentPositions.append([row -1, col])
	if row < len(matrix) -1:
		adjacentPositions.append([row+1, col])
	if col > 0:
		adjacentPositions.append([row,col-1])
	if col < len(matrix[0]) -1 :
		adjacentPositions.append([row, col +1])
	
	return adjacentPositions

def containsNegatives(matrix):
	for row in matrix:
		for value in row:
			if value < 0:
				return True
	return False

# Using one queue only:

def convertNegatives2(matrix):
    queue = getAllPositivePositions(matrix)
    passes = 0
    
    while len(queue) >0:
        currentSize = len(queue)
        
        while currentSize > 0:
            # note that we are using a normal array, and therefore the time complexity is actually O(N)
            # but we can assume we are using a queue for now
            currentRow, currentCol = queue.pop(0)
            currentSize -= 1
            adjacentPositions = getAdjacentPositions(currentRow, currentCol, matrix)
            
            for position in adjacentPositions:
                row, col = position
                value = matrix[row][col]
                if value < 0:
                    matrix[row][col] = value * -1
                    queue.append([row, col])
        
        
        passes += 1
        
    return passes

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [
            [0, -1, -3, 2, 0],
            [1, -2, -5, -1, -3],
            [3, 0, 0, -4, -1],
        ]
        expected = 3
        actual = minimumPassesOfMatrix(input)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()