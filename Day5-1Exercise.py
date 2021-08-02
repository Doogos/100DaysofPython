# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# Not allowed to use sum() or len() functions

#Print the list of heights
print(student_heights)

# Adding heights together
total = 0
for h in student_heights:
    total += h
print(f"The total heights added together is: {total}")

# Calculating total number of students
count = 0
for s in student_heights:
    count += 1
print(f"The total number of students is: {count}")

# Calculating the average of the student heights
a = round(total / count)
print(f"The average height is: {a}")


