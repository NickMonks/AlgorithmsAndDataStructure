# O(2^(n+m)) Time | O(n+m) space - NO CACHING
def interweavingStringsNoCaching(one, two, three):
	
	# here, we do some edge cases:
	if len(three) != len(one) + len(two):
		return False
	
	return areInterwovenNoCaching(one, two, three, 0, 0)

def areInterwovenNoCaching(one, two, three, i, j):
# For this problem, we use three pointers in the three strings: i, j and k. 
# we will recursively check if the char is equal to either one or two. In the case
# whether both are the same, we are going to make two recursive functions again and again
# if the three are not equal then return false, and we go a step back.
#
# This function will check if strings are interwoven. 
# it will take index of one (i) and two (j). the index of three
# is just the sum of one and two (i.e. if we move 2 )
	k = i + j
	
	if k == len(three):
		return True 
	
	# if any index is the same as in the three string, we will make a recursive call
	# adding the i+1 or j+1, depending on the case. 
	if i < len(one) and one[i] == three[k]:
		# if it is interwoven (i.e. we hit the base case) we want to return true
		# recursively. 
		if areInterwovenNoCaching(one, two, three, i+1, j):
			return True
			
	
	if j < len(two) and two[j] == three[k]:
		return areInterwovenNoCaching(one, two, three, i, j+1)
	
	# if neither of the cases are hit, return false
	return False

# O(n*m) Time | O(n*m) space - WITH CACHING
def interweavingStringsCaching(one, two, three):
	
	# here, we do some edge cases:
	if len(three) != len(one) + len(two):
		return False
	# We add the "+1" because it is likely to go out of bounds when we check the strings
	# i.e. aaa_, aaaf 
	#         
	cache = [[None for j in range(len(two)+1)] for i in range(len(one)+1) ]
	return areInterwovenCaching(one, two, three, 0, 0, cache)

def areInterwovenCaching(one, two, three, i, j, cache):
# For this problem, we use three pointers in the three strings: i, j and k. 
# we will recursively check if the char is equal to either one or two. In the case
# whether both are the same, we are going to make two recursive functions again and again
# if the three are not equal then return false, and we go a step back.

# Include cache as a 2D array [i][j], where i is the pointer to array1 and j to array2

	if cache[i][j] is not None:
		return cache[i][j]

# This function will check if strings are interwoven. 
# it will take index of one (i) and two (j). the index of three
# is just the sum of one and two (i.e. if we move 2 )
	k = i + j
	
	if k == len(three):
		return True 
	
	# if any index is the same as in the three string, we will make a recursive call
	# adding the i+1 or j+1, depending on the case. 
	if i < len(one) and one[i] == three[k]:
		# if it is interwoven (i.e. we hit the base case) we want to return true
		# recursively. We should this to be EQUAL TO THE CACHE VALUE
		cache[i][j] = areInterwovenCaching(one, two, three, i+1, j, cache)
		
		if cache[i][j]:
			return True
			
	
	if j < len(two) and two[j] == three[k]:
		cache[i][j] =  areInterwovenCaching(one, two, three, i, j+1, cache)
		return cache[i][j]
	
	# if neither of the cases are hit, return false
	cache[i][j] = False
	return False
