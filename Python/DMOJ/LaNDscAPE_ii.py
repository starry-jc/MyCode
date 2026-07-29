# Problem: dwite08c1p1

n_list = []

for i in range(5):
    n_list.append(int(input()))

for j in range(5): # columns
    for k in range(6): # rows
        print('.', end='')
    print('\n')