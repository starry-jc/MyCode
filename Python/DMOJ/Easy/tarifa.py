# Problem: coci16c1p1

monthly_mb = int(input())
n = int(input())

total_mb = monthly_mb * n
for _ in range(n):
    used = int(input())
    total_mb = total_mb - used

print(total_mb + monthly_mb)