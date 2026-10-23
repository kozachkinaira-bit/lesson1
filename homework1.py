class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def show_balance(self):
        print(f"balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"[{self.account_number}] +${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"[{self.account_number}] -${amount}")
        else:
            print("Not enough money")

class Bank:
    def __init__(self, name):
        self.name = name

    def send(self, account1: BankAccount, account2: BankAccount, amount:int):
        if account1.balance >= amount:
            account1.withdraw(amount)
            account2.deposit(amount)

mono1 = BankAccount("123", 100)
mono2 = BankAccount("321", 100)

mono1.show_balance()
mono1.deposit(100)
mono1.withdraw(100)
mono1.show_balance()

monoBank = Bank("Mono")

monoBank.send(mono1, mono2, 100)
