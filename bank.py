class ATM:
    def __init__(self, balance):
        self.balance = balance
        self.pin = "1111"

    def login(self, pin):
        if self.pin == pin:
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"[withdraw] -${amount}")
        else:
            raise ValueError("Not enough money")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"[deposit] +${amount}")

atm = ATM(1000)

attempts = 3
is_login = False

while True:
    if not is_login:
        pin = input(f"Enter your pin ({attempts}):")
        if not atm.login(pin):
            attempts -= 1
            print("Invalid PIN")
            if attempts <= 0:
                print("Card blocked")
                break
            continue
    print("Menu:")
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Balance: ${atm.balance}")
    elif choice == 2:
        if atm.login(pin):
            amount = int(input("Enter your amount: "))
            try:
                atm.deposit(amount)
            except ValueError as e:
                print(e)
    elif choice == 3:
        if atm.login(pin):
            amount = int(input("Enter your amount: "))
            try:
                atm.withdraw(amount)
            except ValueError as e:
                print(e)
        else:
            print("Invalid PIN")
    else:
        break