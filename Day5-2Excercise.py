# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Not allowed to use the max or min functions.

# Calculate best grade in class
best_grade = 0
for g in student_scores:
    if g > best_grade: best_grade = g
print(f"The highest score in the class is: {best_grade}")

# Calculate the lowest grade in class
lowest_grade = 100
for l in student_scores:
    if l < lowest_grade: lowest_grade = l
print(f"the lowest score in the class is: {lowest_grade}")

# Calculate the average grade in class
average_grade = 0
summed_grades = 0
for a in student_scores:
    summed_grades += a

counted_grades = 0
for c in student_scores:
    counted_grades += 1

average_grade = int(summed_grades / counted_grades)
print(f"The average grade in the class is: {round(average_grade)}")