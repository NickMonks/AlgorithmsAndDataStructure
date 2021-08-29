# O(n) time | O(n) space
def nextGreaterElement(array):
    # to solve this problem, we could perform a brute-force approach solution; however this would take O(n^2) time.
	# so we can create a solution which uses a bit of space: use of stacks. we can provide two solutions:
	# FIRST SOLUTION: initialise an array with -1's and length the original array. Then what we do is create a stack where we push the elements of the array in the following way:
	# - i = 0: push the first index of the element, in this case 0.
	# - If array[i] < top of the stack, then we push the index i to the top of the stack. 
	# - If array[i] > top of the stack, then the update results at the index of the top of the stack to be array[i] and pop the top of the stack. Traverse the stack until finding is not bigger or empty.
	# for either case, we will push the index i. 
	# since the array is circular (the end connects with the beginning), we need to do a for loop of double range, and use the mod operator to take the correct index. When that for loop ends we simply return result. 
	
	result = [-1] * len(array)
	stack = []
	
	for idx in range(2* len(array)):
		# when we reach the second iteration of the circular array, we want to go back using the mod operator
		circularIdx = idx % len(array)
		
		# we will have a while loop that iterates through the stack for every index i, only if the stack is not empty
		# AND the array[top of the stack], where the top is at the end of the array (len(array) minus one) is less than the element at idx:
		while len(stack) > 0 and array[stack[len(stack) - 1]] < array[circularIdx]:
			# the next element is the next greater element, so we pop the element (which is the index),
			# and we give the result output. 
			top = stack.pop()
			result[top] = array[circularIdx]
		
		stack.append(circularIdx)
	return result