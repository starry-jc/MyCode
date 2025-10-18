# Problem: ccc11s1

n = int(input())

ts = 0
ss = 0
language = ''

for i in range(n):
    prompt = input()

    for k in range(len(prompt)):
        if prompt[k] == 't' or prompt[k] == 'T':
            ts = ts + 1

        if prompt[k] == 's' or prompt[k] == 'S':
            ss = ss + 1

if ts > ss:
    language = 'English'
elif ss > ts:
    language = 'French'
elif ts == ss:
    language = 'French'

print(language)