import random
from Bank import *

class User(Bank):
    def __init__(self):
        super().__init__()
        self.loans = {}

    def create_account(self, name, email, address, account_type, password):
        account_number = random.randint(10000, 99999)
        while account_number in self.users:
            account_number = random.randint(10000, 99999)

        self.users[account_number] = {
            'name': name,
            'email': email,
            'address': address,
            'account_type': account_type,
            'password': password,
            'balance': 0,
            'transactions': []
        }
        return account_number

    def deposit(self, account_number, amount):
        if account_number in self.users:
            self.users[account_number]['balance'] += amount
            self.users[account_number]['transactions'].append(f"Deposited {amount}")
            self.total_balance += amount
            return True
        return False

    def withdraw(self, account_number, amount):
        if account_number in self.users:
            if self.users[account_number]['balance'] >= amount:
                self.users[account_number]['balance'] -= amount
                self.users[account_number]['transactions'].append(f"Withdrew {amount}")
                self.total_balance -= amount
                return True
            else:
                return False
        return False

    def transfer(self, from_account, to_account, amount):
        if from_account in self.users and to_account in self.users:
            if self.users[from_account]['balance'] >= amount:
                self.users[from_account]['balance'] -= amount
                self.users[to_account]['balance'] += amount
                self.users[from_account]['transactions'].append(f"Transferred {amount} to {to_account}")
                self.users[to_account]['transactions'].append(f"Received {amount} from {from_account}")
                print("===========================")
                print(f"{amount}TK has been transferred to Account No: {to_account} ")
                print("===========================")
            else:
                print("===========================")
                print("Insufficient balance for transfer")
                print("===========================")
        else:
            print("===========================")
            print("Account does not exist")
            print("===========================")

    def check_balance(self, account_number):
        if account_number in self.users:
            return self.users[account_number]['balance']
        return None

    def get_transactions(self, account_number):
        if account_number in self.users:
            return self.users[account_number]['transactions']
        return None

    def take_loan(self, account_number, amount):
        if account_number in self.users:
            if len(self.loans.get(account_number, [])) < 2:
                if self.loan_feature_enabled:
                    self.users[account_number]['balance'] += amount
                    self.loans.setdefault(account_number, []).append(amount)
                    self.users[account_number]['transactions'].append(f"Took a loan of {amount}")
                    self.total_balance -= amount
                    print("===========================")
                    print(f"{amount}TK has been added as Loan")
                    print("===========================")
                else:
                    print("===========================")
                    print("Loan feature is currently disabled")
                    print("===========================")
            else:
                print("===========================")
                print("You can only take two loans at most")
                print("===========================")
        else:
            print("===========================")
            print("Invalid account number!!")
            print("===========================")

class Admin:
    def __init__(self, name, email, password):
        super().__init__()
        self.name = name
        self.email = email
        self.__password = password

    def admin_delete_account(self, bank_user, account_number):
        if account_number in bank_user.users:
            del bank_user.users[account_number]
            return True
        return False
    
    def admin_all_accounts(self, bank_users):
        return bank_users.users

    def admin_total_balance(self, total_balance):
        return total_balance.total_balance

    def admin_total_loan(self, bank_loan):
        total_loan = sum(sum(loans) for loans in bank_loan.loans.values())
        return total_loan

    def admin_toggle_loan_feature(self, toggle, status):
        toggle.loan_feature_enabled = status
