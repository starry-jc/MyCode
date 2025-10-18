# Problem: coci13c3p1

k = int(input())

alist = [0] * 46
alist[2] = 1
for j in range(3, 46):
    alist[j] = alist[j - 1] + alist[j - 2]

blist = [0] * 46
blist[1] = 1
for i in range(2, 46):
    blist[i] = blist[i - 1] + blist[i - 2]

print(alist[k], blist[k])