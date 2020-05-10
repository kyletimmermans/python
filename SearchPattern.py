'''
Kyle Timmermans
05/8/20
Search for specific words in a document
Inspired by question on Algorithms Final
'''


def SearchPattern(input, word):
    found = []
    n = len(input)
    m = len(word)
    for i in range(0, n):
        if input[i] == word[0]:  # Start checking the rest of the input, if the first letter matches the target word
            for j in range(1, m):  # For the length of the target word e.g. "o o d" in "good", m never fully reached
                if input[i+j] == word[j]:  # Keep checking the next letter in the text to see if matches the target word
                    if input[i+j] == word[j] and j == m-1:   # Did it match the whole word?  -1 needed, first letter already checked
                        found.append(i)  # return index of first letter of the word in the given string that matches target word
    if len(found) == 0:
        return -1  # If target not found at all, return -1
    else:
        return found   # Return all indexes of the first letter of the word found in the text


# Driver
test_text = """There is nothing either good or bad, but thinking makes it so. 
               I would like to think, people are inherently good."""
word = "good"
x = SearchPattern(test_text, word)
print(x)
