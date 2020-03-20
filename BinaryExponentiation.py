'''
Kyle Timmermans
03/04/2020
Exponentiation without pow() function or '**' operator
Recursive Solve
'''


def exponential(a, n):  # a = base, n = exponent
    if n == 0:
        return 1   # Anything to the 0th power is 1
    elif n == 1:
        return a  # Anything to the 1st power is itself
    else:
        if (n % 2 == 0):  # If exponent is even
            return exponential(a, (n / 2)) * exponential(a, (n / 2)) # e.g. 2^10 = (2^5) * (2^5)
        else:             # If exponent is odd
            return exponential(a, int(n / 2)) * exponential(a, int(n / 2)) * a  # e.g. 2^5 = (2^2) * (2^2) * (2^1) and using int to divide odd number in half


a = int(input("Enter exponent number for 2 to be the base of e.g. 5 for 2^5, 10 for 2^10: "))  # Input exponent
print(exponential(2, a))  # Returns final number

# Essentially the end computation is: a * a * a * a * a * a * a * a * a * a



