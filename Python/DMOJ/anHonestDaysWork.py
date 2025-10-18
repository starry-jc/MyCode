# Problem: wc18c3j1

# Assigning variable p
#  Total amount of paint
p = int(input())

# Assigning variable b
#  Paint needed for each badge
b = int(input())

# Assigning variable d
#  Money made per badge
d = int(input())

# Math Time!
#  Assigning variables sold and extra_paint
#  sold is the number of badges that can be sold
#  extra_paint is the amount of paint left over
sold = p // b
extra_paint = p % b

# Multiply sold by d, then add extra_paint
print((sold * d) + extra_paint)