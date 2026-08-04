# Problem: dwite08c1p1

# n_list - empty list that will contain all of the inputs
n_list = []

# Increments the variable i for a total of 5 times
#  after adding every input into n_list
for i in range(5):
    n_list.append(int(input()))

# Increments the variable j for a total of 5 times to
#  represent the number of rows.
#    Increments the variable k for a total of the length
#    of n_list times. In this loop, uses a long if-elif-
#    else chain to acknowledge all output possibilities
#    based on the input (this is possible given the small
#    amount of inputs that are available).
#      In summary, if the element at index k in n_list is
#      0-5, then it would output either a period, an x, or
#      a series of a combination based on the value. These
#      numbers represent the height of the pile of x that will
#      appear, which is why there is an if statement (or elif)
#      for every possibility. 
#    Outside of the nested for loop (with "for k..."), output a
#    \n so that it would start a new row.
for j in range(5): # rows
    for k in range(len(n_list)): # columns
        if n_list[k] == 0:
            print('.', end='')
            
        elif n_list[k] == 1:
            if j == 4:
                print('x', end='')
            else:
                print('.', end='')
                
        elif n_list[k] == 2:
            if j == 3:
                print('.x.', end='')
            elif j == 4:
                print('xxx', end='')
            else:
                print('...', end='')
                
        elif n_list[k] == 3:
            if j == 2:
                print('..x..', end='')
            elif j == 3:
                print('.xxx.', end = '')
            elif j == 4:
                print('xxxxx', end='')
            else:
                print('.....', end='')
                
        elif n_list[k] == 4:
            if j == 1:
                print('...x...', end='')
            elif j == 2:
                print('..xxx..', end='')
            elif j == 3:
                print('.xxxxx.', end='')
            elif j == 4:
                print('xxxxxxx', end='')
            else:
                print('.......', end='')
                
        elif n_list[k] == 5:
            if j == 0:
                print('....x....', end='')
            elif j == 1:
                print('...xxx...', end='')
            elif j == 2:
                print('..xxxxx..', end='')
            elif j == 3:
                print('.xxxxxxx.', end='')
            elif j == 4:
                print('xxxxxxxxx', end='')
            else:
                print('........', end='')
                
    print('\n')