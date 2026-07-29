# Problem: dmopc14ce1p1

# defining variables
subject = "tu"
verb = input()
object = list(input())
article = ""

# checking the letter the object ends in
if object[-1] == 'e':
    # set the article to be feminine
    article = "la"
elif object[-1] == 's':
    # set the article to be plural
    article = "les"
else:
    # set the article to be masculine
    article = "le"

# output
print(f"{verb}-{subject} {article} {''.join(object)} ?")