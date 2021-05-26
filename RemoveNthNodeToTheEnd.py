import unittest


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(1) space
def removeKthNodeFromEnd(head, n):
	first = head
	second = head
	counter =1
	
	# We create two pointers, one ahead of the other to n nodes
	# F                   S
	# 0 -> 1 -> 2 -> 3 -> 4
	
	while counter <= n:
		second = second.next
		counter +=1
	
	# Edge case: imagine that we reach the null value just when it finishes
	# so essentially we are deleting the head node.
	if second is None:
		head.value = head.next.value
		head.next = head.next.next
		return
	
	#If is not point to the next value, we move the first node in the same pace
	# when while loop breaks, first is pointing to the node to be removed. 
	while second.next is not None:
		second = second.next
		first = first.next
	
	# Remove the nth node
	# IMPORTANT: WE BREAK THE LOOP ON THE SECOND.NEXT!, so we're pointing to n-1 node
	first.next = first.next.next
	return

# ---- UNIT TEST

linkedListClass = LinkedList


class LinkedList(linkedListClass):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected = LinkedList(0).addMany([1, 2, 3, 4, 5, 7, 8, 9])
        removeKthNodeFromEnd(test, 4)
        self.assertEqual(test.getNodesInArray(), expected.getNodesInArray())

if __name__ == "__main__":
    unittest.main()