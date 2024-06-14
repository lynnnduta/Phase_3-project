# Phase 3 CLI+ORM Project

## PROJECT TITLE: Recipe Manager CLI
### Date: 2024/06/13
### By: Lynn Wainaina

## Description
A Python CLI application that helps manage users, recipes, and ingredients. The system allows users to add, view, delete, and find users, recipes, and ingredients, offering an efficient way to handle recipe management.

## MINIMAL VIABLE PRODUCT (MVP)

### 1. Database Management with ORM Methods
Implemented a database using Python ORM methods to handle data storage and manipulation. The data model includes three primary classes: User, Recipe, and Ingredient. Established relationships where each user can have multiple recipes, and each recipe can have multiple ingredients.

### 2. Data Model Requirements
- **User class**
  - Attributes: `id` (primary key), `username`, `email`
- **Recipe class**
  - Attributes: `id` (primary key), `name`, `user_id` (foreign key)
- **Ingredient class**
  - Attributes: `id` (primary key), `name`
- **RecipeIngredient class**
  - Attributes: `recipe_id` (foreign key), `ingredient_id` (foreign key), `quantity`
- Property methods to add constraints to ensure valid data entry.
- ORM methods for each class to create, delete, get all, and find by name.

### 3. CLI Requirements
- A user-friendly CLI that displays interactive menus for users to navigate through the application.
- Options for each class to create an object, delete an object, display all objects, and find an object by attribute.
- User input validation and informative error messages to guide users through the process.
- The CLI will use loops to keep the user in the application until they choose to exit.

## Installation

1. Clone the repository:
   
   git clone git@github.com:lynnnduta/Phase_3-project.git

## PROJECT STRUCTURE
config/__init__.py: Contains database connection setup.
lib/cli.py: The entry point for the CLI application. Manages the main menu and user interactions.
lib/helpers.py: Contains helper functions to support the main functionality of the CLI. These include operations like listing, finding, creating, updating, and deleting records for users, recipes, and ingredients.
lib/models/user.py: Contains the User class and its methods for database operations.
lib/models/recipe.py: Contains the Recipe class and its methods for database operations.
lib/models/ingredient.py: Contains the Ingredient class and its methods for database operations.
lib/models/recipe_ingredient.py: Contains the RecipeIngredient class and its methods for database operations.
lib/seed.py: Populates the database with initial seed data for users, recipes, and ingredients. Useful for testing and development purposes.
db/recipe_manager.db: SQLite database file where all the data for the Recipe Manager is stored. This includes information about users, recipes, and ingredients.
## Technologies Used
Python 3.x
SQLite
## Support and Contact Details
For support and further inquiries, please visit git@github.com:lynnnduta

## License
The content of this site is licensed under the MIT license. Copyright (c) 2024.