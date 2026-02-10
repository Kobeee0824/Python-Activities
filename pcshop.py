class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} - ${self.price}"

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        print("\nShopping Cart:")
        for idx, item in enumerate(self.items, start=1):
            print(f"{idx}. {item}")
        print(f"Total: ${self.get_total()}")
    
    def get_total(self):
        return sum(item.price for item in self.items)
    
    def clear_cart(self):
        self.items.clear()

class PCShop:
    def __init__(self):
        self.products = [
            Product("Laptop", 1200),
            Product("Desktop", 1000),
            Product("Keyboard", 50),
            Product("Mouse", 25),
            Product("Monitor", 300),
            Product("Graphics Card", 500),
            Product("RAM 16GB", 80),
            Product("SSD 512GB", 100)
        ]
        self.cart = ShoppingCart()

    def show_products(self):
        print("\nAvailable Products:")
        for idx, product in enumerate(self.products, start=1):
            print(f"{idx}. {product}")

    def place_order(self):
        if not self.cart.items:
            print("Your cart is empty. Add some products before placing an order.")
            return
        
        print("\nFinalizing your order...")
        self.cart.view_cart()
        name = input("Enter your name: ")
        address = input("Enter your delivery address: ")
        phone = input("Enter your phone number: ")

        print("\nOrder Summary:")
        self.cart.view_cart()
        print(f"\nOrder placed successfully! Thank you for shopping with us, {name}.")
        print(f"Delivery details:\nName: {name}\nAddress: {address}\nPhone: {phone}")
        
        self.cart.clear_cart()  # Clear cart after placing the order

def main():
    shop = PCShop()

    while True:
        print("\nWelcome to the PC Shop!")
        print("1. View products")
        print("2. Add product to cart")
        print("3. View cart")
        print("4. Place order")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            shop.show_products()
        elif choice == '2':
            shop.show_products()
            product_choice = int(input("Enter the product number to add to cart: ")) - 1
            if 0 <= product_choice < len(shop.products):
                shop.cart.add_product(shop.products[product_choice])
                print(f"{shop.products[product_choice].name} added to your cart.")
            else:
                print("Invalid product number.")
        elif choice == '3':
            shop.cart.view_cart()
        elif choice == '4':
            shop.place_order()
        elif choice == '5':
            print("Thank you for visiting the PC Shop. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
