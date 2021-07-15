# O(n) time | O(n) space
def sortedSquaredArray(array):
    # First, we need to realize that the array CAN contain negative values; so even if it's ordered
	# the sqaure won't be. to solve this, we know that the array is still ordered, and we now for a fact
	# that the most negative value of the left is, in reality, the biggest value sqaure for negative numbers
	# Therefore we can basically use this info and perform comparison using two pointers: comparing leftIdx with rightIdx
	# if abs(left) < right, then we know that biggest element between two ends must be in the right (and because is ordered, we can assume is the
	# bigges in our list).
	
	sortedSquares = [0 for _ in array]
	smallerValueIdx = 0
	largerValueIdx = len(array) - 1
	
	for idx in reversed(range(len(array))):
		smallerValue = array[smallerValueIdx]
		largerValue = array[largerValueIdx]
		
		if abs(smallerValue) > abs(largerValue):
			sortedSquares[idx] = smallerValue ** 2
			smallerValueIdx +=1
		else:
			sortedSquares[idx] =largerValue ** 2
			largerValueIdx -= 1
	
	return sortedSquares
	