import unittest

# O(n^2) time | O(n) space
def minNumberOfJumps(array):
    
    jumps = [float("inf") for x in array]
    jumps[0] = 0
    for i in range(1, len(array)):
        for j in range(0,i):
            if array[j] + j >= i:
                jumps[i] = min(jumps[j]+1, jumps[i])
    
    return jumps[-1]

# O(n) time | O(1) space
def minNumberOfJumps(array):
	if len(array) == 1:
		return 0
	jumps = 0
	# We define a maxReach variable, which stores the maximum reach of the 
	# variable in an index. then we use the steps variable which stores how many variables are we analyzing
	# the max reach (e.g. maxReach = 3 then steps = 3,2,1,... which was maxReach? jump to it and repeat process)
	maxReach = array[0]
	steps = array[0]
	
	for i in range(1, len(array)-1):
		# we check the max value of the index we are plus the array[i] value)
		maxReach = max(maxReach, i + array[i])
		steps -= 1
		
		# Once the steps is zero, we go to the max reach position and repeat process
		if steps ==0:
			jumps +=1
			steps = maxReach - i
	
	return jumps + 1 # "+1" because we stop just before finish the array

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]), 4)


if __name__ == "__main__":
    unittest.main()
