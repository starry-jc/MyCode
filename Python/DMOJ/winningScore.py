# Problem: ccc19j1

# Assigning Team Apple variables of 3-pointers, 2-pointers, and 1-pointers.
apple_three = int(input())
apple_two = int(input())
apple_one = int(input())

# Assigning Team Banana variables of 3-pointers, 2-pointers, and 1-pointers.
banana_three = int(input())
banana_two = int(input())
banana_one = int(input())

# Calculate the number of points scored by each team
#  Optional: Use parantheses to easily divide the calculations
apple_total = (apple_three * 3) + (apple_two * 2) + apple_one
banana_total = (banana_three * 3) + (banana_two * 2) + banana_one

# Producing the output
#  Using if statements to determine the winning team
if apple_total > banana_total:
    print('A')
elif banana_total > apple_total:
    print('B')
else:
    print('T')