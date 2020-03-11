'''
Kyle Timmermans
03/11/2020
Compiled in python 3.8.2
'''

def stocksCalculation(arr):
    max = 0
    for i in range(int(len(arr)-1), 0, -1):  # len(arr)-1 to -1 gives list to second to beginning of list
      for j in range(i, -1, -1):  # Go to end of list from i
          if (current := arr[i] - arr[j]) > max:
              max = current
              buy, sell = j+1, i+1  # Needs plus one for proper days
    print(' ')
    print("Within these "+str(len(arr))+" days, buying this stock on day "+str(buy)+" and selling on day "+str(sell)+" yields the highest return of "+str(max))


def stocksInput():
    arr = []  # Store stock values per day
    print("\nKeep entering a stock's value for each day it is live, once you're done, type q or Q\n")
    day = 1
    while True:
        x = input("Day "+str(day)+"'s Value: ")
        if x == 'q' or x == 'Q':
            return arr
        else:
            arr.append(int(x))
            day += 1
    return arr


# Driver
stocksCalculation(stocksInput())