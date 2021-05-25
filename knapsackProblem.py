import unittest

# O (nc) time | O (nc) Space
def knapsackProblem(items, capacity):
	# As many dynamic programming problems, and given that we know that
	# the limitation is the capacity , we will build an array of capacities:
	# if capacity is 10, create an array of 0,1,2,3,4...,10
	# After that, create a column of every element possible in the knapsack.
	# Normally in this problems, we should add the empty array for the base case
	# After that, we will store inside this matrix the value of each knapsack
	# as we progress downward, we will add or not the actual item:
	#
	# if weight > j, take value from previous row
	# if weight < j, then apply the following formula:
	# values[i][j] = max (values[i-1][j], values[i-1][j-w]+ value) (first case means we dont add it, and second case we add it)
	#
	# After that, we will reach the max value at the rightmost part of the matrix.
	# to check which items we added, we backtrack:
	#
	# is values[i-1][j]==values[i][j]? No -> append items[j] and move to values[i-1][j-w]
	# 			"           "		 ? Yes -> move to values[i-1][j]
	
	
	# initialize knapsack matrix (we add the "+1" to deal with the 0 element:0, 10)
	knapsackValues = [[0 for x in range(0, capacity + 1)] for y in range(0, len(items) +1)]
	for i in range(1, len(items) + 1):
		currentWeight = items[i - 1][1]
		currentValue = items[i - 1][0]
		for c in range(0, capacity + 1):
			if currentWeight > c:
				# if the weight is bigger than capacity, just take value of prev row
				knapsackValues[i][c] = knapsackValues[i - 1][c]
			else:
				knapsackValues[i][c] = max(
					knapsackValues[i - 1][c], 
					knapsackValues[i - 1][c - currentWeight] + currentValue
				)
		
	return [knapsackValues[-1][-1], 
				genKnapsackItems(knapsackValues, items)]

def genKnapsackItems(knapsackValues, items):
	sequence = []
	i = len(knapsackValues) - 1
	c = len(knapsackValues[0]) -1
	
	# the index of last row is len(knapsackValues) - 1
	# we will go up unitl is zero, therefore we use a while loop
	while i > 0:
		if knapsackValues[i][c] == knapsackValues[i-1][c]:
			i -= 1
		
		else:
			sequence.append(i-1)
			# substract the current capacity with the item weight
			c -= items[i-1][1]
			i -= 1
		
		if c==0:
			break
	
	return(list(reversed(sequence)))

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10), [10, [1, 3]])

if __name__ == "__main__":
    unittest.main()