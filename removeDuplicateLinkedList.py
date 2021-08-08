# O(n) time | O(1) space
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # linkedList is the head of the linkedList
	currentNode = linkedList
	
	while currentNode is not None:
		nextDistinctNode = currentNode.next
		
		# if the nextDistinctNode is not equal to currentNode, we want to point the currentNode.next to this one
		while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
			nextDistinctNode = nextDistinctNode.next
		
		# if the nextDistinctNode is none, that means we reach the end and therefore we can point the next currentnode 
		# to be none (i.e. the tail, we can collapse all the elements in between) and update currentNode.next, which is none
		# and will break out the while loop
		currentNode.next = nextDistinctNode
		currentNode = currentNode.next
		
	return linkedList 