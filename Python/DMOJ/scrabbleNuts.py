# Problem: rgpc17p5

N, M = map(int, input().split())

A = input()
A_list = []
B = input()
B_list = []
operation = 0

if len(A) > N:
    for i in range(N):
        A_list.append(A[i])
else:
    for i in range(len(A)):
        A_list.append(A[i])

if len(B) > M:
    for i in range(M):
        B_list.append(B[i])
else:
    for i in range(len(B)):
        B_list.append(B[i])

while len(B_list) >= 2:
    B_list.pop(-1)
    for i in range(len(A_list)):
        if len(B_list) <= i:
            operation += 1 # This is remove
            'print("remove")'
        elif A_list[i] != B_list[i]:
            operation += 1 # This is swap
            'print("swap")'

    if len(A_list) < len(B_list):
        operation += ((len(B_list)) - len(A_list)) # This is add
        'print("add")'

print(operation)