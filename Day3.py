print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0
if height >= 120:
    print("You can ride!")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12
    print(f"Your total bill is {bill}")
else:
    print("You must be taller to ride.")
