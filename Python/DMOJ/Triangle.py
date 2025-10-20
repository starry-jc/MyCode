# Problem: p183ex6

# importing modules
from math import factorial

# defining variables
n = int(input())

# combination formula
for i in range(n):
    # i = N

    for j in range(i + 1):
        # j = R
        # nCr = n!/(r!*(n-r)!)
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")

    # Print new line
    print()