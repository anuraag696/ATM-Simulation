class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def check_pin(self):
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:
            return True
        else:
            print("Wrong PIN.")
            return False

    def check_balance(self):
        print("Your balance is:", self.balance)

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print("Money deposited. New balance:", self.balance)

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            print("Money withdrawn. New balance:", self.balance)
        else:
            print("Insufficient balance.")

    def start(self):
        if self.check_pin():
            while True:
                print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
                choice = input("Choose an option: ")
                if choice == '1':
                    self.check_balance()
                elif choice == '2':
                    self.deposit()
                elif choice == '3':
                    self.withdraw()
                elif choice == '4':
                    print("Thank you for using the ATM.")
                    break
                else:
                    print("Invalid option.")

# Run
atm = ATM("1234", 1000)
atm.start()
