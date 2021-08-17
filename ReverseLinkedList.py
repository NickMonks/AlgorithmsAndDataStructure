# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # The trick of the problem is that we need to use three pointers, not two (which is the common pattern).
	# the first and third pointer act as a reference and the second one (P2) is the visited one. So, the condition is that when p2 is null, then we have
	# reversed the linked list. At the beginning we start with P1 = null (there's nothing on the left of P2), P2 as first element and p3 and the second one.
	# in order, the algorithm should do the following:
	# p2.next = p1
	# p1 = p2
	# p2 = p3
	# p3 = p3.next
	
	# Initialisation of p1 and p2
	p1, p2 = None, head
	
	
	while p2 is not None:
		# why we do this here? 
		# p2 as the tail of the LL, and so p3 is null; so we are doing None.next which will give an attr error
		# p3 = p2.next, we could do p3 = p3.next if not None else p3
		p3 = p2.next
		p2.next = p1
		p1 = p2
		p2 = p3
		
	
	# when p2 is pointing to none, p1 is the final element in the list, which is the new head!
	return p1