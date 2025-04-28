class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Wpłacono {amount} PLN. Nowe saldo: {self.balance} PLN.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Niewystarczające środki.")
            return False
        else:
            self.balance -= amount
            print(f"Wypłacono {amount} PLN. Nowe saldo: {self.balance} PLN.")
            return True

    def check_balance(self):
        print(f"Twoje saldo: {self.balance} PLN.")