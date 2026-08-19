# Problem: hkccc15j2

# defining variavbles

# n - number of points
n = int(input())
# x_list - empty list that will contain x values
x_list = []
# y_list - empty list that will contain y values
y_list = []
# s_max - The maximum square area value
s_max = 20000**2
# s_ij - Represents each square made from two coordinates
#  and their side lengths, i and j. This variable stores the area.
s_ij = 0



# Iterates through the value n:
#  Splits each incoming coordinate value input
#  into x and y variables.
#  Appends the x values into x_list, and the y
#  values into y_list
#  Iterates through the range of i+1 up to n:
#    Sets s_ij to the maximum value between the absolute value of x_list
#    at element i minus x_list at element j and the absolute
#    value of y_list at element i minus y_list at element j. Squares this
#    value.
#    Checks to see if s_ij is less than s_max.
#      If this is true, set s_max to s_ij.
for i in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
    
    for j in range(i+1, n):
        s_ij = max(abs(x_list[i] - x_list[j]), abs(y_list[i] - y_list[j])) ** 2

        if s_ij < s_max:
            s_max = s_ij

# Output s_max as the answer
print(s_max)