# Create a list named students containing some student names (strings)
students = ['Jenna', 'Molly', 'Nghiem']
# Print out the second student's name
print(students[1])
# Print out the last student's name
print(students[-1])

# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list
foods = ('apple', 'banana', 'orange')
# Use a for loop to print out the string "food goes here is a good food"
for food in foods:
    print('{} is a good food'.format(food))
