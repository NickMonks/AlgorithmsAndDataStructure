
import unittest
# --- METHODS TO TRAVERSE A BST

# O(n) time | O(n) space
def inOrderTraverse(tree, array):
	# The important think is to translate the data into: first left node, then value, then right node. 
	
	# When the tree is none, return the array that we are appending to a previous
	# step. This is key in recursion (if we're manipulating an array, return the element we're modifying)
	if tree is not None:
		# go only to the left, until reaching a value. Once we append look on the right and keep looking the left
		inOrderTraverse(tree.left, array)
		array.append(tree.value)
		inOrderTraverse(tree.right, array)
	return array

# O(n) time | O(n) space
def preOrderTraverse(tree, array):
	# First value, then left node, then right node
	if tree is not None:
		array.append(tree.value)
		preOrderTraverse(tree.left, array)
		preOrderTraverse(tree.right, array)
	
	return array


# O(n) time | O(n) space
def postOrderTraverse(tree, array):
	if tree is not None:
		postOrderTraverse(tree.left, array)
		postOrderTraverse(tree.right, array)
		array.append(tree.value)
	
	return array



class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.right = BST(22)

        inOrder = [1, 2, 5, 5, 10, 15, 22]
        preOrder = [10, 5, 2, 1, 5, 15, 22]
        postOrder = [1, 2, 5, 5, 22, 15, 10]

        self.assertEqual(inOrderTraverse(root, []), inOrder)
        self.assertEqual(preOrderTraverse(root, []), preOrder)
        self.assertEqual(postOrderTraverse(root, []), postOrder)

if __name__ == "__main__":
    unittest.main()