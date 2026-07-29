# Problem: pwindsor18p4

# defining inputs and sorting them alphabetically
adamBag = sorted(input())
lettersInBag = sorted(input())
found = False

# checking for matches
for i in range(len(lettersInBag)):
    if adamBag[i] == lettersInBag[i]:
        # if the characters match, do nothing
        pass
    else:
        # if they don't match, output the character in adamBag
        print(adamBag[i])
        found = True
        break

# check for last letter
if found == False:
    print(adamBag[-1])