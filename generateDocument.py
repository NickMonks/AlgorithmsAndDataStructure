import unittest

# O(m * (n+m)) time | O(1) space
def generateDocument(characters, document):
    # This first solution (non-optimal) will count each instance of each character
	# and check against the other document:
	for character in document:
		documentFrequency = countCharacterFrequency(character, document)
		charactersFrequency = countCharacterFrequency(character, characters)
		
		if documentFrequency > charactersFrequency:
			return False
	
	return True

def countCharacterFrequency(character, target):
	frequency = 0
	
	for char in target:
		if char == character:
			frequency += 1
	
	return frequency


# O(n+m) time | O(n) space
def generateDocument(characters, document):
    characterCounts = {}
    
    for character in characters:
        if character not in characterCounts:
            # If it doesnt exist, we initialize to 0...
            characterCounts[character] = 0
        
        # ... and here we will add it +1 in any case
        characterCounts[character] +=1
    
    for character in document:
        if character not in characterCounts or characterCounts[character] == 0:
            return False
        
        characterCounts[character] -= 1
    
    return True

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        characters = "Bste!hetsi ogEAxpelrt x "
        document = "AlgoExpert is the Best!"
        expected = True
        actual = generateDocument(characters, document)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()