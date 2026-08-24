# Problem: olympics

import math

n, b, s, g = map(int, input().split())

canada_score = b * 1 + s * 3 + g * 5
num_medals = []

remaining_score = n - canada_score + 1

min_medals = math.ceil(remaining_score / 5)
print(min_medals)

'''print(remaining_score)'''

'''if remaining_score < 1:
    print(0)
elif remaining_score == 1:
    print(1)
else:
    num_medals.append(math.ceil(remaining_score / 1))
    num_medals.append(math.ceil(remaining_score / 3))
    num_medals.append(math.ceil(remaining_score / 5))
    
    print(num_medals)

    for i in range(len(num_medals)):
        if num_medals[i] < min_medals or min_medals == 0:
            min_medals = num_medals[i]

    print(num_medals[-1])'''