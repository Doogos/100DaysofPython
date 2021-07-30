#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
#Inputs
bill = float(input("How much is the bill? "))
ppl = int(input("How many people are splitting the bill? "))
tip = int(input("How much would you like to tip?"))

#Calculations
tippercent = tip / 100
ttip = bill * tippercent
tbill = bill + ttip
split = tbill / ppl
total = round(split, 2)

#Print totals
print("##############")
print(f"Total bill: ${bill}")
print(f"Amount of people: {ppl}")
print(f"Tip amount: {int(tip)}%")
print(f"Each person should pay: ${total}")
print("##############")
