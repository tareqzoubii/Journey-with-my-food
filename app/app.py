import pprint
# from tkinter import N
from recipes import recipes

def user_interact():
    print("\n")
    print("------------Hello, Welcome to our Application ------------")
    print("\n")
    print("Here You can find the best recipes for your favorite food")
    print("\n")
    print("----------------------------------------------------------")
    print("\n")

    recipe=(input("Please, Select your recipe --> ").lower())
    what_to_know=input(" \n Do you want to know about\n 1: Ingredients \n 2: Calories \n 3: Cuisine Type \n 4: Fat \n 5: Carbs \n 6: Colesterol \n \n q: Exit the app \n \n (by choosing a number)  \n ")

    recipes.set_q(recipe)
    recipes.get_data()
    try:
        # pprint.pprint(recipes.get_data())
        while what_to_know != "q":
            if what_to_know == '1':
                ing = recipes.get_ingredients()
                print(f" The ingredienst in this {recipe} is {ing} ")
            elif what_to_know == '2':
                cal = recipes.get_calories()
                pprint.pprint(f" This {recipe} is contain {cal} calories")
            elif what_to_know == '3':
                cuis = recipes.get_cuisine_type()
                pprint.pprint(f" The Cuisine Type is {cuis} Dish ")
            elif what_to_know == '4':
                fat = recipes.get_food_fat()
                pprint.pprint(f" This dish contain {fat} % of fat ")
            elif what_to_know == '5':
                carbs = recipes.get_food_carbs()
                pprint.pprint(f" This dish contain {carbs} % of carbs ")
            elif what_to_know == '6':
                col = recipes.get_food_colesterol()
                pprint.pprint(f" This dish contain {col} % of colesterol ")
            elif what_to_know == 'q':
                return
            what_to_know = input("If you want more information please choose a number --> ")    
    except IndexError as err:
            pprint.pprint("This dish in not in our menu")

user_interact()