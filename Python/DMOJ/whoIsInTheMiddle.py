# Problem: ccc07j1

# Assigning variables bowl_1, bowl_2, and bowl_3
bowl_1 = int(input())
bowl_2 = int(input())
bowl_3 = int(input())

# Using if statements
if bowl_1 < max(bowl_2, bowl_3) and bowl_1 > min(bowl_2, bowl_3):
    print(bowl_1)
elif bowl_2 < max(bowl_1, bowl_3) and bowl_2 > min(bowl_1, bowl_3):
    print(bowl_2)
else:
    print(bowl_3)