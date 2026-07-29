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

for j in range(n):
    for k in range(1, n):
        try:
            x_dict[f"difference_{j+1}"] = abs(x_list[j] - x_list[k])
            y_dict[f"difference_{j+1}"] = abs(y_list[j] - y_list[k])
        except IndexError:
            x_dict[f"difference_{j+1}"] = abs(x_list[-1] - x_list[0])
            y_dict[f"difference_{j+1}"] = abs(y_list[-1] - y_list[0])




'''for j in range(int((n * (n - 1)) / 2)):
    print(f"j: {j}")
    for k in range(1, n):
        print(f"k: {k}")
        try:
            x_dict[f"difference_{j+1}"] = abs(x_list[j] - x_list[k])
            y_dict[f"difference_{j+1}"] = abs(y_list[j] - y_list[k])
        except IndexError:
            print("index error")
            x_dict[f"difference_{j+1}"] = abs(x_list[-1] - x_list[0])
            y_dict[f"difference_{j+1}"] = abs(y_list[-1] - y_list[0])'''

print(x_dict)
print(y_dict)

print(x_list)
print(y_list)