from Actors import *

print("-----Welcome E-Bank-----")

bank = User()

while True:
    print("1. User")
    print("2. Admin")
    print("3. Exit")

    n = int(input("Enter Option: "))

    if n == 1:
        current_account_number = None

        while True:
            print("\n1. Create Account")
            print("2. Login")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Check Balance")
            print("6. Transaction History")
            print("7. Take Loan")
            print("8. Transfer Balance")
            print("9. Logout")

            choice = int(input("Enter Option: "))

            if choice == 1:
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                address = input("Enter your address: ")
                password = int(input("Enter your password: "))

                print("Choose your account type: ")
                print("1. Savings")
                print("2. Current")

                ac_type = int(input("Choose option: "))
                account_type = "Savings" if ac_type == 1 else "Current"

                current_account_number = bank.create_account(name, email, address, account_type, password)
                print("Your Account has been created with account number:", current_account_number)
                print("===============================")

            elif choice == 2:
                account_number = int(input("Enter your account number: "))
                password = int(input("Enter your password: "))

                if account_number in bank.users and bank.users[account_number]['password'] == password:
                    current_account_number = account_number
                    print("===========================")
                    print("Login Successful!")
                    print("===========================")
                else:
                    print("===========================")
                    print("Invalid account number or password!")
                    print("===========================")

            elif choice == 3:
                if current_account_number:
                    amount = float(input("Enter the amount to deposit: "))
                    if bank.deposit(current_account_number, amount):
                        print("===========================")
                        print("Deposit successful!")
                        print("===========================")
                    else:
                        print("===========================")
                        print("Deposit failed!")
                        print("===========================")
                else:
                    print("===========================")
                    print("Please login first!")
                    print("===========================")

            elif choice == 4:
                if current_account_number:
                    amount = float(input("Enter the amount to withdraw: "))
                    if bank.withdraw(current_account_number, amount):
                        print("===========================")
                        print("Withdrawal successful!")
                        print("===========================")
                    else:
                        print("===========================")
                        print("Withdrawal amount exceeded!")
                        print("===========================")
                else:
                    print("===========================")
                    print("Please login first!")
                    print("===========================")

            elif choice == 5:
                if current_account_number:
                    balance = bank.check_balance(current_account_number)
                    if balance is not None:
                        print("===========================")
                        print("Your account balance:", balance)
                        print("===========================")
                    else:
                        print("===========================")
                        print("Failed to retrieve balance!")
                        print("===========================")
                else:
                    print("===========================")
                    print("Please login first!")
                    print("===========================")

            elif choice == 6:
                if current_account_number:
                    transaction = bank.get_transactions(current_account_number)
                    if transaction is not None:
                        print("===========================")
                        print("Your transaction history: ", transaction)
                        print("===========================")
                    else:
                        print("===========================")
                        print("Failed to retrieve transaction history!")
                        print("===========================")
                else:
                    print("===========================")
                    print("Please login first!")
                    print("===========================")

            elif choice == 7:
                amount = int(input("Enter Amount: "))
                bank.take_loan(current_account_number, amount)

            elif choice == 8:
                transfer_amount = int(input("Enter Amount: "))
                ac2_number = int(input("Enter Account Number to transfer TK: "))
                bank.transfer(current_account_number, ac2_number, transfer_amount)
                
            elif choice == 9:
                print("===========================")
                print("Logged out successfully!")
                print("===========================")
                break

    elif n == 2:
        ad_name = input("Input your name: ")
        ad_mail = input("Enter your mail: ")
        ad_pass = int(input("Enter your password: "))
        admin = Admin(ad_name, ad_mail, ad_pass)
        print("===========================")
        print("Admin created successfully!")
        print("===========================")
        while True:
            print("1. Toggle Loan Feature")
            print("2. View Total Loan Amount")
            print("3. Total Bank Balance")
            print("4. View all users")
            print("5. Delete user account")
            print("6. Exit")

            choice = int(input("Enter Option: "))

            if choice == 1:
                status = input("Enter 'ON' to enable or 'OFF' to disable loan feature: ").lower()
                if status == 'on':
                    admin.admin_toggle_loan_feature(bank, True)
                    print("===========================")
                    print("Loan feature ON!")
                    print("===========================")
                elif status == 'off':
                    admin.admin_toggle_loan_feature(bank, False)
                    print("===========================")
                    print("Loan feature OFF!")
                    print("===========================")
                else:
                    print("===========================")
                    print("Invalid input! Please enter 'ON' or 'OFF'.")
                    print("===========================")

            elif choice == 2:
                print("Total Loan Ammount: ")
                print("===========================")
                print(admin.admin_total_loan(bank))
                
            elif choice == 3:
                print("Total Bank Balance: ")
                print("===========================")
                print(admin.admin_total_balance(bank))
            
            elif choice == 4:
                print("Users Info: ")
                print("===========================")
                print(admin.admin_all_accounts(bank))
                
            elif choice == 5:
                ac = int(input("Account Number: "))
                temp = admin.admin_delete_account(bank, ac)
                if temp:
                    print("===========================")
                    print("Account has been deleted!")
                    print("===========================")
                else:
                    print("===========================")
                    print("Invalid Account number!")
                    print("===========================")
                
            elif choice == 6:
                print("Exiting Admin Panel...")
                break
    
    elif n == 3:
        print("===========================")
        print("Thank you for visiting E-Bank")
        print("===========================")
        break

    else:
        print("===========================")
        print("Invalid option! Please choose either '1' for User or '2' for Admin.")
        print("===========================")
        break
