import unittest

# Time : O(n log n) | Space: O(n log n)
def mergeSort(array):
    # merge sort without optimizing space is far easier than the swap version of the algorithm

	if len(array) == 1:
		return array
	
	# divide-nad-conquer: divide the array in two (floor)
	middleIdx = len(array) // 2 # left will be equal or bigger than right subarray
	leftHalf = array[:middleIdx]
	rightHalf = array[middleIdx:]
	
	# next we keep dividing them over and over but within the merge sorted Arrays function, to merge them
	# so we call each mergeSort, which splits the subarrays, and calls the merge algorithm. It is important to notice
	# that the logic of the function below works simply both subarrays have been internally sorted and we can loop and compare them
	return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))

def mergeSortedArrays(leftHalf, rightHalf):
	# we use pointers to order the elements in a new array (here's where the penalization of space comes)
	# this array is initialize as an array of null values
	sortedArray = [None] * (len(leftHalf) + len(rightHalf))
	# initialize pointers to be k: currentindex of sorted array, i: left, j: right
	k = i = j = 0
	
	# as long as both index are less than the length of its subarrays...
	while i < len(leftHalf) and j < len(rightHalf):
		if leftHalf[i] <= rightHalf[j]:
			sortedArray[k] = leftHalf[i]
			i += 1
		else:
			sortedArray[k] = rightHalf[j]
			j += 1
		
		k += 1
	# we ended one of the sub-arrays, the next step is to find the non empty subarray and keepa adding
	# the elements
	while i < len(leftHalf):
		sortedArray[k] = leftHalf[i]
		i += 1
		k += 1
	
	while j < len(rightHalf):
		sortedArray[k] = rightHalf[j]
		j += 1
		k += 1
	
	return sortedArray


def mergeSort2(array):
    if len(array) <= 1:
        return array
    
    # create a copy of the array, the auxiliar array, which will be switched in the helper method.
    # It receives the aux and main array, and pointers to the starting index,and end index
    
    auxiliaryArray = array[:]
    mergeSortHelper(array,0, len(array)-1, auxiliaryArray)
    
    return array

def mergeSortHelper(mainArray,startIdx, endIdx, auxiliaryArray):
    # if they are the same index, return directly
    if startIdx == endIdx:
        return
    
    middleIdx = (startIdx + endIdx) // 2
    
    # now here we swap the aux and the main. Why?, because when we hit the base case, we will call 
    # another method which will use the auxiliary array as a reference with two pointers (starting
    # at the beginning of the subarrays) and compare, similar to the first solution. Because we update
    # ALL the main element of the function, this help us to keep track, and reorder Aux to be used in the upper case. 
    mergeSortHelper(auxiliaryArray, startIdx, middleIdx, mainArray)
    mergeSortHelper(auxiliaryArray, middleIdx + 1, endIdx, mainArray)
    
    # finally, we call doMerge
    doMerge(mainArray,startIdx, middleIdx, endIdx, auxiliaryArray)

def doMerge(mainArray,startIdx, middleIdx, endIdx, auxiliaryArray):
    # we can define three pointers based on the start of the left subarray and right subarray. The left is the starting index,
    # the currentIndex we check is also start and the right is middle. 
    k = startIdx
    i = startIdx
    j = middleIdx + 1
    
    while i <= middleIdx and j <= endIdx:
        # here we compare the index of start of both subarrays in the aux array, and update main accordingly
        if auxiliaryArray[i] <= auxiliaryArray[j]:
            mainArray[k] = auxiliaryArray[i]
            i += 1
        else:
            mainArray[k] = auxiliaryArray[j]
            j += 1
        k += 1
        
    while i <= middleIdx:
        mainArray[k] = auxiliaryArray[i]
        i += 1
        k += 1

    while j <= endIdx:
        mainArray[k] = auxiliaryArray[j]
        j += 1
        k += 1

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(mergeSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])

    def test_case_2(self):
        self.assertEqual(mergeSort2([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])

if __name__ == "__main__":
    unittest.main()