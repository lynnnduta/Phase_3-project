from helpers import (
    exit_program, create_user, delete_user, display_users, 
    create_recipe, delete_recipe, display_recipes, 
    create_ingredient, delete_ingredient, display_ingredients, 
    add_ingredient_to_recipe
)

def main():
    while True:
        print("Recipe Manager CLI")
        print("1. View all users")
        print("2. Add a user")
        print("3. Delete a user")
        print("4. View all recipes")
        print("5. Add a recipe")
        print("6. Delete a recipe")
        print("7. View all ingredients")
        print("8. Add an ingredient")
        print("9. Delete an ingredient")
        print("10. Add ingredient to recipe")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_users()
        elif choice == "2":
            create_user()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            display_recipes()
        elif choice == "5":
            create_recipe()
        elif choice == "6":
            delete_recipe()
        elif choice == "7":
            display_ingredients()
        elif choice == "8":
            create_ingredient()
        elif choice == "9":
            delete_ingredient()
        elif choice == "10":
            add_ingredient_to_recipe()
        elif choice == "11":
            exit_program()
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
