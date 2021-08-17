# o(n^4) Time | O(1) space
def maximizeExpression1(array):
    # to solve this problem, we can do a brute force approach (which will imply to use 4 nested for loops, so (N^4) Time complexity),
	# or using dynamic programming. We need to understand that we want to maximise the expression a-b+c-d. Translated, this means:
	# I want to maximize first a, then a-b, then a-b+c, and finally a-b+c-d.
	# so what we can do is to create an auxiliary data structure that stores first the maximum possible value of a.
	# then, we can traverse the original array and find the maximum value of a-b in another auxiliary ds, and keeping doing that
	# until reaching last value of a-b+c-d.
	
	# BRUTE FORCE APPROACH
	# first, we check the length is bigger than 4, otherwise we return 0:
	if len(array) < 4:
		return 0
	
	maximumValueFound = float('-inf')
	
	for a in range(len(array)):
		aValue = array[a]
		for b in range(a+1, len(array)):
			bValue = array[b]
			for c in range(b+1, len(array)):
				cValue = array[c]
				for d in range(c+1, len(array)):
					dValue = array[d]
					expressionValue = aValue - bValue + cValue - dValue
					maximumValueFound = max(maximumValueFound, expressionValue)
	
	return maximumValueFound

# O(N) Time | O(N) Space   
def maximizeExpression(array):
    
    if len(array) < 4:
        return 0
    
    maxOfA =[array[0]]
    maxOfAMinusB = [float('-inf')]
    maxOfAMinusBPlusC = [float('-inf')] * 2 #!!! Multiply list to expand them
    maxOfAMinusBPlusCMinusD = [float('-inf')] * 3
    
    # fill the array of A:
    for idx in range(1, len(array)):
        # here, we find the currentMax value, which essentially is looking the previous value of the maxofA array,
        # and the element at array at idx 
        currentMax = max(maxOfA[idx -1], array[idx])
        maxOfA.append(currentMax)
    
    # fill the array of A - B:
    for idx in range(1, len(array)):
        # here we check which is the current max, if it's the previous value or is equal to maxOfA at idx-1 (idx -1 because we chose a amongst elements between 0...idx-1)
        # MINUS the current element
        currentMax = max(maxOfAMinusB[idx -1], maxOfA[idx-1] - array[idx])
        maxOfAMinusB.append(currentMax)
    
    # fill the array of A - B + C:
    # We start at 2 because we have two -inf
    for idx in range(2, len(array)):
        # here we check which is the current max, if it's the previous value or is equal to maxOfA at idx-1 (idx -1 because we chose a amongst elements between 0...idx-1)
        # MINUS the current element
        currentMax = max(maxOfAMinusBPlusC[idx -1], maxOfAMinusB[idx-1] + array[idx])
        maxOfAMinusBPlusC.append(currentMax)
    
    # fill the array of A - B + C:
    # We start at 2 because we have three -inf
    for idx in range(3, len(array)):
        currentMax = max(maxOfAMinusBPlusCMinusD[idx -1], maxOfAMinusBPlusC[idx-1] - array[idx])
        maxOfAMinusBPlusCMinusD.append(currentMax)
    
    # return last value of the array:
    return maxOfAMinusBPlusCMinusD[len(maxOfAMinusBPlusCMinusD) - 1]