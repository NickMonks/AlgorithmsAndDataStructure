import unittest

# O(n*2^n) time | O(n*2^n) space
def powerset(array):
    	# first, we define our empty array of subsets
	# we include the empty array [] also:
	subsets = [[]]
	
	# for each element in the array, we do a for loop
	# and we append it to the current subset. With this, we can get
	
	for ele in array:
		for i in range(len(subsets)):
			currentSubset = subsets[i]
			subsets.append(currentSubset + [ele])
	
	return subsets

# ------ RECURSIVE SOLUTION ----------
def powerset2(array, idx = None):
    	# Basically in this problem, what we do is: generating all subsets of 
	# one element, then add the second, then all subsets + third element...
	# that is a formula: 
	# P([1,2,3....X]) = P(1,2,3,...., X-1) + [X]
	
	
	if idx is None:
		# In the first iteration, idx = none, so we set the index to the 
		# last element of the array
		idx = len(array)-1
	elif idx < 0:
		# since we will keep recursively calling P(...) + X until reaching base case
		# we will return the empty array
		return [[]]
	
	ele = array[idx]
	# We will recursively call each subsets once we reach the base case
	# first case: [] array, and then we loop over every subset and append the element
	# we extracted
	subsets = powerset2(array, idx-1)
	
	for i in range(len(subsets)):
		currentSubset = subsets[i]
		subsets.append(currentSubset + [ele])
	
	return subsets


# --- UNIT TEST --------
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = list(map(lambda x: set(x), powerset([1, 2, 3])))
        self.assertTrue(len(output) == 8)
        self.assertTrue(set([]) in output)
        self.assertTrue(set([1]) in output)
        self.assertTrue(set([2]) in output)
        self.assertTrue(set([1, 2]) in output)
        self.assertTrue(set([3]) in output)
        self.assertTrue(set([1, 3]) in output)
        self.assertTrue(set([2, 3]) in output)
        self.assertTrue(set([1, 2, 3]) in output)

if __name__ == "__main__":
    unittest.main()