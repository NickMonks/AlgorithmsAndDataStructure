# O(n^2) time | O(n) space
def diskStacking(disks):
	# The algorithm is the following: we will create a list of heights for each disk, and we order the disk stack list.
	# then we will use two pointers, called other (left) and current (right), where other: 0<j<i and current 0<i< length(array)
	# then we will accumulate the maximum height for each disk, if the disk was the base. Because we know that every disk that comes
	# right after the currentDisk is strictly heigher, we can use the value.
	# (!) what happens if a disk have too big w,d and we are looking the maximum? Nothing; we will traverse, find out there is no possible
	# combination and store the max height has the currentDisk height. following iterations will find the maximum 
	# however, how we find the maximum height?, what we do is we get the maximum height of the current Height maximum (i.e. imagine we find that
	# one combination was 10, and the next one is 9; we keep the heigher one). 
	
	
    # First of all, we sort the array by height, since this allow us to create a efficient solution to our 
	# algorithm AND because we. want to optimize this part of the elements.
	
	disks.sort(key=lambda disk: disk[2])
	
	# create a mapping of heights to store the maximum height 
	heights = [disk[2] for disk in disks]
	
	# create another array that links which is the the previous disk that provided the maximum height
	# contains the index; if we find a None, that means is the last disk in our sequence. 
	sequences = [None for disk in disks]
	
	# we keep track of the maximum height
	maxHeightIdx = 0
	
	# we start in index 1 because we check previous ones, to contain the otherDisk
	for i in range(1, len(disks)):
		currentDisk = disks[i]
		for j in range(0,i):
			otherDisk = disks[j]
			if areValidDimensions(otherDisk, currentDisk):
				
				# check if the current max height in the list is less than currentDisk height plus the otherDisk height
				if heights[i] < currentDisk[2] + heights[j]:
					heights[i] = currentDisk[2] + heights[j]
					# update the link : the updated sequence at index i is index j
					sequences[i] = j
		
		# once we got the max for index i, we update the maximum value:
		# be careful: in python you cant compare directly a float with an element of a list 
		if heights[i] >= heights[maxHeightIdx]:
			maxHeightIdx = i
		
	# return sequence elements: we need to pass the max height also obviously
	return buildSequence(disks, sequences, maxHeightIdx)
	
def areValidDimensions(o, c):
	return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]

def buildSequence(array, sequences, currentIdx):

	sequence = []

	while currentIdx is not None:
		sequence.append(array[currentIdx])
		currentIdx = sequences[currentIdx]
		# we will store it in [bottomDisk, secondBottom...], so we need to reverse it
	return list(reversed(sequence))