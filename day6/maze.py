# Lost in a maze
# Reeborg was exploring a dark maze and the battery in its flashlight ran out.

# Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.
# t you need to know
# The functions move() and turn_left().
# Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
# How to use a while loop and if/elif/else statements.
# It might be useful to know how to use the negation of a test (not in Python).

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def clear_right():
    while right_is_clear():
        turn_right()
        move()
def right_wall():
    while wall_on_right():
        if wall_in_front():
            turn_left()
        else:
            move()
def clear_front():
    while front_is_clear():
        move()
        turn_left()  
while not at_goal():
    if right_is_clear():
        clear_right()
    elif wall_on_right():
        right_wall()
    elif front_is_clear():
        clear_front()
    else:
        turn_left()