# Problem: nccc5j2

n = int(input())
a_i = input()

a_i_list = a_i.split()
seen_vals = set()
removed_vals = []

for i in a_i_list:
    if i in seen_vals:
        removed_vals.append(i)
    else:
        seen_vals.add(i)

map(int, removed_vals)

print(removed_vals)

'''for j in range(n):
    int(a_i_list[j])
    for k in range(n):
        if a_i_list[j] == a_i_list[k]:
            repeated_vals.append(a_i_list[j])

print(repeated_vals)'''