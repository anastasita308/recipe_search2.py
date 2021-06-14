import requests
import random
# erase the contents of the text file before running it
open('listrecipe.txt', 'w').close()
open('saverecipe.txt', 'w').close()

def recipe_search(ingredient):
# Register to get an APP ID and key https://developer.edamam.com/
    app_id = '17c0000a'
    app_key = '4ecb31af986187378f22fcb62e68a004'
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}&cuisineType={}'.format(ingredient, app_id, app_key, cuisine_type)
    response = requests.get(url)
    recipe_label = response.json()['hits']
    return recipe_label

# list of cuisines
cuisine = ['American',
           'Asian',
           'British',
           'Caribbean',
           'Central Europe',
           'Chinese',
           'Eastern Europe',
           'French',
           'Indian',
           'Italian',
           'Japanese',
           'Kosher',
           'Mediterranean',
           'Mexican',
           'Middle Eastern',
           'Nordic',
           'South American',
           'South East Asian']

amount = int(input('How many ingredients would you like to enter? '))
for ingredient in range(amount):
    ingredient = input('Enter an ingredient: ')
# random cuisine type
cuisine_type = random.choice(cuisine)

print('Your cuisine type for today is ' + cuisine_type)
# I want some spaces!!
print()
print('Bon appetit!')
print()

def run_output():
    results = recipe_search(ingredient)
# for loop to display the results
    for result in results:
        recipe = result['recipe']
        label = recipe['label']
        url_recipe = recipe['url']
        calories = str(round(recipe['calories']))
        output = label + ' - ' + calories + ' calories' + '\n' + url_recipe + '\n'
        print(output)

# read the txt file
        with open('listrecipe.txt', 'r') as recipe_file:
            contents = recipe_file.read()

            contents = contents + '\n' + output

# write the labels down
        with open('listrecipe.txt', 'w+') as recipe_file:
            recipe_file.write(contents)
    ask_more()

def ask_more():
    question = input('Would you like to know the ingredients list for the specific dish? y/n ')
    # condition - based on the response
    if question == 'y':
        dish = input('Please copy the dish name from the list: ')
        ask_dish(dish)
    else:
        print('Bye!')

def ask_dish(dish):
    app_id = '17c0000a'
    app_key = '4ecb31af986187378f22fcb62e68a004'
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(dish, app_id, app_key)
    # GET request for the dish name
    response = requests.get(url)
    dish_output = response.json()['hits']
    results = dish_output
    # for loop to get to the recipe list
    for result in results:
        recipe = result['recipe']
        ingredients_list = recipe['ingredients']
        # for loop to iterate the ingredients
        for ingredients in ingredients_list:
            text = ingredients['text']
            print(text)
            # read the txt file
            with open('saverecipe.txt', 'r') as recipe_file:
                contents = recipe_file.read()

                contents = contents + '\n' + text

            # write the labels down
            with open('saverecipe.txt', 'w+') as recipe_file:
                recipe_file.write(contents)


run_output()

print()
print('Thank you for your attention!')