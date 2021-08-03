# Hurdle 2 Challenge:
while front_is_clear():
    jump()
    if at_goal() == True:
        break
    else:
        continue

while not at_goal():
    jump()



# Hurdle 3 Challenge:
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front() == True:
        jump()
    elif front_is_clear():
        move()
    elif at_goal() == True:
        break
    else:
        continue

# Hurdle 4 Challenge

while not at_goal():
    if wall_in_front() and right_is_clear():
        turn_right()
        move()
    elif wall_in_front() == True:
        turn_left()    
    elif front_is_clear() and right_is_clear():
        turn_right()
        move()
    elif wall_in_front() and right_is_clear():
        turn_right()
    elif front_is_clear():
         move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif at_goal() == True:
        break
    else:
        continue


# Maze Challenge
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def walk():
    if front_is_clear() and wall_on_right():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front() and right_is_clear():
        turn_right()
        move()
    elif front_is_clear() and right_is_clear():
        turn_right()
        move()

    
while not at_goal():
    walk()