# # # [A.T.M.]
class ATM:
    def __init__(self, balance=0, pin="1234"):
      self.balance = balance
      self.pin = pin

    def check_balance(self):
        print(f"Your current balance is ${self.balance}")

    def deposit(self):
        amount = float(input("Enter amount to deposite: "))
        self.balance += amount
        print(f"${amount} deposited successfully!")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdraw successfully!")
        else:
            print(f"Insufficient balance!")

    def change_pin(self):
        new_pin = input("Enter new PIN:")
        self.pin = new_pin
        print("PIN changed successfully!")

    def menu(self):
        while True:
            print("\n---- ATM MENU ----")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Change PIN")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self. withdraw()
            elif choice == "4":
                self.change_pin()
            elif choice == "5":
                print("Thank you for using our ATM! ")
                break

            else:
                print("Invalid choice! Please try again.")


    # # --- Main Program --- # #
print("===Welcome to Python Bank ATM===")

atm = ATM(balance=5000, pin="1234")  # create ATM object with default balance

entered_pin = input("Enter your PIN: ")

if entered_pin == atm.pin:
    atm.menu()
else:
    print("Incorrect PIN! Access Denied.")