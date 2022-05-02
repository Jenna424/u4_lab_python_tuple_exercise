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
# Using a for loop, print just the last two food strings from foods
for index in range(1, 3):
    print(foods[index])
# Create a dictionary named home_town containing the keys of city, state and population
# Print a string with this format:
# "I was born in city, state - population of population"
home_town = {
    'city': 'Westfield',
    'state': 'New Jersey',
    'population': 500
}
print('I was born in {}, {} - population of {}'.format(
    home_town['city'], home_town['state'], home_town['population']))
