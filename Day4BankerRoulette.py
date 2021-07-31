# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# My attempt at this challenge - I believe it accomplishes the same as the solution
# import random
# random.shuffle(names)
# print(f"{names[0]}, you must pay the bill!")

# Solution as listed by course
import random
#Get the total number of items in the list.
num_items = len(names)
#Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items -1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")