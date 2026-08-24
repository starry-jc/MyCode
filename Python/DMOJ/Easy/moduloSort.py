# Problem: modulosort

# Defining variables

n = int(input())
k = int(input())
m = int(input().split())

modulo_dict = dict.fromkeys(m, 0)

for i in range(len(m)):
    modulo_dict[i] = m[i] % k

print(modulo_dict)