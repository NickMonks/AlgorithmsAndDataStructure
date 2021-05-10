import unittest

# O(n) time | O(1) space
def isMonotonic(array):
    # check direction
	if len(array)<=2:
		return True
	
	# ideally, we should use enums, but in our case is fine to use 
	# the diference between one element and the other. 
	# This is actually pretty useful and is better than using just boolean
	# with boolean it would take a bit longer 
	direction = array[1] - array[0]
	
	for i in range(2, len(array)):
		# check if direction is meaningful
		if direction == 0:
			direction = array[i] - array [i-1]
			continue
		
		# Once we know that it has a direction, let's check if it breaks 
		# the original direction (remember that direction is only stored once!)
		# we pass the direction and also the array values. 
		if breaksDirection(direction, array[i-1], array[i]):
			return False
		
	return True
		
def breaksDirection(direction, previousInt, currentInt):
	difference = currentInt - previousInt
	
	# a clean way to write this. Instead of using direction > 0 And difference < 0
	# this approach is much cleaner. 
	if direction > 0:
		return difference < 0
	return difference > 0

# ---- ALTERNATIVE SOLUTION

def isMonotonic2(array):
    	# Another approach is to check simultaneously the two possible scenarios
	# if both fails then return false; if one of them is true then return true
	
	# we define two booleans. IMPORTANT to pre-define the value to true!
    isNonDecreasing = True
    isNonIncreasing = True
	
    for i in range(1, len(array)):
	    # during this for loop, we will flag the opposite case to be false.
		# so if we see an increase and a decrease, it will be both false. 
	    if array[i] < array[i-1]:
		    isNonDecreasing = False
	    if array[i] > array[i-1]:
		    isNonIncreasing = False
	
	
    return isNonIncreasing or isNonDecreasing

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        expected = True
        actual = isMonotonic(array)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()