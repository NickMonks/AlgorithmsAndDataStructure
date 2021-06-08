import unittest

# O(N^3 + M) time | O(N +M) Space
def numbersInPi(pi, numbers):
	
	# we define this hash table to check if the number exists or not when we tryn to search the min spaces
	numbersTable = {number: True for number in numbers}
	
	# we use the left-to-right approach (right approach is bottom-up)
	
	# we store each number with the minimum space in between of the slice of pi as a hash table, which 
	# has a fast access of O(1) on amortized analysis. We defined it as 'cache' and an empty dictionary.
	minSpaces = getMinSpaces(pi, numbersTable, {}, 0)
	
	# if there is no way, return -1: 
	return -1 if minSpaces == float("inf") else minSpaces


def getMinSpaces(pi, numbersTable, cache, idx):
	# base case
	if idx == len(pi):
		# we return -1, because each recursive call we are adding a new space; but in fact the last iteration
		# should have zero spaces, not 1. therefore to cancel it out we return a -1
		return -1
	
	if idx in cache:
		return cache[idx]
	
	# we initialize the minimum spaces to a high number. In python, we can do this as float("inf")
	minSpaces = float("inf")
	
	# for loop from the idx, which will be re-defined
	for i in range(idx, len(pi)):
		
		# prefix takes the number from left to right
		prefix = pi[idx:i +1] # we add +1 because :i excludes the i
		
		# we loop over i until finding a prefix valid
		if prefix in numbersTable:
			
			# if the prefix is in the numbersTable, as 3141592 and we have 31 as preffix, 
			# we want to check after i (i.e after length of preffix)
			minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i + 1)
			
			# we are recursively calling the getMinSpaces, and it will return a number of spaces of the entire pi.
			# We need to keep track of the minimum of these spaces. 
			
			# when we hit the base case, we will return -1, and -1 +1 = 0 -> zero spaces is the minimum of a prefix
			# then recursion will keep returning the value
			minSpaces = min(minSpaces, minSpacesInSuffix+1)
	
	cache[idx] = minSpaces
	return cache[idx]

PI = "3141592653589793238462643383279"


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        numbers = ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]
        self.assertEqual(numbersInPi(PI, numbers), 2)

if __name__ == "__main__":
    unittest.main()