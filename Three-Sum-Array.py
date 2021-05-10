import unittest

def threeNumberSum(array, targetSum):
    	# We use sort algorithm to sort the array, which will take O(log N) 
	# if the algorithm is quick enough (e.g, quick sort for example)
	
	#since our algorithm is O(N^2) it wont affect us much 
	
	array.sort()
	
	triplets = [];
	
	# We define three pointers: the first element, the second one (the min) and the rightmost
	# One (the max). we will move these pointers depending if the value is < or > than 
	# the targetSum. if it's equal to the sum then we will store the value AND move both pointers
	# until they cross each other. After that, we will change the first pointer. 
	for i in range(len(array)-2):
		
		# we define the indexes
		left = i + 1
		right = len(array)-1
		
		while left < right:
			currentSum = array[i] + array[left] + array[right]
			if currentSum == targetSum:
				triplets.append([array[i], array[left], array[right]])
				
				# After finding a successful candidate, we increment the left
				# pointer and de-crement the right one. 
				left+=1
				right-=1
			
			# if the currentsum is less than the target, move left 
			# pointer to the right
			elif currentSum < targetSum:
				left+=1
			elif currentSum > targetSum:
				right-=1
				
	return triplets


# Unit test
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])


if __name__ == '__main__':
    unittest.main()