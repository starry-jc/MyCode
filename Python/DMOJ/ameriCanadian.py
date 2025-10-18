# Problem: ccc02j2

word = ''
translation = []

while word != 'quit!':
    word = input()

    if len(word) > 4:
        for char in word:
            if (word[-1] == 'r' and word[-2] == 'o' and
                word[-3] not in ['a', 'e', 'i', 'o', 'u', 'y']):
                word = word[:-1] + 'u' + word[-1]
    
    translation.append(word)

output = ''
for t in translation[:-1]:
    output = output + t + '\n'
print(output[:-1])