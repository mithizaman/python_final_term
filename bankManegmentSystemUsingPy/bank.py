import random

class Bank:
    def __init__(self):
        self.users = {}
        self.total_balance = 0
        self.total_loan_amount = 0
        self.status_feature = False  

    def generate_account_number(self):
        return random.randint(100000, 999999)

    def create_account(self, name, email, address, account_type):
        account_number = self.generate_account_number()
        self.users[account_number] = {
            'name': name,
            'email': email,
            'address': address,
            'account_type': account_type,
            'balance': 0,
            'transaction_history': [],
            'loan_taken': False
        }
        return account_number

    def delete_account(self, account_number):
        if account_number in self.users:
            del self.users[account_number]
            print("Account deleted successfully!")
        else:
            print("Account does not exist.")

    def get_all_accounts(self):
        return self.users

    def get_total_balance(self):
        return self.total_balance

    def get_total_loan_amount(self):
        return self.total_loan_amount

    def loan_status_feature(self):
        self.status_feature = not self.status_feature
        if self.status_feature:
            print("OFF")
        else:
            print("ON")

    def deposit(self, account_number, amount):
        if amount > 0:
            self.users[account_number]['balance'] += amount
            self.total_balance += amount
            self.users[account_number]['transaction_history'].append(f"Deposited: ${amount}")
            print("Deposit successful!")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, account_number, amount):
        if amount <= self.users[account_number]['balance']:
            self.users[account_number]['balance'] -= amount
            self.total_balance -= amount
            self.users[account_number]['transaction_history'].append(f"Withdrew: ${amount}")
            print("Withdrawal successful!")
        else:
            print("Withdrawal amount exceeded.")

    def check_balance(self, account_number):
        return self.users[account_number]['balance']

    def check_transaction_history(self, account_number):
        return self.users[account_number]['transaction_history']

    def take_loan(self, account_number, loan_amount):
        if not self.users[account_number]['loan_taken']:
            self.users[account_number]['balance'] += loan_amount
            self.total_balance += loan_amount
            self.users[account_number]['loan_taken'] = True
            self.total_loan_amount += loan_amount
            self.users[account_number]['transaction_history'].append(f"Loan taken: ${loan_amount}")
            print("Loan taken successfully!")
        elif self.users[account_number]['loan_taken']:
            print("You have already taken a loan.")

    def transfer(self, sender_account, receiver_account, amount):
        if sender_account not in self.users or receiver_account not in self.users:
            print("Account does not exist.")
            return
        if amount <= self.users[sender_account]['balance']:
            self.users[sender_account]['balance'] -= amount
            self.users[receiver_account]['balance'] += amount
            self.users[sender_account]['transaction_history'].append(f"Transferred: ${amount} to {receiver_account}")
            self.users[receiver_account]['transaction_history'].append(f"Received: ${amount} from {sender_account}")
            print("Transfer successful!")
        else:
            print("Insufficient balance for transfer.")

