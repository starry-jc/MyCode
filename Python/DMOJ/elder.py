# Problem: coci18c4p1

og_wizard = input()
duels = int(input())
current_owner = og_wizard
obeyed = 1
current_owners = [og_wizard]

for i in range(duels):
    duel = input()
    z1 = duel[0]
    z2 = duel[2]

    if z2 == current_owner:
        current_owner = z1
        if current_owner not in current_owners:
            current_owners.append(current_owner)

print(current_owner)
print(len(current_owners))