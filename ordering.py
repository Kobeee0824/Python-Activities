# Simple Ordering System in Python

menu = {
    1: {"name": "Burger", "price": 5.99},
    2: {"name": "Pizza", "price": 8.49},
    3: {"name": "Pasta", "price": 6.99},
    4: {"name": "Fries", "price": 2.99},
    5: {"name": "Soda", "price": 1.50}
}

order = {}

def show_menu():
    print("\n--- MENU ---")
    for item_id, item in menu.items():
        print(f"{item_id}. {item['name']} - ${item['price']:.2f}")

def add_item():
    try:
        item_id = int(input("Enter item number: "))
        if item_id in menu:
            quantity = int(input("Enter quantity: "))
            order[item_id] = order.get(item_id, 0) + quantity
            print("Item added to order.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Please enter valid numbers.")

def remove_item():
    try:
        item_id = int(input("Enter item number to remove: "))
        if item_id in order:
            del order[item_id]
            print("Item removed.")
        else:
            print("Item not in order.")
    except ValueError:
        print("Invalid input.")

def view_order():
    if not order:
        print("\nYour order is empty.")
        return

    print("\n--- YOUR ORDER ---")
    total = 0
    for item_id, quantity in order.items():
        item = menu[item_id]
        cost = item["price"] * quantity
        total += cost
        print(f"{item['name']} x {quantity} = ${cost:.2f}")
    print(f"Total: ${total:.2f}")

def checkout():
    view_order()
    print("\nThank you for your order!")
    exit()

def main():
    while True:
        print("\n--- ORDERING SYSTEM ---")
        print("1. Show Menu")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. View Order")
        print("5. Checkout")

        choice = input("Choose an option: ")

        if choice == "1":
            show_menu()
        elif choice == "2":
            add_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            view_order()
        elif choice == "5":
            checkout()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
