# Problem: nccc5j2

# Assigning inputs to variables

# n - the first line of input
#  represents the number of integers being compared
n = int(input())
# a_i - the second line of input
#  the integer values being compared in a single line
a_i = input()

# split values of a_i as a list
a_i_list = a_i.split()
# a_i_list - integer versions of each element in a_i_list
a_i_list = list(map(int, a_i_list))

# a_i_dict - empty dictionary for a_i elements and how
#  often they repeat
a_i_dict = {}

# iterates through a_i_list:
#  if the element i is in the empty a_i_dict,
#  the key, i, will have its value increment by 1.
#  otherwise, assign the key a value of 1.
for i in a_i_list:
    if i in a_i_dict:
        a_i_dict[i] += 1
    else:
        a_i_dict[i] = 1

# highest - the maximum value inside of a_i_dict
highest = max(a_i_dict.values())
# most_repeated - empty list that will contain the keys
#  of the repeated values
most_repeated = []

# iterates through the keys and values in a_i_dict:
#  if the value is equal to highest,
#  appends the key into most_repeated
for key, value in a_i_dict.items():
    if value == highest:
        most_repeated.append(key)

# sorts most_repeated by numerical value
most_repeated.sort()
# outputs the first index value
print(int(most_repeated[0]))
