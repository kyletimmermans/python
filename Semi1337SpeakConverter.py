'''
Take a password cracking wordlist and get all words that have an 'a', 'e' or both in them and
all of these words to a new list called temp.lst.

Then take each of those words from temp.lst and generate all of their possible permutations
where 'e'/'E' = 3 and 'a'/'A' = 4. Then all of these extra words will be added to a new wordlist
called "final_wordlist.lst"

E.g.

The word, "searches" would yield: searches, s3arches, se4rches, search3s, s34rches, s3arch3s, se4rch3s, s34rch3s
'''

from itertools import product
import re

# Only get words with that have an 'a', 'e', or both characters in them
with open('original_list.lst') as oldfile, open('temp.lst', 'w') as newfile:
	for line in oldfile:
		if re.search('[ae]', line, re.IGNORECASE):
			newfile.write(line)
            
with open('temp.lst') as oldfile, open('final_wordlist.lst', 'w') as newfile:
	for line in oldfile:
		word_list = list(line)
		wordvowels = []
		mychars = []

		# Take word, get vowel list
		for i in enumerate(word_list):
			if i[1] == 'e':
				wordvowels.append(i)
				mychars.append('e')
				mychars.append('3')
			if i[1] == 'E':
				wordvowels.append(i)
				mychars.append('E')
				mychars.append('3')
			if i[1] == 'a':
				wordvowels.append(i)
				mychars.append('a')
				mychars.append('4')
			if i[1] == 'A':
				wordvowels.append(i)
				mychars.append('A')
				mychars.append('4')
			

		# Get all vowel and number combinations for replacement		
		keywords = [''.join(i) for i in product(mychars, repeat = len(wordvowels))]  # Help with itertools lib: https://stackoverflow.com/a/7074066

		temp_list = []

		# Get the combinations from itertools product() that match our vowellist for current word (E.g. "speak": eae = 343, eae = e4e, eae = 3ae, etc)
		for i in keywords:
			check = 0
			for j in enumerate(wordvowels):
				if j[1][1] == 'e' or j[1][1] == 'E':  # If current letter of wordvowels is e
					if i[j[0]] != 'e' and i[j[0]] != '3' and i[j[0]] != 'E':  # If current letter of keywords is e
						break  # Even if one is off, we stop and go to next
					else:
						check = check + 1
				elif j[1][1] == 'a' or j[1][1] == 'A':
					if i[j[0]] != 'a' and i[j[0]] != '4' and i[j[0]] != 'A':
						break
					else:
						check = check + 1
			if check == len(wordvowels):  # If we got every letter right, add it
				temp_list.append(i)

		final_list = list(set(temp_list)) # Remove duplicates with set logic

		# Take every combination of 3's 4's a's and e's and put them back into the word
		for i in final_list:
			word_list_copy = word_list
			for j in enumerate(wordvowels):
				word_list_copy[j[1][0]] = i[j[0]]
			newfile.write(''.join(word_list_copy))
