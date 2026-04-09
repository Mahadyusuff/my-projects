class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def info(self):
        print(f"{self.name} has {self.balance} dollars")


susan_account = BankAccount("Susan", 100)
susan_account.deposit(200)
susan_account.info()
susan_account.withdraw(250)
susan_account.info()

bill_account = BankAccount("Bill", 200)
bill_account.withdraw(120)
bill_account.info()
bill_account.deposit(50)
bill_account.info()
bill_account.withdraw(180)


class PlatinumAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount + 1


ron_account = PlatinumAccount("Ron", 100)
ron_account.deposit(50)
ron_account.info()
ron_account.deposit(50)
ron_account.info()
ron_account.withdraw(50)
ron_account.info()

kyle_account = PlatinumAccount("Kyle", 100)
for _ in range(50):
    kyle_account.deposit(1)
kyle_account.info()
