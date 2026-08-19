# Problem: alphabetscore

# Defining variables:

# s - the input string
s = input()
# turn s into a list
list(s)

# score - represents tha alphabet score; starts
#  with a default of 0
score = 0

# alphabet_dict - creates a dictionary
#  where each key is paired with an alphabet value
alphabet_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

# iterates through the length of s:
#  Checks to see if the element at index i of s
#  is inside of alphabet_dict
#    If so, the score will add the value found at
#    the key of the element at index i of s to itself
for i in range(len(s)):
    if s[i] in alphabet_dict:
        score += alphabet_dict[s[i]]

# Outputs the score
print(score)