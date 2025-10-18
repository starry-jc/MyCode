# Problem: ccc18j1

# Assigning numbers
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

# Using if statement and operators
#  The following line is asking this: if the first digit is 8 or 9, and...
if ((num1 == 8 or num1 == 9) and
        # ...the fourth digit is also 8 or 9, and...
        (num4 == 8 or num4 == 9) and
        # ...digits two and three are equal, execute the following action.
        (num2 == num3)):
    print('ignore')
else:
    print('answer')