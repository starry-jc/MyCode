# Problem: aac1p4

N, Q = map(int, input().split())

mystring = input().split()
a = []
for i in range(N):
    a.append(int(mystring[i]))

for i in range(Q):
    l, r, x = map(int, input().split())
    answer = 0
    for s in range(l - 1, r):
        for t in range(s + 1, r):
            if a[s] != a[t] and a[s] * a[t] == x:
                answer = 1
    if answer == 0:
        print("NO")
    else:
        print("YES")