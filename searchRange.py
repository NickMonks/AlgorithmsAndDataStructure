# O(log N) time | O (log N) space
def searchForRange(array, target):
    # To solve this algorithm, we basically perfom binary search in the array. When we find the target, we need to find the extreme.
	# so, for the left subarray we check if M = 0; if it is, is deffo the left extreme. Else, we check if array[M-1]= target. If it is, then perform binary search recursively, and apply the same logic
	# do this for the right subarray, check if M = len(array), if not check if array[M+1] = target, if it is do binary search
	
	# initialise the range to be -1, -1
	finalRange = [-1,-1]
	
	# perform binary search and then look at the LEFT - we decide this by another parameter called goLeft
	alteredBinarySearch(array, target, 0, len(array) -1, finalRange, True)
	
	# perform binary search and then look at the RIGHT - we decide this by another parameter called goLeft
	alteredBinarySearch(array, target, 0, len(array) -1, finalRange, False)
	
	return finalRange

def alteredBinarySearch(array, target, left, right, finalRange, goLeft):
	# we define our base case - when the left is bigger or equal to right:
	if left > right:
		return # we do not return anything
	
	mid = (left + right) // 2
	
	if array[mid] < target:
		alteredBinarySearch(array, target, mid + 1, right, finalRange, goLeft)
	elif array[mid] > target:
		alteredBinarySearch(array, target, left, mid -1, finalRange, goLeft)
	else:
		# when we found target, the new logic comes - are we going left or right?
		if goLeft:
			# first, check if we are at the extreme - is mid = 0?, if so just return - this is an extreme, so update finalRange
			# equally if the left element is not equal to target, is the extremity
			if mid == 0 or array[mid -1] != target:
					# this is the other "base case"
					finalRange[0] = mid
			else:
				# further explore the left subarray
				alteredBinarySearch(array, target, left, mid -1, finalRange, goLeft)
		else:
			if mid == len(array) - 1 or array[mid +1] != target:
				finalRange[1] = mid
			else:
				alteredBinarySearch(array, target, mid +1, right, finalRange, goLeft)

def alteredBinarySearchIterative(array, target, left, right, finalRange, goLeft):
    # We simply change the if condition to be a while loop, and update the boundaries of left and right pointers
	while left <= right:

		mid = (left + right) // 2

		if array[mid] < target:
			# update boundaries
			left = mid +1
		elif array[mid] > target:
			right = mid -1 
		else:
			# when we found target, the new logic comes - are we going left or right?
			if goLeft:
				# first, check if we are at the extreme - is mid = 0?, if so just return - this is an extreme, so update finalRange
				# equally if the left element is not equal to target, is the extremity
				if mid == 0 or array[mid -1] != target:
						# this is the other "base case"
						finalRange[0] = mid
						return
				else:
					# further explore the left subarray
					right = mid -1 
			else:
				if mid == len(array) - 1 or array[mid +1] != target:
					finalRange[1] = mid
					return
				else:
					left = mid + 1