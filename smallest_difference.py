import unittest

# Time O(Nlog(N) + M log(M)) | Space O(1)
def smallestDifference(arrayOne, arrayTwo):
	
    # HINT: When we need to compare two arrays and is un-sorted,
	# first sort them out (even if time complexity is O(N log N ))
	arrayOne.sort()
	arrayTwo.sort()
	
	idxOne = 0
	idxTwo = 0
	
	smallest = float("inf") # HINT, initialising with this we will ensure the first value will be stored
	current = float("inf")
	
	smallestPair = []
	
	# Then, we approach this with a DIY solution: we will have two pointers in each array
	# and we will check if x < y (x: pointer to One; y: pointer to Two)
	# We will store the min difference and the pair of values in specific variables:
	
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
	
		# The following conditions must apply:
		# - x < y : move x to the right (index++) & Compute abs difference
		# - x > y : move y to the left (index--) & Compute abs difference
		
		firstNum = arrayOne[idxOne]
		secondNum = arrayTwo[idxTwo]
		
		if firstNum < secondNum:
			current = secondNum - firstNum # HINT: if we know two is bigger (because is sorted) put it before one)
			idxOne +=1
		elif secondNum < firstNum:
			current = firstNum - secondNum
			idxTwo +=1
		else:
			# the numbers are equal
			return [firstNum, secondNum]
		
		# If the difference is bigger than current
		if smallest > current:
			smallest = current
			smallestPair = [firstNum, secondNum]
	
	return smallestPair

# --- UNIT TESTS
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]), [28, 26])


if __name__=='__main__':
    unittest.main()