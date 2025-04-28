from user import User


class Bankomat:
    def __init__(self):
        self.logged_user = None

    def log_in(self, user: User, entered_pin):
        if user.pin == entered_pin:
            self.logged_user = user
            print(f"Witaj, {user.name}!")
        else:
            print("Błędny PIN.")

    def log_out(self):
        if self.logged_user:
            print(f"Do widzenia, {self.logged_user.name}!")
            self.logged_user = None

    def deposit_money(self, amount):
        if self.logged_user:
            self.logged_user.account.deposit(amount)
        else:
            print("Musisz się zalogować.")

    def withdraw_money(self, amount):
        if self.logged_user:
            self.logged_user.account.withdraw(amount)
        else:
            print("Musisz się zalogować.")

    def check_balance(self):
        if self.logged_user:
            self.logged_user.account.check_balance()
        else:
            print("Musisz się zalogować.")