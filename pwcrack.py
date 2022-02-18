#!/usr/bin/env python3

# Kyle Timmermans - AppSec 2021

from binascii import hexlify
from hashlib import sha256
import sys
import time  # Needed to get guesses/sec

# Hash guesses
def hasher(asalt, password):
	asalt = str(salt)
	hasher = sha256()
	hasher.update(asalt.encode('utf-8'))
	hasher.update(password.encode('utf-8'))
	return hasher.hexdigest()
	
if __name__ == '__main__':
	# Usage
	if (len(sys.argv) == 1 or "-h" in sys.argv):
		  print("\nUsage: ./pycrack.py 'YOUR_HASH_HERE'")
		  sys.exit()
		  
	salt, target_hash = sys.argv[1].split('$')
	
	guess_num = 0
	
	start_time = time.time()
	
	# Hash each word in wordlist and compare to target hash
	with open('rockyou.txt', encoding="latin-1") as file:
		for line in file:
			guess_num = guess_num + 1
			if str(hasher(salt, line.strip())) == str(target_hash):  # If a match, stop
				print("\nPASSWORD --> " + str(line.strip()))
				break
	
	end_time = time.time()
	
	print("\nGuess Speed: " + str(guess_num / (end_time - start_time)) + " guesses/sec")
