# Problem: ddrp1

# Defining Variables
n = int(input())    # first row input - car door
m = int(input())    # second row input - tudor selected
p = int(input())    # third row input - jason selected

# Purpose: outputs "Switch" if Tudor's selection
#  is the same as the car door, and "Stay" if not.
# Function: checks to see if Tudor's selection, stored
#  in variable m, is the same as the car door, stored
#  in variable n. If it is, prints "Switch"; if not,
#  print "Stay".
if m == n:
    print("Switch")
else:
    print("Stay")