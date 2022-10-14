
from unicodedata import name
from urllib import response
import  pytest
import requests
from app.recipes import recipes


def test_get_check_status_code_equals_200():
     response = requests.get(f'https://api.edamam.com/api/recipes/v2?type=public&beta=true&q=burger&app_id=4d4e4afa&app_key=f6e97255f8b975bddcdd9834fc5f11fe&ingr=0-8&random=false')
     assert response.status_code == 200




def test_get_ingredients():
    #  response = requests.get(f'https://api.edamam.com/api/recipes/v2?type=public&beta=true&q=burger&app_id=4d4e4afa&app_key=f6e97255f8b975bddcdd9834fc5f11fe&ingr=0-8&random=false')
     recipes.set_q("burger")
     recipes.get_data()
     
     assert recipes.get_ingredients() == [
"2 1/2 pounds skirt steak or sirloin flap steak",
"Accompaniments: homemade burger buns ; homemade ketchup ; homemade mustard ; homemade pickle relish ; lettuce and tomato"
]


def test_get_calories():
    recipes.set_q("burger")
    recipes.get_data()
    assert recipes.get_calories() == 2211.26280375


def test_get_calories():
    recipes.set_q("burger")
    recipes.get_data()
    assert recipes.get_cuisine_type() == ['american']