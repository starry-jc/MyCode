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
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z'
}

# iterates through the length of s:
#  iterates through the keys and values of
#  alphabet_dict:
#    Checks to see if index i in the list of
#    s is equal to the value inside alphabet_dict.
#      If true, score will add the key each time.
for i in range(len(s)):
    for key, value in alphabet_dict.items():
        if s[i] == value:
            score += key

# Outputs the score
print(score)