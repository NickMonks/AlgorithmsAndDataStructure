# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(1), O(1)
def findLoop(head):
    # For this algorithm, we will have two pointers:
    # 	- first: will move 1 step at a time
    # 	- second: 2 steps at a time
    #	Once we keep iterating, there will be a point were first and second will collide.
    #	If this happens, we have traverse the distance x = D + P (D: non-loop distance of 1 step, P: loop distance) for first pointer
    #	and second node x = 2D + 2P ( double the distance)
    # 	Assuming the total length of the linked list is T = D + P + R (where R is the remainder distance)
    #   And also that T = second - P = 2D + P, we can conclude that:
    #   2D + P = D + P + R -> R = 2D + P -D -P = D.
    #	Because D is the distance from [head, loop], we can move the first node to the beginning and move second one step
    #.  both of them. when they collide this is the node to start!
    
    first = head.next
    second = head.next.next
    
    while first != second:
        first = first.next
        second = second.next.next
    
    #when both pointers are pointing each other, we put the first pointer to
    # the beginning and then move both forward one by one, until we hit the first
    # pointer that starts the loop
    first = head
    
    while first != second:
        first = first.next
        second = second.next
    
    return first