# # Simple Cafe Project using if-else in Python

print("=== Welcome to Python Cafe ===")
print("Menu")
print("1. Coffee - $50")
print("2. Tea - $30")
print("3. Sandwitch - $70")
print("4. Burger - $100")
print("5. Exit")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    print("You selected Coffee")
    qty = int(input("Enter quantity: "))
    total = 50 * qty
    print(f"Total amount: ${total}")

elif choice == 2:
    print("You selected Tea.")
    qty = int(input("Enter quantity: "))
    total = 30 * qty
    print(f"Total amount: ${total}")

elif choice == 3:
    print("You selected Sandwich.")
    qty = int(input("Enter quantity: "))
    total = 70 * qty
    print(f"Total amount: ${total}")

elif choice == 4:
    print("You selected Burger.")
    qty = int(input("Enter quantity: "))
    total = 100 * qty
    print(f"Total amount: ${total}")

elif choice == 5:
    print("Total you! Visit again ")

else:
    print("Invalid choice! Please select from 1 to 5.")




print("======= Welcome to Priya's Cafe =======")

menu = {
    1: ["Coffee", 40],
    2: ["Tea", 20],
    3: ["Burger", 80],
    4: ["Sandwich", 60],
    5: ["French Fries", 50],
    6: ["Pizza", 120]
}

# # Display menu
print("\n-------- Menu --------")
for key, item in menu.items():
    print(f"{key}. {item[0]} - ${item[1]}")
print("------------------\n")

total = 0

while True:
    # Multile Choice Input
    choice = int(input("Select your item (1-6): "))

    if choice in menu:
        item_name = menu[choice][0]
        item_price = menu[choice][1]

        qty = int(input(f"How many {item_name}?: "))

        cost = qty * item_price
        total += cost

        print(f"Added {qty} x {item_name} = ${cost}\n")
    else:
        print("Invalid choice! Please choose from 1-6.\n")

        # More items?
        more = input("Do you want to add more items? (yes/no): ").lower()
        if more == "no":
            break
print("\n====== Final Bill ======")
print(f"Total Amount: ${total}")
print("Thank you for visiting Priya's Cafe! ")