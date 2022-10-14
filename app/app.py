import pprint
from recipes import recipes

def user_interact():
    print("\n")
    print("------------Hello, Welcome to our Application ------------")
    print("\n")
    print("Here You can find the best recipes for your favorite food")
    print("\n")
    print("----------------------------------------------------------")
    print("\n")

    recipe=input("Please, Select your recipe --> ")
    what_to_know=input(" \n Do you want to know about\n 1: Ingredients \n 2: Calories \n 3: Cuisine Type \n 4: Exit the app \n \n  (by choosing a number)  \n ")

    recipes.set_q(recipe)
    recipes.get_data()
    
    # pprint.pprint(recipes.get_data())
    while what_to_know != "4":
        if what_to_know == '1':
            ing = recipes.get_ingredients()
            pprint.pprint(f" The ingredienst in this dish is {ing} ")
        elif what_to_know == '2':
            cal = recipes.get_calories()
            pprint.pprint(f" This dish is contain {cal} calories")
        elif what_to_know == '3':
            cuis = recipes.get_cuisine_type()
            pprint.pprint(f" The Cuisine Type is {cuis} Dish ")
        elif what_to_know == '4':
            return
        what_to_know = input("If you want more information please choose a number --> ")    
        

user_interact()