# Problem: tsoc16c1p2

# defining variables
file_name = input()
x = '.'

# if "." isn't in file_name, add another line of input for the extension
if "." not in file_name:
    extension = input()
# if "." is in file_name, split file_name into a list of two separate parts - the file name and extension
if "." in file_name:
    file_extension = file_name.split(x)
    # redefine variables
    file_name = file_extension[0]
    extension = file_extension[1]

# output
print(f"\"{file_name}\" - {extension.lower()}")