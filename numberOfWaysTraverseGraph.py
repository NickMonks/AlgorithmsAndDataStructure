import unittest

# O(2^(n+m)) time | O(n+m) space
def numberOfWaysToTraverseGraph(width, height):
	# Base case: when the width or the height reaches 1 that means we have the number
	if width == 1 or height == 1:
		return 1
	
	# we will be adding over and over the values... this idiom is used a lot in recursion
	return numberOfWaysToTraverseGraph(width-1,height) + numberOfWaysToTraverseGraph(width, height-1)

# --- second solution
def numberOfWaysToTraverseGraph(width, height):
	# we add the "+1" to avoid index error range 
	numberOfWays = [[0 for _ in range(width + 1)] for _ in range(height+1)]
	
	for widthIdx in range(1, width +1):
		for heightIdx in range(1, height+1):
			if widthIdx == 1 or heightIdx == 1:
				numberOfWays[heightIdx][widthIdx] = 1
			else:
				waysUp = numberOfWays[heightIdx - 1][widthIdx]
				waysLeft = numberOfWays[heightIdx][widthIdx -1]
				numberOfWays[heightIdx][widthIdx] = waysUp + waysLeft
	
	return numberOfWays[height][width]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        width = 4
        height = 3
        expected = 10
        actual = numberOfWaysToTraverseGraph(width, height)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()