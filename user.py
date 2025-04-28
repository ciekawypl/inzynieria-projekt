from account import Account

class User:
    def __init__(self, name, pin, account: Account):
        self.name = name
        self.pin = pin
        self.account = account