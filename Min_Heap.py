# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # we will implement the min heap with the sift down method
        # first we pick the first parent, which is in fact at the bottom
        
        # Remember that we're talking about the index
        # IMPORTANT: we write a "-2" so in the for loop the parent appears
        # Otherwise it will jump to the next one 
        firstParentIdx = (len(array)-2)//2
        print(firstParentIdx)
        
        # IMPORTANT: We need to remember that the parent are in the first
        # section of the array, and all the values that are previous to the previous
        # parent are adjacent. Therefore, if we do a reverse loop we can go into every parent
        
        for currentIdx in reversed(range(firstParentIdx+1)):
            
            self.siftDown(currentIdx, len(array)-1, array)
        return array
        
    def siftDown(self, currentIdx, endIdx, heap):
        
        # define the child positions:
        childOneIdx = currentIdx * 2 + 1
        
        # as soon as the Idx is bigger than the endIdx then stop
        # that means we have found a leaf node
        while childOneIdx <= endIdx:
            # then we calculate the child two, BUT ONLY IF the len is less than endIdx
            # otherwise we put a placeholder like -1 to indicate that is not correct
            childTwoIdx = currentIdx * 2 + 2 if currentIdx *2 + 2 <= endIdx else -1
            
            # Decide what index to swap:
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            
            # swap parent-child
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                
                # re-calculate currentIdx and childOne
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                break
            
            
    def siftUp(self, currentIdx, heap):
        # To sift up, we need to allocate the parent of the current node
        # for a heap in general, this formula is (i-1)/2
        
        parentIdx = (currentIdx - 1) //2 # Use this to floor in python
        
        # while the index is bigger than 0 (remember, we want to go to the root)
        # AND the current value is less than a parent (we want the smaller to be the parent)
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            
            self.swap(currentIdx, parentIdx, heap)
            
            #update the currentIdx and the parent
            currentIdx = parentIdx
            parentIdx = (currentIdx -1)//2
            
            
    def peek(self):
        # return the peek value, the first one 
        return self.heap[0]

    def remove(self):
        #IMPORTANT: This is a min heap, therefore the only value we can pop
        # is the actual root. therefore, we will treat this as a method that
        # only removes the root node (which is the min value)
        
        # First, we swap the root value
        self.swap(0, len(self.heap)-1, self.heap)
        
        # pop the value of the root
        valueToRemove = self.heap.pop()
        
        # then we sift down the value, we pass the startIdx, the endIdx
        self.siftDown(0, len(self.heap) -1, self.heap)
        
        #IMPORTANT: In any remove method, remember to return the valueToRemove
        return valueToRemove
        
    
    def insert(self, value):
        # Whenever we insert an element in the heap, we first insert it at the end:
        self.heap.append(value)
        
        # then, we will shift up the value
        # we need the index where we start (in this case is at the end )
        # and the actual heap that we want to do the shift up
        self.siftUp(len(self.heap)-1, self.heap)
        
    # IMPORTANT: Whenever we need to swap variables, use a helper function
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
        
# ---- UNIT TEST

import unittest


def isMinHeapPropertySatisfied(array):
    for currentIdx in range(1, len(array)):
        parentIdx = (currentIdx - 1) // 2
        if array[parentIdx] > array[currentIdx]:
            return False
    return True


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        minHeap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
        minHeap.insert(76)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), -5)
        self.assertEqual(minHeap.remove(), -5)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), 2)
        self.assertEqual(minHeap.remove(), 2)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), 6)
        minHeap.insert(87)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))

if __name__ == '__main__':
    unittest.main()