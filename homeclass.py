class SailendraInvestmentAdvanceBank:

    def __init__(self):
        self.balance = 0

    def welcome(self):
        print("   Sailendra INVESTMENT ADVANCE BANK (CIAB)")
        print("Welcome to our bank!")

    def create_account(self):
        self.name = input("\nEnter your full name: ")
        self.account_no = input("Create Account Number: ")

        initial_deposit = float(input("Enter Initial Deposit Amount: Rs. "))
        self.balance = initial_deposit

        print("Account Created Successfully!")
        print("Account Holder:", self.name)
        print("Account Number:", self.account_no)

    def check_balance(self):
        print("Current Balance = Rs.", self.balance)

    def deposit(self):
        amount = float(input("Enter amount to deposit: Rs. "))
        self.balance += amount
        print("Deposit Successful!")
        print("Updated Balance = Rs.", self.balance)

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: Rs. "))

        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful!")
            print("Remaining Balance = Rs.", self.balance)
        else:
            print("Insufficient Balance!")

    def menu(self):
        while True:
            print("BANK MENU ")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.check_balance()

            elif choice == "2":
                self.deposit()

            elif choice == "3":
                self.withdraw()

            elif choice == "4":
                print("Thank you for banking with")
                print("Sailendra Investment Advance Bank!")
                break

            else:
                print("Invalid Choice!")


bank = SailendraInvestmentAdvanceBank()

bank.welcome()
bank.create_account()
bank.menu()