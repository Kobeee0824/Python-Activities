class Menu:
  def appetizer(self, appetizer, quantity):
    return (f"Appetizer Order: {quantity}pcs of {appetizer}")
  def main_course(self, main_course, quantity):
    return (f"Main Course order: {quantity}pcs of {main_course}")
  def drinks(self, drinks, quantity):
    return (f"Drinks Order: {quantity}pcs of {drinks}")
  def dessert(self, dessert, quantity):
    return (f"Dessert Oders: {quantity}pcs of {dessert}")

def main():
    
    get_order = Menu()
    order_again = ""

    while order_again != "N": 
      
      appetizer_choice = ""
      main_course_choice = ""
      drinks_choice = ""
      dessert_choice = ""
      quantity = 0

      print("Welcome to the Restaurant!")
      print("1 - Appetizers\n2 - Main Courses\n3 - Drinks\n4 - Desserts")
      print("==================================")

      while True:
        try: 
          choice = int(input("Enter you choice: "))
        except ValueError:
          print("Invalid Input!")


        if (choice == 1):
          print("Available Appetizers: \na - Salad\nb - Bread")
          appetizer_choice = input("Enter Appetizer: ")
          if (appetizer_choice == "a"):
            appetizer_choice = "Salad"
            quantity = input("How many orders?: ")
            print(get_order.appetizer(appetizer_choice, quantity))
          elif (appetizer_choice == "b"):
            appetizer_choice = "Bread"
            quantity = input("How many orders?: ")
            print(get_order.appetizer(appetizer_choice, quantity))
          else:
            print("Invalid Input!")

        elif (choice == 2):
          print("Available Main Courses:\na - Steak\nb - Fried Chicken")
          main_course_choice = input("Enter Main Course: ")
          if (main_course_choice == "a"):
            main_course_choice = "Steak"
            quantity = input("How many orders?: ")
            print(get_order.main_course(main_course_choice, quantity))
          elif (main_course_choice == "b"):
            main_course_choice = "Fried Chicken"
            quantity = input("How many orders?: ")
            print(get_order.main_course(main_course_choice, quantity))
          else:
            print("Invalid Input!")
          
        elif (choice == 3):
          print("Available Drinks:\na - Water\nb - Coke")
          drinks_choice = input("Enter Drinks: ")
          if (drinks_choice == "a"):
            drinks_choice == "Water"
            quantity = input("How many orders?: ")
            print(get_order.drinks(drinks_choice, quantity))
          elif (drinks_choice == "b"):
            drinks_choice == "Coke"
            quantity = input("How many orders?: ")
            print(get_order.drinks(drinks_choice, quantity))
          else:
            print("Invalid Input!")

        
        elif (choice == 4):
          print("Available Desserts:\na - Vanilla Ice Cream\nb - Halo-Halo")
          dessert_choice = input("Enter Dessert: ")
          quantity = input("How many orders?: ")
          if dessert_choice == "a":
            dessert_choice = "Vanilla Ice Cream"
            print(get_order.dessert(dessert_choice, quantity))
          elif dessert_choice == "b":
            dessert_choice = "Halo-Halo"
            print(get_order.dessert(dessert_choice, quantity))
          else:
            print("Invalid Input!")

        else:
          print("Invalid Input!")



        while True:
          order_again = input("Do you want to order again?(Y/N): ").upper()
          if order_again in "YN".upper():
            break #kapag ganito, ay eexit sa current loop. so babalik lang siya sa taas.
          else:
            print("Invalid Input! Please Enter Y or N ONLY")
    print("Thank you for ordering!")



if __name__ == "__main__":
  main()

  