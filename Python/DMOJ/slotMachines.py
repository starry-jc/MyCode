# Problem: ccc00s1

quarters = int(input())
first = int(input())
second = int(input())
third = int(input())

plays = 0

while quarters >= 1:
    # determine current machine based on number of plays
    machine = plays % 3
    quarters = quarters - 1

    if machine == 0:
        first = first + 1
        # determine whether martha gets paid
        if first % 35 == 0:
            quarters = quarters + 30
    elif machine == 1:
        second = second + 1
        if second % 100 == 0:
            quarters = quarters + 60
    elif machine == 2:
        third = third + 1
        if third % 10 == 0:
            quarters = quarters + 9

    plays = plays + 1

print(f'Martha plays {plays} times before going broke.')