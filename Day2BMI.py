height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#bmi = str(height / (weight ** weight))
#print(bmi)

bmi = float(weight) / float(height) ** 2
print(bmi)
bmi_as_integer = int(bmi)
print(bmi_as_integer)