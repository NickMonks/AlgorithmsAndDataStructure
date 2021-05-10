import unittest


# ----- CODE ANSWER ----------
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O (N) Time | O (N) Space
def branchSums(root):
	# declare an empty list here (in fact, that's why we create two functions)
	# if we had declared this one in the same function we would have problems
	
	sums = []
	calculateBranchSums(root, 0, sums)
	return sums

def calculateBranchSums(node, runningSum, sums):
	
	if node is None:
		return
	
	# sum the node value with the runningSum
	# body of the recursion function
	newRunningSum = runningSum + node.value
	
	# return conditions
	if node.left is None and node.right is None:
		sums.append(newRunningSum)
		return
	
	calculateBranchSums(node.left, newRunningSum, sums)
	calculateBranchSums(node.right, newRunningSum, sums)

class BinaryTree(BinaryTree):
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(branchSums(tree), [15, 16, 18, 10, 11])
        
if __name__ == '__main__':
    unittest.main()