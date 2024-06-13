from models.user import User
from models.recipe import Recipe
from models.ingredient import Ingredient
from models.recipe_ingredient import RecipeIngredient

User.drop_table()
User.create_table()

Recipe.drop_table()
Recipe.create_table()

Ingredient.drop_table()
Ingredient.create_table()

RecipeIngredient.drop_table()
RecipeIngredient.create_table()

# Creating seed data

# Seed data for users
user1 = User.create("john_doe", "john@example.com")
user2 = User.create("jane_doe", "jane@example.com")

# Seed data for recipes
recipe1 = Recipe.create("Pancakes", user1.id)
recipe2 = Recipe.create("Omelette", user2.id)

# Seed data for ingredients
ingredient1 = Ingredient.create("Flour")
ingredient2 = Ingredient.create("Eggs")
ingredient3 = Ingredient.create("Milk")
ingredient4 = Ingredient.create("Salt")

# Seed data for recipe ingredients
recipe_ingredient1 = RecipeIngredient.create(recipe1.id, ingredient1.id)
recipe_ingredient2 = RecipeIngredient.create(recipe1.id, ingredient2.id)
recipe_ingredient3 = RecipeIngredient.create(recipe1.id, ingredient3.id)
recipe_ingredient4 = RecipeIngredient.create(recipe2.id, ingredient2.id)
recipe_ingredient5 = RecipeIngredient.create(recipe2.id, ingredient4.id)

print(user1)
print(recipe1)
print(ingredient1)
print(recipe_ingredient1)
