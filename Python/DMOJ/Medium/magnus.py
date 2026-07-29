# Problem: coci18c3p1

# Defining word
word = input()
subword = 'HONI'
i = 0
# Calculating the length of HONI
m = len(subword)

for char in word:
    if char == subword[i % m]:
        # For every char in subword, add 1 to i
        i += 1

# Then divide the total number of chars in the word by m
print(i // m)