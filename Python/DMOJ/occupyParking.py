# Problem: ccc18j2

# three lines of input:
#  n = number of parking spaces
#  yesterday = yesterday's parking space info
#  today = today's parking space info

# n is usually ignored in irl situations

n = int(input())
yesterday = input()
today = input()

# defining occupied
#  used to definte # of occupied parking spaces
occupied = 0

# begins to loop through indices of yesterday and today
for i in range(len(yesterday)):
    # we check whether the parking space was occupied each day
    if yesterday[i] == 'C' and today [i] == 'C':
        # if it was, then add 1 to occupied
        occupied = occupied + 1

print(occupied)