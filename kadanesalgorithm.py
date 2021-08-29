import unittest

def kadanesAlgorithm(array):
    	# the kadanes Algorithm tries to find the maximum sum value of a subarray inside an array. The challenge is obviously the fact that we can negative numbers. How to solve this easily?
	# a way to do this in a clean way is using dynamic programming; basically we create an array were, at index i, we try to find the biggest sum if we are adding the element at index i.
	# so, when we add a value we need to decide, either to add that value to our previous max value, or start counting at i. 
	# So, for [3,5,-9,1], the array will be: [3,8,-1,1]. The "-1" is due to the fact we could chose to start at -9, or -1 (8 -9). Then, at "1" we simply start at 1 since adding -1 + 1 = 0.
	# Moreover, instead of using an auxiliary data structure, we just need to keep track of the maximum value, and the maximum value at i - 1. 
	
	maxEndingHere = array[0]
	maxSoFar = array[0]
	
	#iterate through the array at 1
	for num in array[1:]:
		# our dynamic programming logic - we find the max between number and the sum of the previous maxEndingHere and num
		maxEndingHere = max(num, maxEndingHere + num)
		maxSoFar = max(maxSoFar, maxEndingHere)
	
	return maxSoFar

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]), 19)

if __name__ == "__main__":
    unittest.main()