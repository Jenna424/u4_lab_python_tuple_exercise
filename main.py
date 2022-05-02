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
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"
for key in home_town:
    print('{} = {}'.format(key, home_town[key]))

# Create an empty list named cohort
# Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape
# {
#    'student': 'Tina',
#    'fav_food' 'Cheeseburger'
#  }
# Iterate over cohort printing out each element.
cohort = []
for index in range(len(students)):
    cohort.append({
        'student': students[index],
        'fav_food': foods[index]})
for student in cohort:
    print(student)

# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string.
awesome_students = ['{} is awesome!'.format(student) for student in students]
for string in awesome_students:
    print(string)
