# Problem: anct1

# defining variables
#  N = intervals
#  D = days
#  J = jumps
numIntervals, days = map(int, input().split())
intervals = input()
intervalsList = intervals.split()
potentialIntervals = []
jumpsList = []

for i in range(len(intervalsList)):
    intervalsList[i] = int(intervalsList[i])

    if days % intervalsList[i] == 0:
        potentialIntervals.append(intervalsList[i])

if not potentialIntervals:
    print("This is not the best time for a trip.")
else:
    for j in range(len(potentialIntervals)):
        jumps = abs(days / potentialIntervals[j])
        jumpsList.append(int(jumps))
    print(min(jumpsList))