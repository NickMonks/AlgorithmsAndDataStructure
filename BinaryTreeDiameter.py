import unittest

# O(n) time | O(h) space (call stack space), O(n) worst
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
	return getTreeInfo(tree).diameter
	

def getTreeInfo(tree):
	
	# Base case, we return the child node (which is zero height, zero diameter)
	if tree is None:
		return TreeInfo(0,0)
	
	# We recursively call the left sub-tree and then the right one. Once we got the result
	# of the height and diameter, we apply our formula
	leftTreeInfo = getTreeInfo(tree.left)
	rightTreeInfo = getTreeInfo(tree.right)
	
	# we calculate the longest path (which it's essentialy the diameter) between two subtrees
	# initially it will be zero
	longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
	maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
	currentDiameter = max(longestPathThroughRoot, maxDiameterSoFar)
	
	# calculate current height, will is adding a +1 to the maximum height between right and left
	currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)
	
	# this will return the normal case of the left and right tree values (no base case)
	return TreeInfo(currentDiameter, currentHeight)
	

# We define a struct-like class to save the diameter and the height of each node
class TreeInfo:
	def __init__(self,diameter, height):
		self.diameter = diameter
		self.height = height
  
  

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.left.left = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        root.left.right = BinaryTree(4)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)
        root.right = BinaryTree(2)
        expected = 6
        actual = binaryTreeDiameter(root)
        self.assertEqual(actual, expected)


if __name__=="__main__":
    unittest.main()