# Problem: ccc15j1

# Assigning variables month and day
month = int(input())
day = int(input())

# Assigning special day
special_month = 2
special_day = 18

# Assigning if statements with operators
if (month < special_month):
    print('Before')
elif (month > special_month):
    print('After')
elif (month == special_month):
    if (day == special_day):
        print('Special')
    elif (day < special_day):
        print('Before')
    elif (day > special_day):
        print('After')