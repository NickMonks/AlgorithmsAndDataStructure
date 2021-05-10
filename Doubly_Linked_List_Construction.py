# LinkedList is a wonderful data structure; insertion, remove, etc can be done in O(1) space and time
# the only place it fails is traversing and it's O(p)

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
	
	#  O(1) time | O(1) space
    def setHead(self, node):
        # If we deal with an empty linked list...
	    if self.head is None:
		    self.head = node
		    self.tail = node
		    return 
        
        # DONT FORGET TO RETURN!
		
		# ... otherwise, we should insert the node BEFORE the current head
		# so we need to implement the insertBefore!
		
	    self.insertBefore(self.head, node)
	
	#  O(1) time | O(1) space
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node) 
            # this will perform the first if statement, so we dont type the 3 same lines
            return
		
        self.insertAfter(self.tail, node)
			
	# O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        # IMPORTANT: define the edge cases. Is the linked list only of one element?
	    
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return # inserting the same node?
		
		#Since we are moving node, we delete it from the main linkedList
		# but since it's an argument we still keep track of it
        self.remove(nodeToInsert)
        
        nodeToInsert.prev = node.prev
        
        # the next value is the node, since we're inserting before
        nodeToInsert.next = node 
        
        # once the reference is updated, if the previous v
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert # the previous node of the before insertion, the next value will be our node (if it's not the head!!!)
        
        # since we are inserting before, the new node will be nodeToInsert
        # This is why order matters; if we did this before it wont work. 
        node.prev = nodeToInsert
        
            
        

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        
        node.next = nodeToInsert

    # O(p) time | O(1) space: p is the position where we want to insert the node
    def insertAtPosition(self, position, nodeToInsert):
        # the position is basically an index. 
        
        if position == 1:
            # set the head
            self.setHead(nodeToInsert)
            return
        
        node = self.head # keep a reference of the first node and traverse it
        currentPosition = 1
        
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        
        # once we reached the position, we need to check whether node is none or we found the position
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else: 
            # if is none, we are on the tail
            self.setTail(nodeToInsert)
        
    # O(n) time | O(1) space
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            # IMPORTANT: KEEP TRACK OF THE NODES!
            # if we remove the node, we will lose track of that node.next
            # so, what we do is create a temporal variable, nodeToRemove, which
            # is a reference to the node. so, we will remove the node and keep the 
            # next value in node.
            nodeToRemove = node
            node = node.next
            
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    # O (1) time | O(1) space
    def remove(self, node):
        # edge cases: are we dealing with a head or a tail?
        if (node == self.head):
            # if we remove the head, point the new head to the next value
            self.head = self.head.next 
        
        if (node == self.tail):
            self.tail = self.tail.prev
        
        self.removeNodeBindings(node)

    # O(n) time | O(1) space
    def containsNodeWithValue(self, value):
        # this is the search method
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    def removeNodeBindings(self, node):
        
        # make the previous node we had the next value
        # to be the next value of the node. This method works
        # even if we are a head or tail.
        
        # IMPORTANT: The order matters!, if you don't do it
        # like this you will lose the references. 
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
            
        # set up our node as None
        node.next = None
        node.prev = None
        
# ------ UNIT TEST

import unittest


class TestNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


def getNodeValuesHeadToTail(linkedList):
    values = []
    node = linkedList.head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values


def getNodeValuesTailToHead(linkedList):
    values = []
    node = linkedList.tail
    while node is not None:
        values.append(node.value)
        node = node.prev
    return values


def bindNodes(nodeOne, nodeTwo):
    nodeOne.next = nodeTwo
    nodeTwo.prev = nodeOne


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        linkedList = DoublyLinkedList()
        one = Node(1)
        two = Node(2)
        three = Node(3)
        three2 = Node(3)
        three3 = Node(3)
        four = Node(4)
        five = Node(5)
        six = Node(6)
        bindNodes(one, two)
        bindNodes(two, three)
        bindNodes(three, four)
        bindNodes(four, five)
        linkedList.head = one
        linkedList.tail = five

        linkedList.setHead(four)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 3, 5])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [5, 3, 2, 1, 4])

        linkedList.setTail(six)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 3, 5, 6])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 5, 3, 2, 1, 4])

        linkedList.insertBefore(six, three)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 5, 3, 6])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 3, 5, 2, 1, 4])

        linkedList.insertAfter(six, three2)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 5, 3, 6, 3])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [3, 6, 3, 5, 2, 1, 4])

        linkedList.insertAtPosition(1, three3)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [3, 4, 1, 2, 5, 3, 6, 3])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [3, 6, 3, 5, 2, 1, 4, 3])

        linkedList.removeNodesWithValue(3)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 5, 6])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 5, 2, 1, 4])

        linkedList.remove(two)
        self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 5, 6])
        self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 5, 1, 4])

        self.assertEqual(linkedList.containsNodeWithValue(5), True)
        

if __name__ == '__main__':
    unittest.main()