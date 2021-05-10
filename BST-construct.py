
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)

        root.insert(12)
        self.assertTrue(root.right.left.left.value == 12)

        root.remove(10)
        self.assertTrue(not root.contains(10))
        self.assertTrue(root.value == 12)

        self.assertTrue(root.contains(15))



#  This can be solved recursevly or iteratively; since iterative will
# require constant space O(1) we will go for this solution. 
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    #Time: O(log N), worst O (N)
    #Space: O(1), worst O (1)

    def insert(self, value):
        # Define a variable to keep track of what node are we right now
        currentNode = self
    
        #Infinite loop
        while True:
            if value < currentNode.value:
                #we explore left side
                if currentNode.left is None:
                    # if it's null that means we reach the leaf
                    currentNode.left = BST(value)
                    break
                else:
                    # we define the new node pointer to the left of the parent
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    # if it's null that means we reach the leaf
                    currentNode.right = BST(value)
                    break
                else:
                    # we define the new node pointer to the left of the parent
                    currentNode = currentNode.right
        
        # this allows to change methods! testBST.insert(1).insert(5)
        return self

    def contains(self, value):
        #Initialise the root node (or current node):
        currentNode = self
        
        # 
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                # if the value is equal, then return true
                return True
        
        return False

    def remove(self, value, parentNode = None):
        # to remove the node, we need to keep tract of the parent node
        # because in case 
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                #we found the node. We need to address this according to the edge cases
                # 1. the Node is not a left and has right and left values
    
                if currentNode.left is not None and currentNode.right is not None:
                    # the actual value of that node will be substituted for the min value
                    # of the right side of the branch!
                    currentNode.value = currentNode.right.getMinValue()
                    # and now we delete the smallest value of the right subtree
                    # we call this recursevely. we pass the value we want to delete,
                    # on the right subtree (that's why we call it on currentNode.right)
                    # and the parent is the currentNode. 
                    currentNode.right.remove(currentNode.value, currentNode)
                
                # root node
                elif parentNode is None:
                    if currentNode.left is not None:
                        # change the value to the left value
                        # (!) we changed the value, but the right and left references are the same as previous
                        currentNode.value = currentNode.left.value
                        
                        # be very careful of not overwriting the currentNode.left before,
                        # since currentNode is used for assigning and we don't want to mix it
                        currentNode.right = currentNode.left.right # currentNode.left is the new root
                        currentNode.left = currentNode.left.left
                        
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left # currentNode.left is the new root
                        currentNode.right = currentNode.right.right
                    # extreme edge case: there is no more nodes - we delete the BST
                    else:
                        pass
            
                # if we found the value and either left or right side is null...
                # we check in which side is the child.
                
                # This is where we will enter if the remove is been called recursevely
                # and only if it's a leaf!ß
                elif parentNode.left == currentNode:
                    # if the node we want to remove is on the left side of the parent
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                
                break
        return self
        
    def getMinValue(self):
        currentNode = self
        #we traverse on the leftmost side of the binary tree to find the value
        while currentNode.left is not None:
            currentNode = currentNode.left
        # when the left is null, return the value (it is a leaf)
        return currentNode.value


if __name__ == '__main__':
    unittest.main()