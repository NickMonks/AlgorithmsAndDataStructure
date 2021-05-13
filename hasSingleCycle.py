import unittest

# O(n) time | O(1) Space
def hasSingleCycle(array):
	# we want to check that we will jump exactly n times, and the condition
	# shall be that we return back to the same element. 
	# two conditions:
	# - If after n iterations we're not reaching original index;
	# - If we reach the original index before finish n iterations;
	# then return false
	
	numElementsVisited = 0
	currentIdx = 0 # In an interview maybe you want to add an argument for the starting index
	
	while numElementsVisited < len(array):
		if numElementsVisited > 0 and currentIdx == 0:
			return False
		numElementsVisited +=1
		currentIdx = getNextIdx(currentIdx, array)
	
	# once visited n elements,  confirm that currentIdx is STARTING:
	return currentIdx == 0 # IMPORTANT: remember that we can do this in Python!

def getNextIdx(currentIdx, array):
	# HINT: When we have edge cases, wrap it in a helper function
	jump = array[currentIdx]
	# HINT: When we have cycles that might go over and over, use the mod operator
	nextIdx = (currentIdx + jump) % len(array) # BEWARE! We might overpass the array and cycle over it
	
	# Be careful; we can have negative numbers. So return whatever the mod was (negative) plus the length we have
	return nextIdx if nextIdx >= 0 else nextIdx + len(array)

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(hasSingleCycle([2, 3, 1, -4, -4, 2]), True)

if __name__ == '__main__':
    unittest.main()