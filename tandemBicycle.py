def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # The solution to this problem is basically sort both arrays and create a pair for each element at i;
	# if fastest is true, then we will sort one asc and another desc and take the pair and sum the biggest one.
	# if it's false, we sort both ASC and take the max of each pair and acc them.
	# to have less space complexity, we sort the arrays in place
	
	redShirtSpeeds.sort()
	blueShirtSpeeds.sort()
	
	if fastest:
		reverseArrayInPlace(redShirtSpeeds)
	
	totalSpeed = 0
	
	for idx in range(len(redShirtSpeeds)):
		rider1 = redShirtSpeeds[idx]
		rider2 = blueShirtSpeeds[idx]
		totalSpeed += max(rider1,rider2)
		
	return totalSpeed
	
def reverseArrayInPlace(array):
	# reverse using a build-in function to reverse it
	start = 0
	end = len(array) -1 
	
	# basically use a while loop where we keep looping over start and end. Don't return anything
	# since we change by reference. 
	while start < end:
		array[start], array[end] = array[end], array[start]
		start += 1
		end -= 1