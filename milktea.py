# Milk Tea Ordering System

MENU = {
    1: {"name": "Classic Milk Tea", "price": 50},
    2: {"name": "Okinawa Milk Tea", "price": 60},
    3: {"name": "Taro Milk Tea", "price": 65},
    4: {"name": "Matcha Milk Tea", "price": 70}
}

SIZES = {
    "S": 0,
    "M": 10,
    "L": 20
}

ADD_ONS = {
    1: {"name": "Pearls", "price": 10},
    2: {"name": "Pudding", "price": 15},
    3: {"name": "Cheese Foam", "price": 20}
}


def display_menu():
    print("\n--- Milk Tea Menu ---")
    for key, item in MENU.items():
        print(f"{key}. {item['name']} - ₱{item['price']}")


def display_sizes():
    print("\nSizes:")
    for size, price in SIZES.items():
        print(f"{size} (+₱{price})")


def display_add_ons():
    print("\nAdd-ons:")
    for key, item in ADD_ONS.items():
        print(f"{key}. {item['name']} - ₱{item['price']}")


def main():
    total = 0
    order_summary = []

    print("🧋 Welcome to Milk Tea Shop!")

    while True:
        display_menu()
        choice = int(input("\nSelect milk tea (number): "))

        if choice not in MENU:
            print("Invalid choice. Try again.")
            continue

        display_sizes()
        size = input("Choose size (S/M/L): ").upper()

        if size not in SIZES:
            print("Invalid size. Try again.")
            continue

        price = MENU[choice]["price"] + SIZES[size]

        display_add_ons()
        add_on_choice = input("Add add-on? (enter number or N): ").upper()

        add_on_name = "None"
        if add_on_choice != "N":
            add_on_choice = int(add_on_choice)
            if add_on_choice in ADD_ONS:
                price += ADD_ONS[add_on_choice]["price"]
                add_on_name = ADD_ONS[add_on_choice]["name"]

        qty = int(input("Quantity: "))
        item_total = price * qty
        total += item_total

        order_summary.append({
            "drink": MENU[choice]["name"],
            "size": size,
            "addon": add_on_name,
            "qty": qty,
            "subtotal": item_total
        })

        again = input("\nOrder another? (Y/N): ").upper()
        if again != "Y":
            break

    print("\n--- Receipt ---")
    for item in order_summary:
        print(f"{item['qty']}x {item['drink']} ({item['size']}) "
              f"Add-on: {item['addon']} - ₱{item['subtotal']}")

    print(f"\nTotal Amount: ₱{total}")
    print("Thank you for ordering! 🧋")


if __name__ == "__main__":
    main()
