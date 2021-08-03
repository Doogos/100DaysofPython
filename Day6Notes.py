# Day_6_Notes = ["Code Blocks and Indentations", "Functions", "While Loops"]

# Code Blocks and Indentations

# Blocks are made by indenting code within a function or if/else statements.
# Visualize each indentation with a container to better understand code
#Typical indentation is four "4" spaces - spaces are preferred by python


###################################################################################
# Functions

# Simple print function
print("Hello")

# Print number of character in string
num_char = len("Hello")
print(num_char)

# Create function - needs to be triggered, or called.
def my_function():
    print("Hello")
    print("Bye")


# Trigger or "call" the function
my_function()

#Defining Functions
# def name_of_function():
    #do this (these must be indented)
    #do this
    #do this
# Calling Functions
# name_of_function()

###################################################################
# Reeborg game Challenge
###################################################################
#def turn_around():
#    turn_left()
#    turn_left()

#def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()

#def jump():
#    turn_left()
#    move()
#    turn_right()
#    move()
#    turn_right()
#    move()
#    turn_left()

#move()
#jump()
#move()
#jump()
#move()
#jump()
#move()
#jump()
#move()
#jump()
#move()
#jump()
#####################################################################
###########################################################################################


# While Loops
 
 #Reeborg's World example from before
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()

hurdles = 6
while hurdles > 0:
    jump()
    hurdles -= 1
    print(hurdles)

#While Loop
while something_is_true:
    #Do this
    #Then do this
    #Then do this
    #Do this until contidition becomes false

# Hurdle 2 Challenge:
while front_is_clear():
    jump()
    if at_goal() == True:
        break
    else:
        continue

while not at_goal():
    jump()

# Infinite Loop
while 5 > 3:
    #Do this
    #Then do this
    #This will always go  on because five is greater than three.

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