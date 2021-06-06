import unittest

# Best Time : O(n log n) | space O(n log n)
def quickSort(array):
	# Explanation of quick sort: we use the Quick sort technique, which consist of declaring
	# three pointers: the pivot (P), which is the number we will sort, Left (L)
	# which is the leftmost element of the subarray , and Right (R). The following conditions shall apply:
	# while R > L:
	# 	If L < R -> move +1
	# 	If R > P -> move -1
	# when while breaks, swap R with P.
	# then call the quick sort algorithm recursively on the subarray on the left side of the pivot and the right
	# base case will be when the len of the subarray is one; in that case, we ensure is bein sorted.
	# For our example, we will set the pivot to be at the begining. 
	quickSortHelper(array, 0, len(array)-1)
	return array


def quickSortHelper(array, startIdx, endIdx):
	# because we call this recursively, we need to know the bounds on the left and right. 
	if startIdx >= endIdx:
		return # base case: len(1), or that start and end is the same
	
	# we will place the start pivot always at the leftmost
	pivotIdx = startIdx
	leftIdx = startIdx + 1
	rightIdx = endIdx
	
	while rightIdx >= leftIdx:
		
		# we check if we need to swap or not
		if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
			swap(leftIdx, rightIdx, array)
		
		# otherwise, check if we need to swap right or left:
		if array[leftIdx] <= array[pivotIdx]:
			leftIdx += 1
		if array[rightIdx] >= array[pivotIdx]:
			rightIdx -= 1
	
	# when while breaks, we swap the pivot:
	# REMEMBER WE SWAP THE ARRAY[IDX], NOT THE ACTUAL POINTER
	swap(pivotIdx, rightIdx, array)
	
	# and finally, we call quick sort recursively. Due to space complexity, we want to call it always
	# on the smallest subarray first.
	# rightIdx points to the right of the left pointer, so we have to delete 1, and we check if is smaller than
	# the other section.
	leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
	 
	if leftSubarrayIsSmaller:
		quickSortHelper(array, startIdx, rightIdx -1)
		quickSortHelper(array, rightIdx +1 , endIdx)
	else:
		quickSortHelper(array, rightIdx +1 , endIdx)
		quickSortHelper(array, startIdx, rightIdx -1)


def swap(i, j, array):
	array[i], array[j] = array[j], array[i]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(quickSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])

if __name__ == "__main__":
    unittest.main()