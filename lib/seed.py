from models.user import User
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.recipe_ingredient import RecipeIngredient

def initialize_database():
    """Initialize the database by creating tables."""
    Recipe.drop_table()
    Recipe.create_table()

    Ingredient.drop_table()
    Ingredient.create_table()

    RecipeIngredient.drop_table()
    RecipeIngredient.create_table()

    User.drop_table()
    User.create_table()

    print("Tables created successfully.")

def seed_data():
    """Seed data into the tables."""
    # Seed data for ingredients
    ingredient1 = Ingredient.create("Flour")
    ingredient2 = Ingredient.create("Sugar")
    ingredient3 = Ingredient.create("Eggs")
    ingredient4 = Ingredient.create("Chocolate")

    # Seed data for recipes
    recipe1 = Recipe.create("Chocolate Cake", "Delicious chocolate cake recipe")
    recipe2 = Recipe.create("Pancakes", "Classic pancakes with syrup")

    # Seed data for recipe-ingredient relationships
    RecipeIngredient.create(recipe1.recipe_id, ingredient1.ingredient_id, 2)
    RecipeIngredient.create(recipe1.recipe_id, ingredient2.ingredient_id, 1)
    RecipeIngredient.create(recipe1.recipe_id, ingredient3.ingredient_id, 3)
    RecipeIngredient.create(recipe2.recipe_id, ingredient1.ingredient_id, 1)
    RecipeIngredient.create(recipe2.recipe_id, ingredient2.ingredient_id, 1)

    # Seed data for users
    user1 = User.create("alice", "alice@example.com")
    user2 = User.create("bob", "bob@example.com")

    print("Seed data inserted successfully.")

if __name__ == "__main__":
    initialize_database()
    seed_data()
