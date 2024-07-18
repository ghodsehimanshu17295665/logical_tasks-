#Create an abstract class Account with abstract methods deposit and withdraw. 
# Implement these methods in subclasses SavingsAccount and CurrentAccount.

from abc import ABC, abstractmethod


class Account(ABC):

    @abstractmethod
    def deposite(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(Account):
    def __init__(self, balance):
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
        else:
            print("Insufficient balance")


class CurrentAccount(Account):
    def __init__(self, balance):
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
        else:
            print("Insufficient balance")


savings = SavingsAccount(1000)
savings.deposite(500)
savings.withdraw(200)

curr = CurrentAccount(2000)
curr.deposite(1000)
curr.withdraw(500)