import unittest

# O(n) time | O(d) space: d is the greatest depth of special array
def productSum(array, multiplier=1):
	sum = 0
	for element in array:
		if type(element) is list:
			sum += productSum(element, multiplier + 1)
		else:
			sum += element
	
	return sum * multiplier 

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
        self.assertEqual(productSum(test), 12)
        
if __name__ == "__main__":
    unittest.main()
