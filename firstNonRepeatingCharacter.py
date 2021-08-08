def firstNonRepeatingCharacter(string):
    characterFrequencies = {}
    
    for character in string:
        # IMPORTANT: get will get the value if character exists, if not it will return 0!!
        characterFrequencies[character] = characterFrequencies.get(character, 0) + 1
    
    for idx in range(len(string)):
        character = string[idx]
        if characterFrequencies[character] == 1:
            return idx
    
    return -1