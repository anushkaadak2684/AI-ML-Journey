class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        print(f"Total balance after deposit: {self.balance + amount}")

    def withdraw(self, amount):
            print(f"Total balance after withdraw: {self.balance - amount}")

    def check_balance(self):
            print(f"Total balance: {self.balance}")


c1 = BankAccount(123456, "Anushka Adak", 10000000)
c1.deposit(100000)
c1.withdraw(200000)
c1.check_balance()