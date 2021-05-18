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