# Problem: primes1

# define variables
num = int(input())
j = 0
x = 2

def isPrime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

while j < num:
    if isPrime(x) == True:
        print(x)
        j += 1
    x += 1