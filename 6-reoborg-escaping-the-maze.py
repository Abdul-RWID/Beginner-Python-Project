# You're going to be learning about FUNCTION, INDENTATIONS, CODE BLOCKS & WHILE LOOP

# This is just a note, don't run this file because it will be error.


def TURN_RIGHT():
    TURN_LEFT()
    TURN_LEFT()
    TURN_LEFT()



def maze():
    while front_is_clear():
        move()
    turn_left()

    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()
