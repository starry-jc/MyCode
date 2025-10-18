# Problem: ccc06j1

# Assigning variables burger, side, drink, dessert
burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

# Setting if statements for burgers
if burger == 1:
    burger_cal = 461
elif burger == 2:
    burger_cal = 431
elif burger == 3:
    burger_cal = 420
else:
    burger_cal = 0

# Setting if statments for sides
if side == 1:
    side_cal = 100
elif side == 2:
    side_cal = 57
elif side == 3:
    side_cal = 70
else:
    side_cal = 0

# Setting if statements for drinks
if drink == 1:
    drink_cal = 130
elif drink == 2:
    drink_cal = 160
elif drink == 3:
    drink_cal = 118
else:
    drink_cal = 0

# Setting if statements for desserts
if dessert == 1:
    dessert_cal = 167
elif dessert == 2:
    dessert_cal = 266
elif dessert == 3:
    dessert_cal = 75
else:
    dessert_cal = 0

# Adding it all together
total_cal = burger_cal + side_cal + drink_cal + dessert_cal
print("Your total Calorie count is " + str(total_cal) + ".")