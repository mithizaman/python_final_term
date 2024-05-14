
from bank import Bank
from admin import Admin

if __name__ == "__main__":
    bank = Bank()
    admin = Admin(bank)

    while True:
        print("\nWelcome to Banking Management System")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. View All Accounts")
        print("4. Check Total Balance")
        print("5. Check Total Loan Amount")
        print("6. Loan Status Feature")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current): ")
            account_number = bank.create_account(name, email, address, account_type)
            print(f"Account created successfully! Account number: {account_number}")
        
        elif choice == '2':
            account_number = int(input("Enter account number to delete: "))
            bank.delete_account(account_number)
        
        elif choice == '3':
            accounts = bank.get_all_accounts()
            print("All Accounts:")
            for account_number, details in accounts.items():
                print(f"Account Number: {account_number}, Details: {details}")

        elif choice == '4':
            total_balance = bank.get_total_balance()
            print(f"Total Balance: ${total_balance}")

        elif choice == '5':
            total_loan_amount = bank.get_total_loan_amount()
            print(f"Total Loan Amount: ${total_loan_amount}")

        elif choice == '6':
            bank.loan_status_feature()

        elif choice == '7':
            break
