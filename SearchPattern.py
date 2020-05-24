'''
Kyle Timmermans
05/8/20
Search for specific words in a document
Inspired by question on Algorithms Final

Note: range() does not hit final element, e.g. for j in range(1, m), will never hit m, always m-1
'''


def SearchPattern(input, word):
    found = []
    n = len(input)
    m = len(word)
    for i in range(0, n):
        if input[i] == word[0]:  # Check if the letters of both words are the same, if true, continue checking the word
            for j in range(1, m):  # For the length of the target word e.g. "o o d" in "good", #(m never fully reached, always m-1)#
                if input[i+j] != word[j]:  # if at least one letter doesn't match, go to next word
                    break
                elif input[i+j] == word[j] and j == m-1:  # 'j == m-1'  check if the final letter of both words match
                    found.append(i)   # return index of first letter of the word in the given string that matches target word
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
