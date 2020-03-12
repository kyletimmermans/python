'''
Kyle Timmermans
03/11/20
Compiled in python 3.8.2

Used to calculate rod cutting problem, even when the rod is longer or shorter than the size of the price array
'''

import sys

# Define price / length array
def inputArray():
        arr = []
        print("\nKeep placing in prices for each rod length, once you're done, type q or Q\n")
        length = 1
        while True:
            x = input("Length("+str(length)+") - Value: ")
            if x == 'q' or x == 'Q':
                return arr
            else:
                arr.append(int(x))
                length += 1

# Append 0's if size of final rod is larger than the price array size
def fixArray(arr):
    x = size - int(len(arr))
    for i in range(x):
        arr.append(0)
    return arr

# Recursively find Max Profit if size >= len(arr)
def MaxProfSmallerSize(price, k):
    if k <= 0:
        return 0
    maxVal = -sys.maxsize - 1  # Smallest possible system number
    for i in range(0, k):  # Recursively cut rod in different places and compare results
        if maxVal > (price[i] + MaxProfSmallerSize(price, k - i - 1)):
            maxVal = maxVal
        else:
            maxVal = price[i] + MaxProfSmallerSize(price, k - i - 1)
    return maxVal

# Recursively find Max Profit if larger than size of price array
def MaxProfOverSize(price, k):
    if k <= 0:
        return 0
    maxVal = -sys.maxsize - 1
    for i in range(1, k):  # Recursively cut rod in different places and compare results
        cost = price[i] + MaxProfOverSize(price, k - i - 1)
        if cost > maxVal:
            maxVal = cost
    return maxVal

# Driver code
arr = inputArray()
size = int(input("\nInput length of final rod to be cut: "))

if size > len(arr):
    print("Max Profit: "+str(MaxProfOverSize(fixArray(arr), size)))
else:
    print("Max Profit: "+str(MaxProfSmallerSize(arr, size)))
