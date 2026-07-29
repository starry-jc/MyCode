# problem: ccc08j2

songs = 'ABCDE'

button = 0

# while loop continues as long as button 4 hasn't been pressed
while button != 4:
    button = int(input())
    presses = int(input())
    # We need to loop each button press
    for i in range(presses):
        if button == 1:
            # Slice the song so that the first is now the last
            songs = songs[1:] + songs[0]
        elif button == 2:
            # Slice the song so that the last is now the first
            songs = songs[-1] + songs[:-1]
        elif button == 3:
            # Slice the song so that the first and second are swapped
            songs = songs[1] + songs[0] + songs[2:]
        
output = ''

for song in songs:
    output = output + song + ' '

print(output[:-1])