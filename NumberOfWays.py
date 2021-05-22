import unittest

# Time : O(nd), d: denominations | Space: O(n)
def numberOfWaysToMakeChange(n, denoms):
	# In order to solve this problem, we use dynamic programing, where
	# we define an array of ways= [0,...,n] and we traverse it for each denomination
	
	ways = [0 for amount in range(n+1)]
	
	# ways of 0 amount is 1, which is ... none
	ways[0] = 1
	# the recursive formula that we can reach using this relationship is:
	# ways[i] += ways[i-denom]
	
	for denom in denoms:
		for amount in range(1, n+1):
			# here we check that the denom is less or equal to the amount 
			# if it's less then we skip it, we can't change it 
			if denom <= amount:
				ways[amount] += ways[amount-denom]
	
	return ways[n]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(numberOfWaysToMakeChange(6, [1, 5]), 2)

if __name__ == "__main__":
    unittest.main()