class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(self.filepath, "r") as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, "w") as file:
            file.write(str(self.balance))


account = Account("balance.txt")
print(account.balance)
account.withdraw(200)
print(account.balance)
account.deposit(300)
print(account.balance)
account.commit()
