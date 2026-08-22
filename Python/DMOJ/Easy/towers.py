# Problem: towers

# Defining variables
n = int(input())
t = input()

good_towers = []

t_list = t.split()
t_list = list(map(int, t_list))

for i in range(len(t_list)):
    if i == 0 or i == (len(t_list) - 1):
        pass
    
    try:
        if t_list[i] > t_list[i-1] and t_list[i] < t_list[i+1]:
            good_towers.append(t_list[i])
    except IndexError:
        pass

print(len(good_towers))