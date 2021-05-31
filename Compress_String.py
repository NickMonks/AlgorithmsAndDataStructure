import unittest

def runLengthEncoding(string):
    encondedStringCharacters = []
    # We start with 1, since we need to return a non-empty string
    currentRunLength = 1
    
    for i in range(1, len(string)):
        # We start on the second character. What we do is compare i-1 against i,
        # if they're equal continue to increase run length; otherwise,  
        currentCharacter = string[i]
        previousCharacter = string[i-1]
        
        if currentCharacter != previousCharacter or currentRunLength == 9:
            # we add both conditions here since the output will be to restore
            # the run length and append the characters.
            encondedStringCharacters.append(str(currentRunLength))
            encondedStringCharacters.append(previousCharacter)
            
            # Reset current run length (we put a zero because, not matter what, we will increase the string)
            currentRunLength = 0
        
        currentRunLength += 1
        
    # for the last run, we append the run length
    encondedStringCharacters.append(str(currentRunLength))
    # Important to notice that this wont give a indexbounderror since we know
    # from the prompt that we wont have an empty array (THIS IS IMPORTANT TO MENTION IN THE INTERVIEW)
    encondedStringCharacters.append(string[len(string)-1])
    
    # THIS METHOD IS IMPORTANT TO CONVERT LIST TO STRING!
    return "".join(encondedStringCharacters)