import unittest

# ------------- OPTION 1 ----------------------------
# O(n) time | O(n) space
def reverseWordsInString(string):
	# Solution 1. Find all words in the string, and also register the white spaces (image we have
	# many white spaces; we need to keep track of them)
	
	words = []
	startOfWord = 0
	for idx in range(len(string)):
		character = string[idx]
		
		if character == " ":
			words.append(string[startOfWord:idx]) # this wont include the IDX variable
			startOfWord = idx # we change the start of word to be here
			
		# once we have a white space, we keep checking if for that index we have a white space
		elif string[startOfWord] == " ":
			words.append(" ")
			startOfWord = idx
	
	# we need to add any possible white spaces at the end:
	words.append(string[startOfWord:])
	
	reverseList(words)
	
	return "".join(words) # join will create a string out of a list

def reverseList(list):
	# to reverse, we need to swap the first element with last element, 
	# and move the first and last pointer until they collide or last > first
	
	start, end = 0, len(list)-1
	while start < end:
		list[start], list[end] = list[end], list[start]
		start +=1
		end -=1

# ------------- OPTION 2 ----------------------------
# O(n) time | O(n) space
def reverseWordsInString(string):
    # OPTION 2: Reverse the whole string as a list of chars (with a helper function), and then reverse each word with the same helper function. To do that, the helper function will need
    # to now the start and end indexes and keep ignoring white spaces
    
    # create a list from the string
    characters = [char for char in string]
    
    # reverse the entire list of chars:
    reverseListRange(characters, 0, len(characters)-1)
    
    startOfWord = 0
    while True:
        # we start with end being equal to start until find the end of the word
        endOfWord = startOfWord
        while endOfWord < len(characters) and characters[endOfWord] != " ":
            endOfWord += 1
        
        # when the end of the word has been found, and it is the len of characters,
        # then we reverse the whole characters list
        if endOfWord == len(characters):
            reverseListRange(characters, startOfWord, len(characters)-1)
            break
        
        # if while loop breaks that means we have found a space " ", so we reverse the word
        # and at the start of the while loop we will define again endOfWord as startOfWord
        # we reverse the word we're currently at in the bounds of [start, end]
        # we substract one since we're adding the endOfWord the space character, and we don't want to reverse that
        # (the condition is that characters[endOfWord] = " " to break, but we want endOfWord -1)
        reverseListRange(characters, startOfWord, endOfWord -1)
        
        # we add one since we know we have a white space; even if the next character is a space the algorithm
        # will keep adding until there is a character
        startOfWord = endOfWord + 1
	
	return "".join(characters)
	
def reverseListRange(list, start, end):
	while start < end:
		list[start], list[end] = list[end], list[start]
		start +=1
		end -=1

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = "AlgoExpert is the best!"
        expected = "best! the is AlgoExpert"
        actual = reverseWordsInString(input)
        self.assertEqual(actual, expected)