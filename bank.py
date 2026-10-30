class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"[withdraw] -${amount}")
        else:
            pass

bank = BankAccount(100)
bank.withdraw(150)

print(bank.balance)