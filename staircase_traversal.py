import unittest

#--- RECURSIVE SOLUTION (No memoization)

def staircaseTraversal(height, maxSteps):
    return staircaseCounter(height, maxSteps)


def staircaseCounter(height, maxSteps):
	if height <=1:
		return 1
	
	count = 0
	for step in range(1,min(maxSteps, height)+1):
		count += staircaseCounter(height - step, maxSteps)
		
	return count

#---- RECURSIVE SOLUTION (With memoization):
def staircaseTraversal2(height, maxSteps):
    return staircaseCounter2(height, maxSteps, {0:1, 1:1})

def staircaseCounter2(height, maxSteps, memoize):
	if height in memoize:
		return memoize[height]
	
	count = 0
	for step in range(1,min(maxSteps, height)+1):
		count += staircaseCounter2(height - step, maxSteps, memoize)
	
	memoize[height] = count
	return count


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        stairs = 4
        maxSteps = 2
        expected = 5
        actual2 = staircaseTraversal2(stairs, maxSteps)
        actual = staircaseTraversal(stairs, maxSteps)
        
        self.assertEqual(actual2, expected)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()