#import random

# randomInteger = random.randint(1,10)
# print(randomInteger)

# randomFloat = random.random() * 5
# print(randomFloat)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

states_of_america = ["Delaware", "Pennsylvania", "Tennessee", "Georgia", "Homerland"]
print(states_of_america[1])

print(states_of_america[-2])

states_of_america[1] = "Pencilvania"
print(states_of_america[1])

#states_of_america.append("Angelaland")
states_of_america.extend(["Angelaland", "Documentationland"])
print(states_of_america)