

from models.user import User
from models.recipe import Recipe
from models.ingredient import Ingredient

def exit_program():
    """ Exit the program """
    print("Goodbye!")
    exit()

def create_user():
    """ Create a new user """
    username = input("Enter username: ")
    email = input("Enter email: ")
    try:
        User.create(username, email)
        print("User created successfully.")
    except Exception as e:
        print(f"Error creating user: {e}")

def delete_user():
    """ Delete a user """
    user_id = input("Enter the user's id: ")
    try:
        user = User.find_by_id(user_id)
        if user:
            user.delete()
            print(f"User {user_id} deleted successfully.")
        else:
            print(f"User {user_id} not found.")
    except Exception as e:
        print(f"Error deleting user: {e}")

def display_users():
    """ Display all users """
    users = User.get_all()
    for user in users:
        print(user)

def create_recipe():
    """ Create a new recipe """
    name = input("Enter recipe name: ")
    instructions = input("Enter recipe instructions: ")
    user_id = int(input("Enter user id: "))  # Assuming user_id is required to associate recipe with a user
    try:
        Recipe.create(name, instructions, user_id)
        print("Recipe created successfully.")
    except Exception as e:
        print(f"Error creating recipe: {e}")

def delete_recipe():
    """ Delete a recipe """
    recipe_id = input("Enter the recipe id: ")
    try:
        recipe = Recipe.find_by_id(recipe_id)
        if recipe:
            recipe.delete()
            print(f"Recipe {recipe_id} deleted successfully.")
        else:
            print(f"Recipe {recipe_id} not found.")
    except Exception as e:
        print(f"Error deleting recipe: {e}")

def display_recipes():
    """ Display all recipes """
    recipes = Recipe.get_all()
    for recipe in recipes:
        print(recipe)

def create_ingredient():
    """ Create a new ingredient """
    name = input("Enter ingredient name: ")
    # Add more fields as needed (e.g., quantity, unit)
    try:
        Ingredient.create(name)
        print("Ingredient created successfully.")
    except Exception as e:
        print(f"Error creating ingredient: {e}")

def delete_ingredient():
    """ Delete an ingredient """
    ingredient_id = input("Enter the ingredient id: ")
    try:
        ingredient = Ingredient.find_by_id(ingredient_id)
        if ingredient:
            ingredient.delete()
            print(f"Ingredient {ingredient_id} deleted successfully.")
        else:
            print(f"Ingredient {ingredient_id} not found.")
    except Exception as e:
        print(f"Error deleting ingredient: {e}")

def display_ingredients():
    """ Display all ingredients """
    ingredients = Ingredient.get_all()
    for ingredient in ingredients:
        print(ingredient)
