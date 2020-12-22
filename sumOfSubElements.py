'''
Given an array A = [10,20,30,40,50,60,70,80,90,100]
Write a function that receives two integers as parameters.
The function returns the sum of elements in the array found between those two integers.
For example, if we use 20 and 50 as parameters, the function should return 140.
'''

def sumOfSubElements(a, b, array):
    for i in range(len(array)):  # Find index of a and b
        if array[i] == a:  # If values are the same
            a = i
        if array[i] == b:
            b = i
    answer = 0
    for x in array[a:b+1]:  # Start adding from a which is now the first element,
            answer += x     # Up until b+1, the new last element
    return answer


# Driver
myArray = [10,20,30,40,50,60,70,80,90,100]

print(sumOfSubElements(20, 50, myArray))
