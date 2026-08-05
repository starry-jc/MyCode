# Problem: cspc1p4

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


i_name = []
i_wpd = []
i_class_code = []


for i in range(n):
    i_list.append(input().split())
    
    i_name.append(i_list[-1][0])
    i_wpd.append(i_list[-1][1])
    i_class_code.append(i_list[-1][2])

efficient_readers = []

try:
    for j in range(len(i_name)):
        if i_class_code[j] != class_code:
            i_name.remove(i_name[j])
            i_wpd.remove(i_wpd[j])
            i_class_code.remove(i_class_code[j])
            
        try:
            if round(p / d) == int(i_wpd[j]):
                efficient_readers.append(i_name[j])
        except ZeroDivisionError:
            continue
except IndexError:
    pass
        


if len(efficient_readers) == 1:
    print(f"The most efficient reader is {efficient_readers[0]}.")
    print("This reader is perfectly efficient.")
elif len(efficient_readers) == 0:
    print("None of the readers are perfectly efficient.")
else:
    print(f"The most efficient readers are {",".join(efficient_readers)}.")
    print("These readers are perfectly efficient.")