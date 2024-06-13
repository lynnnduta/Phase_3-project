from models.user import User
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.recipe_ingredient import RecipeIngredient

def exit_program():
    print("Goodbye!")
    exit()

def create_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    user = User.create(username, email)
    print(f"User created: {user}")

def delete_user():
    user_id = input("Enter the user's id: ")
    user = User.find_by_id(user_id)
    if user:
        user.delete()
        print(f"User {user_id} deleted")
    else:
        print(f"User {user_id} not found")

def display_users():
    users = User.get_all()
    for user in users:
        print(user)

def create_recipe():
    name = input("Enter recipe name: ")
    user_id = input("Enter user id: ")
    recipe = Recipe.create(name, user_id)
    print(f"Recipe created: {recipe}")

def delete_recipe():
    recipe_id = input("Enter the recipe's id: ")
    recipe = Recipe.find_by_id(recipe_id)
    if recipe:
        recipe.delete()
        print(f"Recipe {recipe_id} deleted")
    else:
        print(f"Recipe {recipe_id} not found")

def display_recipes():
    recipes = Recipe.get_all()
    for recipe in recipes:
        print(recipe)

def create_ingredient():
    name = input("Enter ingredient name: ")
    ingredient = Ingredient.create(name)
    print(f"Ingredient created: {ingredient}")

def delete_ingredient():
    ingredient_id = input("Enter the ingredient's id: ")
    ingredient = Ingredient.find_by_id(ingredient_id)
    if ingredient:
        ingredient.delete()
        print(f"Ingredient {ingredient_id} deleted")
    else:
        print(f"Ingredient {ingredient_id} not found")

def display_ingredients():
    ingredients = Ingredient.get_all()
    for ingredient in ingredients:
        print(ingredient)

def add_ingredient_to_recipe():
    recipe_id = input("Enter recipe id: ")
    ingredient_id = input("Enter ingredient id: ")
    recipe_ingredient = RecipeIngredient.create(recipe_id, ingredient_id)
    print(f"Ingredient {ingredient_id} added to recipe {recipe_id}")


