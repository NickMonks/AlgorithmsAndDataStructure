import unittest

def nodeDepths2(root, depth = 0):
    # handle base case
    if root is None:
        return 0 
    # Recursive formula: f(n,d) = d + f(l, d+1) + f(r, d+1)
    # remember: we use use root.left and root.right but it will be recursively to root.left.left.[...]
    return depth + nodeDepths2(root.left, depth + 1) + nodeDepths2(root.right, depth + 1)
    


# For this solution, an alternative approach is used: we will store
# for each node a hash table (dictonary in python, HashMap in Java)
# of the node itself AND THE DEPTH

# HINT: How to come up with this solution? Simply try to think ; if you need an ordered
# data structure with more than one field, choose a combination of Hash Table + X

# Time: O(n) | Space : O(h) -> if we check the stack, the size it will be roughly the height of the tree
def nodeDepths(root):
    sumOfDepths = 0
    
    # For this solution, we will store each node with a dictionary of node and depth
    stack = [{"node": root, "depth":0}]
    
    # The approach will be the following:
    # - Append each node child: left and right, inside a stack, with the correspondent parent depth +1
    # - Extract each time we loop a node with the node and depth:
    #   * If Node = None , then ignore and don't add the depth (that means it is a leaf)
    #   * If exists, add the depth
    #
    # Since we popped the node, it wont iterate more
    # WHILE CONDITION: Until the stack length is zero (that means we pop all the possible options)
    while len(stack) > 0:
        nodeExtract = stack.pop()
        node, depth = nodeExtract["node"], nodeExtract["depth"]
        if node is None:
            continue
        sumOfDepths += depth
        stack.append({"node": node.left, "depth": depth+1})
        stack.append({"node": node.right, "depth": depth+1})
    return sumOfDepths
        
        
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#---- UNIT TEST
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.left.right = BinaryTree(9)
        root.left.right = BinaryTree(5)
        root.right = BinaryTree(3)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        actual = nodeDepths(root)
        self.assertEqual(actual, 16)

if __name__=='__main__':
    unittest.main()