from helpers import *

def main_menu():
    while True:
        print("\n--- Recipe Manager ---")
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
        choice = input("Enter your choice: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            create_recipe()
        elif choice == '3':
            add_ingredient_to_recipe()
        elif choice == '4':
            display_users()
        elif choice == '5':
            display_recipes()
        elif choice == '6':
            display_ingredients()
        elif choice == '7':
            delete_user()
        elif choice == '8':
            delete_recipe()
        elif choice == '9':
            delete_ingredient()
        elif choice == '10':
            exit_program()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
