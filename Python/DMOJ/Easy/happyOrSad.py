# Problem: ccc15j2

# Assigning sentence variable
sentence = input()

# Counting :-) in sentence
#  Assign variable happy
happy = sentence.count(":-)")

# Counting :-( in sentence
#  Assign variable sad
sad = sentence.count(":-(")

# if statement
if happy > sad:
    print("happy")
elif happy < sad:
    print("sad")
elif happy == 0 and sad == 0:
    print("none")
elif happy == sad:
    print("unsure")