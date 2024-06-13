 
from models.user import User
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.recipe_ingredient import RecipeIngredient

def populate_data():
    # Drop existing tables (if any) and create new ones
    User.drop_table()
    User.create_table()

    Recipe.drop_table()
    Recipe.create_table()

    Ingredient.drop_table()
    Ingredient.create_table()

    RecipeIngredient.drop_table()
    RecipeIngredient.create_table()

    # Creating seed data for my tables

    # Seed data for users
    user1 = User.create(username="Lynn_Wainaina", email="lynn@example.com")
    user2 = User.create(username="jane_Wendy", email="jane@example.com")
    user3 = User.create(username="emma_smith", email="emma@example.com")
    user4 = User.create(username="michael_brown", email="michael@example.com")
    user5 = User.create(username="sophia_adams", email="sophia@example.com")
    print(user1)
    print(user2)
    print(user3)
    print(user4)
    print(user5)

    # Seed data for recipes
    recipe1 = Recipe.create(name="Pancakes", user_id=user1.user_id)
    recipe2 = Recipe.create(name="Omelette", user_id=user2.user_id)
    print(recipe1)
    print(recipe2)

    # Seed data for ingredients
    ingredient1 = Ingredient.create(name="Flour")
    ingredient2 = Ingredient.create(name="Eggs")
    ingredient3 = Ingredient.create(name="Milk")
    ingredient4 = Ingredient.create(name="Salt")
    print(ingredient1)
    print(ingredient2)
    print(ingredient3)
    print(ingredient4)

    # Seed data for recipe ingredients
    recipe_ingredient1 = RecipeIngredient.create(recipe_id=recipe1.recipe_id, ingredient_id=ingredient1.ingredient_id, quantity=200)
    recipe_ingredient2 = RecipeIngredient.create(recipe_id=recipe1.recipe_id, ingredient_id=ingredient2.ingredient_id, quantity=3)
    recipe_ingredient3 = RecipeIngredient.create(recipe_id=recipe1.recipe_id, ingredient_id=ingredient3.ingredient_id, quantity=250)
    recipe_ingredient4 = RecipeIngredient.create(recipe_id=recipe2.recipe_id, ingredient_id=ingredient2.ingredient_id, quantity=4)
    recipe_ingredient5 = RecipeIngredient.create(recipe_id=recipe2.recipe_id, ingredient_id=ingredient4.ingredient_id, quantity=1)
    print(recipe_ingredient1)
    print(recipe_ingredient2)
    print(recipe_ingredient3)
    print(recipe_ingredient4)
    print(recipe_ingredient5)

if __name__ == "__main__":
    populate_data()
