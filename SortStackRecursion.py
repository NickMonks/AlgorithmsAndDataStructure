import unittest

# O(N^2) Time | O(N) Space
def sortStack(stack):
    # The problem of this problem is that we need to do this in place, using recursion. How do we do that?
	# the idea is that we will have two recursive functions: one that sorts the stack, or checks if it's sorted or not, and the insert method
	# first, we will pop up every element for each recursive call. then we hit base case (when the stack is empty); then we call the insert() method,
	# which takes the element popped up in that recursive that.
	# the insert method as an if statement, checking if the element is bigger than the top element. If it is, then insert it, if not that means it should ne in the middle
	# we pop the top value (which is greater than the current element), save it and perform a recursive call to insert. When we manage to insert the element, we return and 
	# try to insert the popped element.
	
	if len(stack) == 0:
		return stack
	
	top = stack.pop()
	
	# first, we pop the elements out and sort recursively:
	sortStack(stack)
	
	# once finished, we insert the top element again:
	insertInSortedOrder(stack, top)
	
	# finally, return the stack recursively:
	return stack

def insertInSortedOrder(stack, value):
	# check base case:
	if len(stack) == 0 or stack[-1] <= value:
		stack.append(value)
		return
	# else, if we are not returning that means the element value is smaller; we need to pop the top of the stack 
	# and recursively call the insert method
	
	top = stack.pop()
	insertInSortedOrder(stack,value)
	insertInSortedOrder(stack, top)
 
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [-5, 2, -2, 4, 3, 1]
        expected = [-5, -2, 1, 2, 3, 4]
        actual = sortStack(input)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()