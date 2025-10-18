# Problem: ccc20j2

estimate = int(input())
day0 = int(input())
infected = int(input())

day = 0
total_infected = day0

while total_infected <= estimate:
    day += 1
    day0 *= infected
    total_infected += day0

    if total_infected > estimate:
        print(day)