# Problem: coci12c5p1

line = input()
scale = ''
major_note = 0
minor_note = 0
first = True

for i in range(len(line)):
    if first:
        if line[i] == 'C' or line[i] == 'F' or line[i] == 'G':
            major_note += 1
        if line[i] == 'A' or line[i] == 'D' or line[i] == 'E':
            minor_note += 1
        first = False

    else:
        if line[i] == '|':
            first = True

if major_note > minor_note:
    scale = 'C-dur'
elif minor_note > major_note:
    scale = 'A-mol'
elif major_note == minor_note:
    if line[-1] == 'C':
        scale = 'C-dur'
    elif line[-1] == 'A':
        scale = 'A-mol'

print(scale)