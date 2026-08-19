# Problem: cspc1p4

import math

# Assigning variables

# d - days left in break
d = int(input())
# p - number of pages in book
p = int(input())
# class_code - class code as a string
class_code = input()
# n - number of students in class
n = int(input())
# i_list - n inputs including student name,
#  daily number of pages read, and class code
i_list = []

# i_name - List of names created from the nested
#  list in i_list
i_name = []
# i_ppd - List of pages per day created from the
#  nested list in i_list
i_ppd = []
# i_class_code - List of class codes created from the
#  nested list in i_class_code
i_class_code = []

# Iterates for a total of n times:
#  Adds and splits all of inputs into i_list, which
#  creates nested lists of all of the split inputs.
#  Adds a specific element of each nested list into
#  i_name, i_ppd, and i_class_code from the main list.
for i in range(n):
    i_list.append(input().split())
    
    i_name.append(i_list[-1][0])
    i_ppd.append(i_list[-1][1])
    i_class_code.append(i_list[-1][2])

# efficient_readers - empty list of efficient readers
efficient_readers = []
# efficient_pages - empty list of the efficient number of pages
efficient_pages = []
# most_efficient_readers - empty list of the most efficient
#  readers from the efficient_readers list
most_efficient_readers = []
# ppd_main - variable containing the minimum ppd. default value
#  set to 0
ppd_min = 0

# Iterates through the length of i_name:
#  Checks to see if the index j in i_class_code is not equal to
#  the class_code variable. If true, ignores the value.
#  Otherwise, tries the following:
#    if the integer of p / d, rounded to the upper value, is less
#    than or equal to the integer of the element j in i_ppd,
#    then efficient_readers and efficient_pages will append
#    the element j in i_name and i_ppd (respectively).
#    Assuming there is a ZeroDivisionError, continue the code
#    as normal.
for j in range(len(i_name)):
    if i_class_code[j] != class_code:
        pass
    else:
        try:
            if int(math.ceil(p / d)) <= int(i_ppd[j]):
                efficient_readers.append(i_name[j])
                efficient_pages.append(i_ppd[j])

        except ZeroDivisionError:
                continue

# Iterates through the length of efficient_pages:
#  Checks to see if the integer value of efficient_pages at element
#  k is less than the ppd minimum or the ppd minimum is equal to 0.
#  If either is true, then ppd_min will be set to the new value of
#  the integer version of efficient_pages at element k.
#  Checks to see if the integer value of element k in efficient_pages
#  is equal to the ppd minimum.
#  If so, add the reader at element k of efficient_readers into
#  most_efficient_readers list.
for k in range(len(efficient_pages)):
    if int(efficient_pages[k]) < ppd_min or ppd_min == 0:
        ppd_min = int(efficient_pages[k])
        
    if int(efficient_pages[k]) == ppd_min:
        most_efficient_readers.append(efficient_readers[k])

# Checks to see if the length of most_efficient_readers is equal
#  to one. If it is, print who the most efficient reader is.
#    Checks to see if the ppd minimum is equal to the integer value of
#    p / d rounded to the upper value. If so, print that the reader is
#    perfectly efficient. Otherwise, Print that none of the readers are
#    perfectly efficient.
#  If the length of most_efficient_readers is equal to 0,
#  print that none of the readers are perfectly efficient.
#  Otherwise, print who the most efficient readers are (there are multiple).
#    If the ppd minimum is equal to the integer of p / d rounded to the upper
#    value, print these readers are perfectly efficient.
#    Otherwise, print that none of the readers are perfectly efficient.
if len(most_efficient_readers) == 1:
    print(f"The most efficient reader is {most_efficient_readers[0]}.")
    if ppd_min == int(math.ceil(p / d)):
        print("This reader is perfectly efficient.")
    else:
        print("None of the readers are perfectly efficient.")
elif len(most_efficient_readers) == 0:
    print("None of the readers are perfectly efficient.")
else:
    print(f"The most efficient readers are {",".join(most_efficient_readers)}.")
    if ppd_min == int(math.ceil(p / d)):
        print("These readers are perfectly efficient.")
    else:
        print("None of the readers are perfectly efficient.")

