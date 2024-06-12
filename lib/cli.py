from models.user import User
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.recipe_ingredient import RecipeIngredient

def display_menu():
    print("Recipe Manager")
    print("1. Add User")
    print("2. Add Recipe")
    print("3. Add Ingredient to Recipe")
    print("4. View Users")
    print("5. View Recipes")
    print("6. View Ingredients")
    print("7. Delete User")
    print("8. Delete Recipe")
    print("9. Delete Ingredient")
    print("10. Exit")

def add_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    User.create(username, email)
    print("User added successfully.")

def add_recipe():
    name = input("Enter recipe name: ")
    instructions = input("Enter recipe instructions: ")
    user_id = int(input("Enter user ID: "))
    Recipe.create(name, instructions, user_id)
    print("Recipe added successfully.")

def add_ingredient():
    recipe_id = int(input("Enter recipe ID: "))
    ingredient = input("Enter ingredient: ")
    RecipeIngredient.create(recipe_id, ingredient)
    print("Ingredient added successfully.")

def view_users():
    users = User.get_all()
    for user in users:
        print(user)

def view_recipes():
    recipes = Recipe.get_all()
    for recipe in recipes:
        print(recipe)

def view_ingredients():
    ingredients = Ingredient.get_all()
    for ingredient in ingredients:
        print(ingredient)

def delete_user():
    user_id = int(input("Enter user ID to delete: "))
    User.delete(user_id)
    print("User deleted successfully.")

def delete_recipe():
    recipe_id = int(input("Enter recipe ID to delete: "))
    Recipe.delete(recipe_id)
    print("Recipe deleted successfully.")

def delete_ingredient():
    ingredient_id = int(input("Enter ingredient ID to delete: "))
    Ingredient.delete(ingredient_id)
    print("Ingredient deleted successfully.")

def run():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_user()
        elif choice == '2':
            add_recipe()
        elif choice == '3':
            add_ingredient()
        elif choice == '4':
            view_users()
        elif choice == '5':
            view_recipes()
        elif choice == '6':
            view_ingredients()
        elif choice == '7':
            delete_user()
        elif choice == '8':
            delete_recipe()
        elif choice == '9':
            delete_ingredient()
        elif choice == '10':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()
