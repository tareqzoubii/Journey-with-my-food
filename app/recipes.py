import os
import pprint
import requests
from dotenv import load_dotenv



class Recipes:
    
    """
    a class is created to give information of food based on meal name!
    """
    # q menas the query or the name of the dish you need!

    count = 0
    __instance__ = None # to lock my class!!

    def __init__(self):
        if Recipes.__instance__ is None: # accessing my constructor
            Recipes.__instance__ = self
            self.q = None
            self.r = None
            self.api_key = os.getenv("API_KEY")
            Recipes.count += 1
        else:
            raise Exception("We can not create another class")
    
    def set_q(self, q):
        self.q = q

    def get_data(self): # instance method --> request function
        self.url1 = f'https://api.edamam.com/api/recipes/v2?type=public&beta=true&q={self.q}&app_id=4d4e4afa&app_key={self.api_key}&ingr=0-8&random=false'
        self.r = requests.get(self.url1).json()
        return self.r

    def get_ingredients(self):
        ingredients = self.r['hits'][0]['recipe']['ingredientLines']
        return ingredients

    def get_calories(self):
        calories =  self.r['hits'][0]['recipe']['calories']
        return calories

    def get_cuisine_type(self):
        cuisine_type = self.r['hits'][0]['recipe']['cuisineType']
        return cuisine_type


load_dotenv()
recipes=Recipes()
#recipes2=Recipes() # it's protected Now ;)
# print(Recipes.count)
# recipes.set_q('chicken pizza')
# print(recipes.r)
# pprint.pprint(recipes.get_ingredients())
# pprint.pprint(recipes.get_calories())
# pprint.pprint(recipes.get_cuisine_type())




"""
    url1="https://api.edamam.com/api/recipes/v2?type=public&beta=true&q=chicken%20pizza&app_id=4d4e4afa&app_key=f6e97255f8b975bddcdd9834fc5f11fe&ingr=5-8&random=false"

r = requests.get(url1)
# print(r.status_code)
# pprint.pprint(r.json())
json = r.json()

"""      

"""
now we need function for each option the user choose --> 
ingredients and calories and the cuisine type
"""
# for x in json['hits']:
#     y = x['recipe']
#     ingredient= y['ingredientLines']
# # print(ingredient)

# for x in json['hits']:
#     y = x['recipe']
#     calories = y['calories']
# # print(calories)

# for x in json['hits']:
#     y = x['recipe']
#     cuisine_type= y['cuisineType']
# # print(cuisine_type)