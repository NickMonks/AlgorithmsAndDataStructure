def maxSumIncreasingSubsequence(array):
    # To solve this problem, we use dynamic programming, following our intuition and some basic rules typical of dp:
	# - Create an auxiliary data structure the size of the input, which will be used iteratively over the input
	# - perform an operation using the input AND the previous acumulated values, and find a min/max relationship
	# - keep track of the max/min value
	
	
	# In this case, we store the max sum of each previous element. So, starting from the first element the greatest sum is 8.
	# next element, check if the previous numbers are less than my current number. If so, add it. do that until finding a sum that is greatest than the greatest value
	# In this case we need to return also the values that are added on the sum, so a good idea is to create another array that stores the index of the previous value. When we find None
	# means there are no other numbers
	
	# we create the sums array and sequence array:
	sequences = [None for x in array]
	
	# this is important; we basically create a copy because in the for loop, if we dont find an element that
	# satisfies the conditions then we simply return the value itself (in this case, we do not return)
	sums = array[:] 
	
	#keep track of the max Sum idx:
	maxSumIdx = 0
	
	for i in range(len(array)):
		# take the element from the original array...
		currentNum = array[i]
		# ... and check all previous numbers 
		for j in range(0,i):
			
			# first, check if the element we are looking at is strictly less than the current number. Then,
			# if the sum of the element + sums[j] is greater than the sum of index i,
			otherNum = array[j]
			
			if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
				sums[i] = sums[j] + currentNum
				sequences[i] = j
	
		if sums[i] >= sums[maxSumIdx]:
			maxSumIdx = i
	
	# we need to return an array of : max SUm idx and the elements in ascending order. we use a buildSequence function for that
	return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]

def buildSequence(array, sequences, currentIdx):
	#initialise the sequence
	sequence = []
	
	# keep track of the current idx; when we find none means there are no other elements that links it
	while currentIdx is not None:
		sequence.append(array[currentIdx])
		#update currentIdx to the next one
		currentIdx = sequences[currentIdx]
	
	return list(reversed(sequence))