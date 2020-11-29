# This is a sample Python script.

#first example writing a bank account from object oriented programming
# reference: https://www.youtube.com/watch?v=4-NqE8ZA4vI

class BankAccount:
    def __init__(self):
        self.balance = 0

# this function takes the amount you deposit as an argument.
    def deposit(self, amount):
            self.balance = self.balance + amount
            return self.balance
        # this function takes the amount that you withdraw as an argument
    def withdraw(self, amount):
            if self.balance >= amount:
                self.balance -= amount
                self.balance = self.balance - amount
                return self.balance
            else:
                print("insufficient funds")

    def print_balance(self):
        print(self.balance)
        return self.balance


account = BankAccount ()
account.deposit(100)
account.deposit(100)
account.deposit(400)
print (account.print_balance())


# reference : https://www.youtube.com/watch?v=4-NqE8ZA4vI