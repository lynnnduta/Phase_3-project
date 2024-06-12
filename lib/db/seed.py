from config import CONN, CURSOR
from models.user import User
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.recipeingredient import RecipeIngredient

def seed_data():
    User.create_table()
    Recipe.create_table()
    Ingredient.create_table()
    RecipeIngredient.create_table()

    # Seed users
    User.create("user1", "user1@example.com")
    User.create("user2", "user2@example.com")

    # Seed recipes
    Recipe.create("Recipe 1", "Instructions for Recipe 1", 1)
    Recipe.create("Recipe 2", "Instructions for Recipe 2", 2)

    # Seed ingredients
    Ingredient.create("Ingredient 1")
    Ingredient.create("Ingredient 2")

    # Seed recipe ingredients
    RecipeIngredient.create(1, 1)
    RecipeIngredient.create(1, 2)
    RecipeIngredient.create(2, 1)

if __name__ == "__main__":
    seed_data()
