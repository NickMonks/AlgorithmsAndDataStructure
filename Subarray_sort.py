
import unittest

# O(N) Time | O(1) Space
def subarraySort(array):
	# we first need to find the unsorted numbers, and inside the
	# unsorted numbers, find the smallest and the greatest. 
	# once that is done, check which position should they be.
	# those will be the indices. 
	
	# IMPORTANT: We initialise the min and max to be inf and -inf, so
	# we ensure we will find any value no matter what. 
	minOutOfOrder = float("inf")
	maxOutOfOrder = float("-inf")
	
	for i in range(len(array)):
		num = array[i]
		
		# IMPORTANT: for this cases, use helper/utility functions
		# If the number is out of order (incorrected sort), then we want
		# to track the smallest number of that subarray
		if isOutOfOrder(i,num,array):
			minOutOfOrder = min(minOutOfOrder, num)
			maxOutOfOrder = max(maxOutOfOrder, num)
		
	# if we have a sorted array we deal with an edge case. what will tell us
	# is ordered or not is the minOutOfOrder and maxOutOfOrder
	
	if minOutOfOrder == float("inf"):
		return [-1,-1]
	
	# next we need to find in which position should we put the min and max out of order.
	# to do so we can traverse the array index and increment the value until find it!
	
	# left side:
	subarrayLeftIdx = 0
	while minOutOfOrder >= array[subarrayLeftIdx]:
		subarrayLeftIdx += 1
	
	# right side:
	subarrayRightIdx = len(array)-1
	while maxOutOfOrder <= array[subarrayRightIdx]:
		subarrayRightIdx -= 1
	
	return [subarrayLeftIdx, subarrayRightIdx]
	
		
def isOutOfOrder(i,num,array):
	# specific cases of extremes [0, ..., end]
	if i == 0:
		return num > array[i +1]
	if i == len(array)-1:
		return num < array[i-1]
	
	# check if the number is (<, num, <)
	return num > array[i+1] or num < array[i-1]


# ------ TESTING ------
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])

if __name__ == '__main__':
    unittest.main()