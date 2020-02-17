'''
Kyle Timmermans
1/20/2020
compiled on python 3.7.3
'''

import random
import time

#Using random to create random number list in specific range
#Using time to measure run time of algorithms

#Sorting Algorithm Implementations
#Timer Included
def bubbleSort(arr):
    bSortNormStart = time.time()
    x = len(arr)
    for i in range(x):
        for j in range(0, x-i-1): #x-i-1: dont recheck sorted parts, also -1 because start from zero
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] #swap
    bSortNormEnd = time.time()
    return float(bSortNormEnd - bSortNormStart) #convert scientific notation to float

def selectionSort(arr):
    sSortNormStart = time.time()
    x = len(arr)
    for i in range(x):
        smallest = i #first element initialized as smallest
        for j in range(i+1, x):
            if arr[smallest] > arr[j]:
                smallest = j #smallest is now j
        arr[i], arr[smallest] = arr[smallest], arr[i] #swap
    sSortNormEnd = time.time()
    return float(sSortNormEnd - sSortNormStart)

def insertionSort(arr):
    iSortNormStart = time.time()
    x = len(arr)
    for i in range(1, x):
        key = arr[i] #key is where they begin to sort and push back at
        j = i - 1
        while j >= 0 and key < arr[j]: #continue pushing element behind key
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key #change key position
    iSortNormEnd = time.time()
    return float(iSortNormEnd - iSortNormStart)

print(' ') #Create space
print('1. Testing the three Algorithms: ') #Output start

#BubbleSort
a = [random.randrange(1, 10000, 1) for i in range(10)]
a_sorted = sorted(a)
bubbleSort(a)
if a == a_sorted:
    print('Testing Bubble Sort with an array of size 10: ' + 'Correct!')
else:
    print('Testing Bubble Sort with an array of size 10: ' + 'Error!')

#SelectionSort
b = [random.randrange(1, 10000, 1) for i in range(10)]
b_sorted = sorted(b)
selectionSort(b)
if b == b_sorted:
    print('Testing Selection Sort with an array of size 10: ' + 'Correct!')
else:
    print('Testing Selection Sort with an array of size 10: ' + 'Error!')

#InsertionSort
c = [random.randrange(1, 10000, 1) for i in range(10)]
c_sorted = sorted(c)
insertionSort(c)
if c == c_sorted:
    print('Testing Insertion Sort with an array of size 10: ' + 'Correct!')
else:
    print('Testing Insertion Sort with an array of size 10: ' + 'Error!')

print(' ') #Create space

#Size 100 Array Test and Run Times
x = [random.randrange(1, 10000, 1) for i in range(100)]
y = [random.randrange(1, 10000, 1) for i in range(100)]
z = [random.randrange(1, 10000, 1) for i in range(100)]

#Do function 30 times, divide total sum times by 30
def repeat(func):
    total_sum = 0.0
    for i in range(30):
        y = float(func)
        total_sum = total_sum + y
        final = total_sum/30
        return '%.7f' % round(final, 7) #Precision float rounding

print('2. Measuring the three sorting algorithms with 30 randomly generated input sets consisiting of values 1-10,000')
print('3. Summary of measurement result:')
print(' ')
print('Input-size              Average Running Time')
print('-----------------------------------------------------')
print('               Bubble        Selection      Insertion')
print('100          '  +  str(repeat(bubbleSort(x)))+'s'+ '      ' +  str(repeat(selectionSort(y)))+'s'+ '     ' + str(repeat(insertionSort(z)))+'s')
print(' ')
