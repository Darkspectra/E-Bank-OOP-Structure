from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self):
        self.users = {}
        self.total_balance = 10000000000
        self.loan_feature_enabled = True
        
    @abstractmethod
    def create_account(self, name, email, address, account_type):
        pass

    @abstractmethod
    def deposit(self, account_number, amount):
        pass

    @abstractmethod
    def withdraw(self, account_number, amount):
        pass

    @abstractmethod
    def transfer(self, from_account, to_account, amount):
        pass

    @abstractmethod
    def check_balance(self, account_number):
        pass

    @abstractmethod
    def get_transactions(self, account_number):
        pass

    @abstractmethod
    def take_loan(self, account_number, amount):
        pass