#Treasure Island Game
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
direction = input("You stand in a beautiful courtyard with two paths, will you go left or right? ")
if direction == "left":
    decision = input("You approach a river, do you swim or wait around?")
    if decision == "wait":
        door = input("A boat picks you up and drops you off in front of a building with a red, blue, and yellow door. Which color door will you open? ")
        if door == "Red":
            print("The door leads to a room filled with fire!")
            print("GAME OVER")
        elif door == "Blue":
            print("The door leads to a room full of beasts!")
            print("GAME OVER")
        elif door == "Yellow":
            print("The door leads to a room full of treasure!")
            print("YOU WIN")
        else:
            print("You hurt yourself in confusion")
            print("HINT: Trying capitalizing the color of the door like Purple instead of purple")
            print("GAME OVER")
    else:
        print("You are attacked by trout.")
        print("GAME OVER")
else:
    print("You fall into a hole.")
    print("GAME OVER")