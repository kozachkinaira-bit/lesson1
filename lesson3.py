class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def show_balance(self):
        print(f"balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"+${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"-${amount}")
        else:
            print("Not enough money")

    

mono = BankAccount("123", 100)

mono.show_balance()
mono.deposit(100)
mono.withdraw(100)
mono.show_balance()
