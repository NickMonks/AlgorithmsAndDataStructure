import unittest

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(max(n,m))
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Initialize the head pointer of the new linked list
	# we initialize the head as 0
	newLinkedListHeadPointer = LinkedList(0)
	
	# set the pointer and carrier of the sum
	currentNode = newLinkedListHeadPointer
	carry = 0
	
	nodeOne = linkedListOne
	nodeTwo = linkedListTwo
	
	# Remember, is an OR: if both nodes are empty, but the carry is not null add it
	
	while nodeOne is not None or nodeTwo is not None or carry !=0:
		valueOne = nodeOne.value if nodeOne is not None else 0
		valueTwo = nodeTwo.value if nodeTwo is not None else 0
		
		sumOfValues = valueOne + valueTwo + carry
		
		newValue = sumOfValues % 10
		carry = sumOfValues // 10
		
		newNode = LinkedList(newValue)
		
		# Update the node to the sum and set the next pointer
		currentNode.next = newNode
		currentNode = newNode
		
		# finally, update the nodeOne and nodeTwo if not empty/tail
		
		nodeOne = nodeOne.next if nodeOne is not None else None
		nodeTwo = nodeTwo.next if nodeTwo is not None else None
	
	# return the next pointer of our dummy node
	return newLinkedListHeadPointer.next


#----unit test

class LinkedList(LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self


def getNodesInArray(output):
    nodes = []
    current = output
    while current is not None:
        nodes.append(current.value)
        current = current.next
    return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        ll1 = LinkedList(2).addMany([4, 7, 1])
        ll2 = LinkedList(9).addMany([4, 5])
        expected = LinkedList(1).addMany([9, 2, 2])
        actual = sumOfLinkedLists(ll1, ll2)
        self.assertEqual(getNodesInArray(actual), getNodesInArray(expected))

if __name__ == "__main__":
    unittest.main()