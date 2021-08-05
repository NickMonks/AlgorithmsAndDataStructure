# O(N log N) | O(1)
def heapSort(array):
    # as the name suggest, heap sort will basically create a heap sort using the sift down method (whitch is a log N operation)
	# and then continuosly swaping the first element (which will be a max heap) to the last element. Then, we reduce the list every iteration
	# and finally have a sorted list!
	
	#First, we want to build a max heap:
	buildMaxHeap(array)
	
	# then we swap the last index of the heap with the root value 
	for endIdx in reversed(range(1,len(array))): 
		# we want to go to len(array) -1, but because the function is exclusive we simply say len(array) and wont take last element
		swap(0,endIdx, array)
		
		#then, we want to sift down the new value, so we have the biggest element at idx 0 until endIdx -1
		# (and we dont need to rebuild a max heap; we simply need to fix it by sifting down the unsorted element)
		# because heaps are balanced trees, it will work.
		siftDown(0, endIdx -1, array)
	
	return array

def swap(i,j,array):
	array[i], array[j] = array[j], array[i]

def buildMaxHeap(array):
	# first, find the first parent node
	firstParentIdx = (len(array) -1) //2
	
	# then continuosly sift down the elements:
	for currentIdx in reversed(range(firstParentIdx+1)): # because is exlusive, we need to add the +1
		siftDown(currentIdx, len(array)-1, array)
	
def siftDown(currentIdx, endIdx, heap):
	# grab the two children nodes, compare and take the one that should be potentially swaped
	# we need to keep track that we are on the limits of the last index element. 
	childOneIdx = currentIdx * 2 + 1
	# first we verify that one is in the limits, and then check that two is also in the limits
	# if so we declare the biggest the idxToSwap and compare the heap value. 
	while childOneIdx <= endIdx:
		childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
		if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
			idxToSwap = childTwoIdx
		else:
			idxToSwap = childOneIdx
		
		if heap[idxToSwap] > heap[currentIdx]:
			# if its bigger, we swap them AND update the currentIdx
			swap(currentIdx, idxToSwap, heap)
			currentIdx = idxToSwap
			# re-calculate the childOneIdx:
			childOneIdx = currentIdx * 2 + 1
		else:
			return # the node is in the correct position