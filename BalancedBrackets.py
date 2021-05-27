import unittest

def balancedBrackets(string):
    	# First, we defined two arrays for opening brackets and closing brackets
	# This eases the work of using "if"statements:
	openingBrackets = "([{"
	closingBrackets = ")]}"
	
	# then we define a hash table/dictionary, which matches each opening bracket with its
	# closing bracket
	matchingBrackets = {")":"(", "]":"[", "}":"{"}
	stack = []
	
	for char in string:
		# TIP: to check if a char is in a string use the "in" keyword
		if char in openingBrackets:
			stack.append(char)
		elif char in closingBrackets:
			# first, check that stack is not empty (if it is empty then the next condition would fail!)
			if len(stack)== 0:
				return False
			if stack[-1] == matchingBrackets[char]:
				stack.pop()
			else:
				return False
	
	# When we finish to iterate, check if there are not elements in the array
	return len(stack) == 0

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(balancedBrackets("([])(){}(())()()"), True)

if __name__ == "__main__":
    unittest.main()