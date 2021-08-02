# Range function starts at the 1, and the range does not include the second number.
# For example, a range(1, 10) does not include the number 10, you must put range(1, 11)
# The range function will by default print each digit in the range
# But you can add a third comma to indicate the steps it takes
# A range of 1, 11, 3 will output 1, 4, 7, 10 skipping to every third number.

# First example
# for number in range(1, 11, 3):
#     print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)
