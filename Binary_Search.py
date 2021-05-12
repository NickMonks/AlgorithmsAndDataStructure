import unittest

def binarySearch(array, target):
    	# Binary search perform the algorithm considering three pointers:
	# Left pointer, Right pointer and Middle:
	
	# TIP: contextualise variable names. I.e. we now that left and right
	# will mean left and right pointer for this situation. 
	left = 0
	right = len(array)-1
	
	while left <= right: 
		middle = (left + right)//2
				   
		# TIP: Name your name relevant to your problem. this value is in fact
		# the middle, but what it means for our problem?: is the potential match value!
		potentialMatch = array[middle]
		if potentialMatch == target:
			return middle
		elif target < potentialMatch:
			right = middle -1
		else:
			left = middle + 1
	
	# In case the while loop breaks, i.e. the left pointer is bigger than right, then return -1
	return -1

import unittest

# ---- UNIT TEST
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)

if __name__ == '__main__':
    unittest.main()