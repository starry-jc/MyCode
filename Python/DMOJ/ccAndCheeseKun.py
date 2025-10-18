# Problem: dmopc16c1p0

# Assigning variables width and cheese
width = int(input())
cheese = int(input())

# if statements
if width == 3 and cheese >= 95:
    m = "absolutely"
elif width == 1 and cheese <= 50:
    m = "fairly"
else:
    m = "very"

# Output
print("C.C. is " + m + " satisfied with her pizza.")