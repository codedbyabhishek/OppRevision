#Hiding the internal details of an object and only exposing what's necessary.
#why it protect data from outside interference and misuse.
class BankAccount:
    def __init__(self, balance):
        self._balance = balance # private variable
    def deposit(self, amount):
        self._balance += amount
    def get_balance(self):
        return self._balance
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())

