
class Account:
    def __init__(self):
        self.balance = 0
        self.name = "Tolani"
        self.account_number = None

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Amount cannot be negative")

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
        else:
            raise ValueError("Amount cannot be negative")

    def airtime_purchase(self, amount):
        if amount > 0:
            self.balance -= amount
        else:
            raise ValueError("Amount cannot be negative")

    # @staticmethod
    def transfer(self, amount, account):
        self.withdraw(amount)

        account.deposit(amount)



