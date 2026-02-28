# Ex 1
def manage_students():
    students =['student1', 'student2', 'student3']
    second_student= students[1]
    last_student=students[-1]
    return (second_student, last_student)
    # your code here

print('Exercise 1:', manage_students( ))


# Ex 2
def combine_foods():
    foods = ('carrot', 'celery', 'potato')
    meal=""

    for food in foods:
        meal+= food + ""
    return meal.strip()
# Create a tuple named foods with three food strings.
# Create a variable named meal and assign it an empty string "".
# Use a for loop to concatenate each food into meal, separated by a space.
# Return the final string.

print('Exercise 2:', combine_foods())

# Ex 3.
def slice_foods():
    foods = ("salad", "pot-pie", "pizza", "tacos", "sushi", "stew")
    slice_two= foods[-2:]
    return slice_two


print('Exercise 3:', slice_foods())

# Ex. 4
def hometown_info():
    home_town = {
        "city": "Buffalo",
        "state": "NY",
        "population": 278000
    }

    return f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"

print('Exercise 4:', hometown_info())


# Ex 5
def list_home_town_items():
     home_town = {
        "city": "Buffalo",
        "state": "NY",
        "population": 278000
    }
     home_town_items=[]
     for key, value in home_town.items():
        home_town_items.append(f"{key} = {value}")

     return home_town_items

print('Exercise 5:', list_home_town_items())