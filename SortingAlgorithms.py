'''
Kyle Timmermans
03/07/2020
compiled in python 3.8.2
'''

import random  # Using random to create random number list in specific range
import time  # Using time to measure run-time of algorithms


#####################################
# Sorting Algorithm Implementations #
#####################################

# Bubble Sort
def bubbleSort(arr):
    x = len(arr)
    for i in range(x):
        for j in range(0, x-i-1): #x-i-1: don't recheck sorted parts, also -1 because start from zero
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] #swap


# Selection Sort
def selectionSort(arr):
    x = len(arr)
    for i in range(x):
        smallest = i #first element initialized as smallest
        for j in range(i+1, x):
            if arr[smallest] > arr[j]:
                smallest = j #smallest is now j
        arr[i], arr[smallest] = arr[smallest], arr[i] #swap


# Insertion Sort
def insertionSort(arr):
    x = len(arr)
    for i in range(1, x):
        key = arr[i] #key is where they begin to sort and push back at
        j = i - 1
        while j >= 0 and key < arr[j]: #continue pushing element behind key
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key #change key position


# Recursive Merge Sort
def mergeSort(arr):
    if len(arr) > 1:  # Base case
        middle = len(arr) // 2  # Split middle in half, double slash makes half an int (no division remainder)
        left = arr[:middle]  # Left = Everything left of middle pivot
        right = arr[middle:]  # Right = Everything right of middle pivot

        mergeSort(left)  # Sort left half recursively
        mergeSort(right) # Sort right half recursively

        i = j = z = 0  # i = left iterator, j = right iterator, z = whole list iterator

        # Place the smaller values into the merged array, starting from arr[z=0]
        while i < len(left) and j < len(right):
            if left[i] < right[j]: # Check if left is smaller
                arr[z] = left[i] # Place left value into merged array
                i += 1  # Up one spot in left
            else:  # Check if right is smaller
                arr[z] = right[j]  # Place right value into merged array
                j += 1  # Up one spot in right

            z += 1 # Move to next space of merged array

        # Clean up remaining value in left array
        while i < len(left):
            arr[z] = left[i]
            i += 1 # Up one spot in left array
            z += 1 # Next spot in merged array

        # Clean up remaining values in right array
        while j < len(right):
            arr[z] = right[j]
            j += 1 # Up one spot in right array
            z += 1 # Next spot in merged array


# Quick Sort with random partition
def quickSort(arr):
    def sort(list, left, right): # Define sort within quickSort
        if right <= left:  # Base Case
            return

        pivot = random.randint(left, right)  # Choose random pivot point between or at left / right

        list[left], list[pivot] = list[pivot], list[left]  # Place pivot in first index

        # Partition() completed here
        i = left  # Index of smaller element
        for j in range(left+1, right+1):
            if list[j] < list[left]: # If current element is smaller than pivot
                i += 1  # Increment index of smaller element
                list[i], list[j] = list[j], list[i] # Swap

        list[i], list[left] = list[left], list[i]  # Move pivot into correct position with swap

        sort(list, left, i-1)  # Sort left partition
        sort(list, i+1, right)  # Sort tight partition

    if len(arr) < 2 or arr is None:  # If array is empty or less than 2 elements
        return

    sort(arr, 0, len(arr) - 1)  # Sort array from left = beginning to right = end


# Radix Sort, uses Counting Sort to sort each digits place
def radixSort(arr):

    # Counting Sort (Non-comparison based, stable sorting algorithm)
    def countingSort(arr, place):
        n = len(arr)

        output = [0] * (n)  # Output array that stores sorted array
        count = [0] * (10)  # Initialize count to 0, used to store count of value

        for i in range(0, n):  # Place number of occurrences in count[]
            index = (arr[i] / place)
            count[int(index % 10)] += 1  # Needs int() otherwise index of float value

        for i in range(1, 10):  # Update count[i] so count[i] contains correct index of digit in output
            count[i] += count[i - 1]

        i = n - 1   # Start building output array, starting at end of array
        while i >= 0:  # Place elements in correct positions
            index = (arr[i] / place)
            output[count[int(index % 10)] - 1] = arr[i]  # Needs int() otherwise index of float value
            count[int(index % 10)] -= 1  # Needs int() otherwise index of float value
            i -= 1  # Decrease by one and keep moving down until 0

        for i in range(0, len(arr)):  # Copy output to 'arr' for Radix Sort
            arr[i] = output[i]

    # Radix Sort begins here, compare one's, ten's, and hundred's place using countingSort
    maximum = max(arr)
    place = 1  # Initialize at one's place
    while maximum/place > 0:  # While the greatest value at least has a one's place
        countingSort(arr, place)
        place *= 10  # Used to increase place value each time (Opposite is 10 % 1)


####################
# Helper Functions #
####################

# Function for testing if functions work for small sets
def test(name, func_name):   # Need name of function and function
    arr = [random.randrange(1, 100, 1) for i in range(10)]  # Different value for 'a' every time function called
    func_name(arr)
    print("Testing " + name + " with an array of size 10: ", end='')  # Include results on this line with 'end'
    print("Correct!" if arr == sorted(arr) else "Error!")   # One liner with Ternary Operation

# Time Sorting Algorithms and round float value
def timer(func, arr):
    start = time.time()
    func(arr)
    end = time.time()
    final = float(end - start)
    return '%.7f' % round(final, 7)  # Precision float rounding

# Function for printing all results on one line
def printOutput(size):
        arr = [random.randrange(1, 100, 1) for i in range(size)]  # Can be used for each function because it is declared in function locally, so not sorted each time
        times = [timer(bubbleSort,arr), timer(selectionSort,arr), timer(insertionSort,arr), timer(mergeSort,arr), timer(quickSort,arr), timer(radixSort,arr)] # Array of times
        if size <= 99:
            print(str(size) + ' '* 7, end='')  # Change spacing between size and measurements, depending on number of chars used for size
            for i in times:
                print(str(i) + 's' + "       ", end='') # Include 's' and space after each measurement
            print(' ')
        elif size <= 999:
            print(str(size) + ' ' * 6, end='')
            for i in times:
                print(str(i) + 's' + "       ", end='')
            print(' ')
        else:
            print(str(size) + ' ' * 5, end='')
            for i in times:
                print(str(i) + 's' + "       ", end='')
            print(' ')


##########
# Output #
##########

print(' ') #Create space
print('1. Testing the three Algorithms: ') #Output start

# Driver for test function
# Ensure each function is working
test("Bubble Sort", bubbleSort)
test("Selection Sort", selectionSort)
test("Insertion Sort", insertionSort)
test("Merge Sort (Recursive)", mergeSort)
test("Quick Sort (Recursive)", quickSort)
test("Radix Sort (Counting Sort)", radixSort)

print(' ')

print('2. Measuring the Sorting Algorithms with randomly generated input sets consisting of values 1-100 for varying array sizes:')
print('3. Summary of measurement results:')
print(' ')
print('Input-size                                     Running-Time')
print('----------------------------------------------------------------------------------------------------------')
print('           Bubble         Selection        Insertion          Merge            Quick            Radix')
printOutput(20)
printOutput(40)
printOutput(50)
printOutput(100)
printOutput(200)
printOutput(500)
printOutput(1000)
print(' ')
