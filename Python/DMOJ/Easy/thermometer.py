# Problem: qcc0p

# Defining variables

# n - number of family members
n = int(input())
# t_list - empty list that will contain the temperature numbers
t_list = []

# iterates through 0 to n:
#  appends the float input based on the number of inputs
#  into t_list
for i in range(n):
    t_list.append(float(input()))

# iterates through the length of t_list:
#  checks to see if the element at index j
#  of t_list is less than 34.
#    if it is, print the necessary statement.
#  otherwise, checks to see if the element at index j
#  of t_list is less than or equal to 35.5.
#    if it is, print the necessary statement.
#  otherwise, checks to see if the element at index j
#  of t_list is less than or equal to 38.
#    if it is, print the necessary statement.
#  otherwise, checks to see if the element at index j
#  of t_list is less than or equal to 39.
#    if it is, print the necessary statement.
#  otherwise, checks to see if the element at index j
#  of t_list is less than or equal to 41.
#    if it is, print the necessary statement.
#  otherwise, checks to see if the element at index j
#  of t_list is less than or equal to 46.1.
#    if it is, print the necessary statement.
#  otherwise, checks to see if the element at index j
#  of t_list is less than or equal to 50.
#    if it is, print the necessary statement.
#  if none of the above apply (the temperature is greater
#  than 50),
#    then print the necessary statement.
for j in range(len(t_list)):
    if t_list[j] < 34:
        print("Too cold, please try again.")
    elif t_list[j] <= 35.5:
        print("Take a hot bath.")
    elif t_list[j] <= 38:
        print("Rest if feeling unwell.")
    elif t_list[j] <= 39:
        print("Take some medicine.")
    elif t_list[j] <= 41:
        print("Take a cold bath and some medicine.")
    elif t_list[j] <= 46.1:
        print("Go to the hospital.")
    elif t_list[j] <= 50:
        print("Congrats, you have a new world record!")
    else:
        print("Too hot, please try again.")