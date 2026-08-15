# Problem: hkccc15j2

# defining variavbles
n = int(input())
x_list = []
y_list = []

x_dict = {}
y_dict = {}
coordinate_diff_dict = {}

for i in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

s_min = 20000**2

for j in range(n):
    for k in range(j+1, n):
        s_ij = max(abs(x_list[j] - x_list[k]), abs(y_list[j] - y_list[k])) ** 2

        if s_ij < s_min:
            s_min = s_ij

print(s_min)