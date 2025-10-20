# Problem: coci06c5p1

swaps = input()

ball_location = 1

# Loop the swaps
for swap_type in swaps:
    # Swaps are processed by a nested if statement
    if swap_type == 'A' and ball_location == 1:
        # The if statement checks to see where the ball is
        #  and checks the swap type. If both are true, then
        #  the if statement is processed, and the location
        #  changes.
        ball_location = 2
    elif swap_type == 'A' and ball_location == 2:
        ball_location = 1
    elif swap_type == 'B' and ball_location == 2:
        ball_location = 3
    elif swap_type == 'B' and ball_location == 3:
        ball_location = 2
    elif swap_type == 'C' and ball_location == 1:
        ball_location = 3
    elif swap_type == 'C' and ball_location == 3:
        ball_location = 1

print(ball_location)