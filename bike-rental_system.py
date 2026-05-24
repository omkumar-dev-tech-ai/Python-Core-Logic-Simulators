# # Simple Bike Rental System using Class in Python

class BikeRental:
    def __init__(self, stock):
        self.stock = stock # total bike available

    def display_bikes(self):
        print(f"Total bikes available: {self.stock}")

    def rent_bike(self, qty):
        if qty <= 0:
            print("Enter a valid number of bikes!")
        elif qty > self.stock:
            print("Sorry, not enough bikes available!")
        else:
            self.stock += qty
            print(f"You have rented {qty} bike(s). Enjoy your ride!")
            print(f"Bike left in stock: {self.stock}")

    def return_bike(self, qty):
        if qty <= 0:
            print("Enter a valid number of bikes!")
        else:
            self.stock += qty
            print(f"Thank for returning {qty} bike(s)")
            print(f"Updated stock: {self.stock}")


# --- MAIN PROGRAM --- # #
bike_shop = BikeRental(10) # start with 10 bike

while True:
    print("\n=== Welcome to Bike Rental Shop ===")
    print("1. Display available bikes")
    print("2. Rent a bike")
    print("3. Return a bike")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        bike_shop.display_bikes()

    elif choice == "2":
        qty = int(input("Enter number of bikes to rent: "))
        bike_shop.return_bike(qty)

    elif choice == "3":
        qty = int(input("Enter number of bikes to return: "))
        bike_shop.return_bike(qty)

    elif choice == "4":
        print("Thank you for visiting! ")
        break

    else:
        print("Invalid choice, please try again.")