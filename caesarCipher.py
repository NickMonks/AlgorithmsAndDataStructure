def caesarCipherEncryptor(string, key):
    # To solve this problem, we need first to break the string into a list of chars, and then apply a function
	# basically transform each letter the key shifted, and then join them together. Obviously creating the list will take O(n) time and space
	# the function can be implemented in two ways:
	# 1. using Unicode and buildin functions. Specifically, using or to get the unicode value and chr to transform to char.
	# knowing that a = 97 and z = 122, we can convert the value. We need to understand the edge cases:
	#	newlleter = letter + key:
	#	
	#	- If unicode > 122, we need to use the modulo : newletter = (shiftedletter % 122 + 96), we use 96, since
	# 	if char = 'a' -> 123 % 122 = 1 + 96
	#   - If key > 26, we need to be careful since we are not containing this in the prior logic: we need to use the modulo
	#	ALSO in the key = key % 26
	
	newLetters = []
	newKey = key % 26
	for letter in string:
		# instead of creating a new list, we can do this in place directly, populating the new list
		newLetters.append(getNewLetter(letter, newKey))
	
	return "".join(newLetters)

def getNewLetter(letter, key):
	newLetterCode = ord(letter) + key
	return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)