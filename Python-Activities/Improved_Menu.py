class Menu:
    def appetizer(self, item, quantity):
        return f"Appetizer Order: {quantity} pcs of {item}"

    def main_course(self, item, quantity):
        return f"Main Course Order: {quantity} pcs of {item}"

    def drinks(self, item, quantity):
        return f"Drinks Order: {quantity} pcs of {item}"

    def dessert(self, item, quantity):
        return f"Dessert Order: {quantity} pcs of {item}"


def get_quantity():
    """Ask the user for quantity safely."""
    while True:
        try:
            quantity = int(input("How many orders?: "))
            if quantity > 0:
                return quantity
            else:
                print("Enter a positive number!")
        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    get_order = Menu()
    order_again = ""

    while order_again != "N":
        print("\nWelcome to the Restaurant!")
        print("1 - Appetizers\n2 - Main Courses\n3 - Drinks\n4 - Desserts")
        print("==================================")

        # Get valid menu choice
        while True:
            try:
                choice = int(input("Enter your choice (1-4): "))
                if choice in [1, 2, 3, 4]:
                    break
                else:
                    print("Invalid choice! Enter 1-4.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        # Dictionary to map choices to menu items
        menu_options = {
            1: {"a": "Salad", "b": "Bread"},
            2: {"a": "Steak", "b": "Fried Chicken"},
            3: {"a": "Water", "b": "Coke"},
            4: {"a": "Vanilla Ice Cream", "b": "Halo-Halo"}
        }

        category_name = {1: "Appetizer", 2: "Main Course", 3: "Drink", 4: "Dessert"}

        # Display options for the chosen category
        options = menu_options[choice]
        print(f"Available {category_name[choice]}s:")
        for key, item in options.items():
            print(f"{key} - {item}")

        # Get valid item choice
        while True:
            item_choice = input(f"Enter your {category_name[choice]} choice: ").lower()
            if item_choice in options:
                item_name = options[item_choice]
                break
            else:
                print("Invalid input! Please choose a valid option.")

        # Get quantity safely
        quantity = get_quantity()

        # Call the correct Menu method
        if choice == 1:
            print(get_order.appetizer(item_name, quantity))
        elif choice == 2:
            print(get_order.main_course(item_name, quantity))
        elif choice == 3:
            print(get_order.drinks(item_name, quantity))
        elif choice == 4:
            print(get_order.dessert(item_name, quantity))

        # Ask if user wants to order again
        while True:
            order_again = input("Do you want to order again? (Y/N): ").upper()
            if order_again in "YN":
                break
            else:
                print("Invalid input! Please enter Y or N.")

    print("Thank you for ordering!")


if __name__ == "__main__":
    main()
