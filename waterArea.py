import unittest

# Time: O(N) | Space: O(N)
def waterArea(heights):
	# This problem can be solved easily using dynamic programming. We know for a fact that the water will be trapped between 
	# the pillars, and that the water will be trapped if the height at the current index is less than the neighbours.
	# but only the minimum between the biggests pillars in the extremes will trap water.
	# How do we implement this?
	#
	# We need to understand what is what we want. between index i and j, I want to know which of the greatest pillars are, but also the MIN BETWEEN BOTH OF THEM
	# So, we need two data structures: maxs of pillars from left-right and right-left. Then a thrid array to store the minimum of these. 
	#
	# we define two arrays, which will take the max height of the pillars from left to right, and from right to left.
	# then we will define another array that takes the min(array1, array2). for each index:
	# if height < minheight:
	# 	w = minheight - hight
	# else:
	# w = 0
	
	maxes = [0 for x in heights]
	leftMax = 0
	
	# Define the left max array:
	for i in range(len(heights)):
		height = heights[i]
		maxes[i] = leftMax
		# we update the max value by checking the leftMax value, which originally is just 0.
		leftMax = max(leftMax, height)
	
	# conceptually, we stored 3 arrays; here, we will just do the calculations of the third array 
	# re-using this maxes array. This is a bit more efficient, but the complexity analysis it wont change
	rightMax = 0
	for i in reversed(range(len(heights))):
		height = heights[i]
		# calculate third array directly.
		minHeight = min(rightMax, maxes[i])
		if height < minHeight:
			maxes[i] = minHeight - height
		else:
			maxes[i] = 0
		
		rightMax = max(rightMax, height)
	
	return sum(maxes)

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]), 48)

if __name__ == "__main__":
    unittest.main()