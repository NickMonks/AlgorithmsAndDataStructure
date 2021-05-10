import unittest

# ----- UNIT TEST SECTION --------

def testMinMaxPeek(self, min, max, peek, stack):
    self.assertEqual(stack.getMin(), min)
    self.assertEqual(stack.getMax(), max)
    self.assertEqual(stack.peek(), peek)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        stack = program.MinMaxStack()
        stack.push(5)
        testMinMaxPeek(self, 5, 5, 5, stack)
        stack.push(7)
        testMinMaxPeek(self, 5, 7, 7, stack)
        stack.push(2)
        testMinMaxPeek(self, 2, 7, 2, stack)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 7)
        testMinMaxPeek(self, 5, 5, 5, stack)

# ----- CODE SECTION

class MinMaxStack:
	def __init__(self):
        # Create an array of MinMax values; this will be stored every time we push
        # even if they are the same. when we pop, we will have tracked the reference of this
        # values
        self.minMaxStack =[]
        self.stack =[]

    # O(1) time | O(1) space	
    def peek(self):
            return self.stack[len(self.stack)-1]
    
    # O(1) time | O(1) space
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()
    
    # O(1) time | O(1) space
    def push(self, number):
        # we want to push, not only the new value but also populate
        # and push the new element of the minMaxStack. For that, we will first create
        # a hash table (a dictionary in Python).
            
        # Then, we create the new MinMax struct/hash table
        newMinMax = {"min": number, "max": number}
            
        # Check if the minmaxstack is empty
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) -1]
                
                #check the last value of the minMax array and extract min and max
                # with python builtin methods. 
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
                
            # append the value at the end of the array
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)
    
    # O(1) time | O(1) space	
    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack)-1]["min"]
        
    # O(1) time | O(1) space
    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack)-1]["max"]
    
if __name__ == '__main__':
    unittest.main()