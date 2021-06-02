# O(n^2) time | O (n) space
def longestPalindromicSubstring(string):
	# For this algorithm, we will check every time if we are in the middle of a palindrome
	# and storing the length of that palindrome in a list. 
	
	# First, we initialize this list:
	currentLongest = [0,1]
	
	
	# we start from second position, at 1
	for i in range(1, len(string)):
		# check if we have an odd or even palindrome (another option)
		# IMPORTANT: WE CHECK BOTH OF THEM AT THE SAME TIME!
		
		
		odd = getLongestPalindromeFrom(string, i-1, i+1)
		# if even, we want to check if the neighbour (i-1) is the same as i
		even = getLongestPalindromeFrom(string, i-1, i)
		
		# finally, we use max builtin function to get the longest array
		# since we return a list of [min, max] format, we apply a lambda will does x[1]- x[0]
		# to return an integer. 
		
		longest = max(odd, even, key = lambda x: x[1]-x[0])
		
		# same logic as above but with general longest palindrome
		currentLongest = max(longest, currentLongest, key = lambda x: x[1]-x[0])
	
	# we can easily slice our array like this: string[0:1]
	return string[currentLongest[0]:currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
	# Check if its a palindrome or not
	
	# while the index are bounded to string length...
	while leftIdx >= 0 and rightIdx < len(string):
		if string[leftIdx] != string[rightIdx]:
			break
		leftIdx -= 1
		rightIdx += 1
	
	# we add the "+1" because at the last iteration substract one to left
	# the same could happen with right but because we slice to currentLongest[1]
	# (were in Python DOESNT INCLUDE the index) this is fine. 
	return [leftIdx +1, rightIdx]