#Reeborg's solution:
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    turn_left()
    turn_left()

    
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front() and right_is_clear():
        turn_right()
    elif wall_in_front():
        turn_left()
    elif front_is_clear() and right_is_clear():
        turn_right()
    else:
        move()
