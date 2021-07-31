import random

#Game resources
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

cheat = '''
....................../´¯/) 
....................,/¯../ 
.................../..../ 
............./´¯/'...'/´¯¯`·¸ 
........../'/.../..../......./¨¯\ 
........('(...´...´.... ¯~/'...') 
.........\.................'.../ 
..........\............... _.·´ 
............\..............( 
..............\.............\
'''

#Asking for user input, numbers make it easier for syntax
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))

#My original thought was to create a list and make a random choice from the list
#options = [0, 1, 2]
#npc = random.choice(options)

#While typing original code, remembered to used randint then created if/else statements to print choice
npc = random.randint(0, 2)

#Player choice
print("You chose:")
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("cheater")

#Computer choice
print("Computer chose:")
if npc == 0:
    print(rock)
elif npc == 1:
    print(paper)
else:
    print(scissors)

#Game rules
if choice == npc:
    print("Tie")
elif choice >= 3 or choice <= 0:
    print("You lose")
    print(cheat)
elif choice == 0 and npc == 1:
    print("You lose")
elif choice == 1 and npc == 2:
    print("You lose")
elif choice == 2 and npc == 0:
    print("You lose")
else:
    print("You win")
