'''
Kyle Timmermans
2/12/20
compiled in python 3.7.3

Self-reminder: Inner-most loop executes all the way through first
'''

import time
import sys

# Add up To K Functions:
# Default parameters(timer=1), return time
# If timer = 0, return elements
# If timer = 2, simply increment amount of sets found, and dont return anything

def PairsAddupToK(arr, k, timer=1): #Selection Sort used (Optimised, doesn't check searched subsets)
    amountOfPairs = 0 #Increment in case timer=2 and we don't want to print anything
    start = time.time() #Start timer
    pairs = [] #Store explicit values
    n = len(arr)
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] == k):
                x = '('+str(arr[i])+','+str(arr[j])+')'
                pairs.append(x)
    end = time.time() #End timer
    if (timer==1):
        return '%.7f' % round((end - start), 7) #Print time
    elif timer==0:
        for elements in range(len(pairs)): #Print elements
            print(pairs[elements])
    else:
        amountOfPairs += 1

def TriplesAddupToK(arr, k, timer=1): #Uses 3 for-loops for triples, each outer-loop must go to a smaller number than its inner loop
    amountOfTriples = 0 #Increment in case timer=2 and we don't want to print anything
    start = time.time() #Start time
    triples = [] #Store explicit values
    n = len(arr) #Array length
    for i in range(0, n-2):
        for j in range(i, n-1):
            for z in range(j+1, n):
                if (arr[i] + arr[j] + arr[z] == k):
                    x = '('+str(arr[i])+','+str(arr[j])+','+str(arr[z])+')'
                    triples.append(x)
    end = time.time()
    if (timer==1):
        return '%.7f' % round((end - start), 7) #Print time
    elif timer == 0:
        for elements in range(len(triples)):
            print(triples[elements])
    else:
        amountOfTriples += 1

def PrintSubsetsAddupToK(arr, k): #Requires the use of PairsAddupToK and TripletsAddupToK, just prints elements
    PairsAddupToK(arr, k, timer=0)
    TriplesAddupToK(arr, k, timer=0)
    for i in range(0, len(arr)):
        for j in range(i+3, len(arr)):
                sum = 0
                for z in range(i, j):
                    sum = sum + arr[z]
                if (sum == k):
                    print('(', end='')
                    for z in range(i, j):
                        if (z < j-1): #No more trailing commas
                            print(str(arr[z]) + ',', end='')
                        else:
                            print(str(arr[z])+')', end='')
                            sys.stdout.flush()


def TimeSubsetsAddupToK(arr, k): #Only times and stores info
    start = time.time()
    subsets = []
    PairsAddupToK(arr, k, timer=2) #Print nothing
    TriplesAddupToK(arr, k, timer=2)
    for i in range(0, len(arr)):  #For subsets larger than triplets and pairs
        for j in range(i+3, len(arr)):
                sum = 0
                for z in range(i, j):
                    sum = sum + arr[z] #Continually add
                if (sum == k): #if k check
                    for z in range(i, j):
                        subsets.append(arr[z])
    end = time.time()
    return '%.7f' % round((end - start), 7) #Print time




# Reusable print function to clean up code (timer set to 1)
def printOutput(size, arr):
    if (size > 9): #Extra space formatting
        print(str(size)+'          '+str(PairsAddupToK(arr,100))+'s'+'       '+str(TriplesAddupToK(arr,100))+'s'+'       '+str(TimeSubsetsAddupToK(arr,100))+'s')
    else:
        print(str(size)+'           '+str(PairsAddupToK(arr,100))+'s'+'       '+str(TriplesAddupToK(arr,100))+'s'+'       '+str(TimeSubsetsAddupToK(arr,100))+'s')

# Lists
test_set = [50, 90, 20, 30, 70, 8, 5, 84, 2, 1, 80, 100]
a5 = [50, 90, 20, 30, 10]
a10 = [50, 33, 90, 2, 20, 72, 30,10, 92, 8]
a20 = [50, 33, 11, 79, 90, 2, 20, 72, 30, 10, 92, 8, 99, 101, 25, 71, 48, 72, 35, 9]
a30 = [50, 33, 11, 79, 90, 2, 20, 72, 30, 10, 92, 8, 99, 101, 25, 71, 48, 72, 35, 9, 37, 41, 55, 73, 67, 66, 22, 11, 6, 4]

#Output
print(' ') # Formatting
print('1. Testing the three algorithms with input {50, 90, 20, 30, 70, 8, 5, 84, 2, 1, 80, 100}')
print('Testing pairs add up to 100: ')
PairsAddupToK(test_set, 100, 0) #Using timer=0 to print results, remove print() b/c already built in
print('Testing triples add up to 100: ')
TriplesAddupToK(test_set, 100, 0)
print('Testing subsets add up to 100: ')
PrintSubsetsAddupToK(test_set, 100)
print(' ') # Formatting
print(' ')
print('2. Measuring the three sorting algorithms with test sets of varying sizes')
print(' ') # Formatting
print('3. Summary of measurement result:')
print(' ')
print('Input-size                 Running Time')
print('--------------------------------------------------------')
print('               Pairs          Triples         Any-Subets')
printOutput(5, a5) #Needs an extra space for formatting
printOutput(10, a10)
printOutput(20, a20)
printOutput(30, a30)
print(' ') # Formatting
