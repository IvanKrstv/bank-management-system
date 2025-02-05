# Enhanced Bank Account Management System
from define_class import BankAccount
list_accounts = []

MAX_LOAN_AMOUNT = 10000
INTEREST_RATE = 0.03

def user_index(account):
    """
    Function for verification that checks if the target user exists
    :parameter: target account
    :return: index or None
    """

    found = False  # Flag for keeping track if the name exists in the list
    index = 0  # Will store at which index the person is found

    # Goes through the list of accounts to check if the target name is there
    for i in range(len(list_accounts)):
        if list_accounts[i].account_holder == account.strip():
            index = i
            found = True
            return index

    if not found:
        print(f"\nNo account with the name {account} has been found! ❌")
        return None

def display_menu():
    """Main menu for banking system."""

    print("\n🌟 Welcome to Enhanced Bank System 🌟")
    print("1️⃣ Create Account")
    print("2️⃣ Deposit Money")
    print("3️⃣ Withdraw Money")
    print("4️⃣ Check Balance")
    print("5️⃣ List All Accounts")
    print("6️⃣ Transfer Funds")
    print("7️⃣ View Transaction History")
    print("8️⃣ Apply for Loan")
    print("9️⃣ Repay Loan")
    print("🔟 Identify Credit Card Type")
    print("0️⃣ Exit")

def create_account():
    """Create a new account."""

    account_name = input("Enter your name: ")
    list_accounts.append(BankAccount(account_name, 0, 0)) # Appends the new account to the accounts list
    print("Account has been successfully created! ✅")

def deposit():
    """Deposit money into an account."""

    target_account = input("Enter the name of the account you would like to deposit money to: ")
    index = user_index(target_account) # Index of the target account

    if index is not None: # Allows the user to deposit money to the account
        deposit_money = input("\nHow much money would you like to deposit?"
                              "\nMoney: ")
        list_accounts[index].balance += deposit_money
        list_accounts[index].transaction_history.append(f"+{deposit_money}")
        print(f"{deposit_money} dollars have been successfully deposited to your account! ✅")

def withdraw():
    """Withdraw money from an account."""

    target_account = input("Enter the name of the account you would like to withdraw money from: ")
    index = user_index(target_account) # Index of the target account

    if index is not None: # Allows the user to withdraw money from the account
        withdraw_money = input("\nHow much money would you like to withdraw?"
                              "\nMoney: ")
        if withdraw_money <= list_accounts[index].balance: # Checks if the sufficient balance exists for the withdrawal
            list_accounts[index].balance -= withdraw_money
            list_accounts[index].transaction_history.append(f"-{withdraw_money}")
            print(f"{withdraw_money} dollars have been successfully withdrawn from your account! ✅")
        else:
            print("You don't have enough funds to withdraw this amount!")

def check_balance():
    """Check balance of an account."""

    target_account = input("Enter the name of the account you would like to check the balance of: ")
    index = user_index(target_account)

    if index is not None: # Prints the current balance
        print(f"\nCurrent balance: {list_accounts[index].balance}")

def display_accounts():
    """List all account holders and details."""

    if not list_accounts: # Check if there are created accounts
        print("No accounts to display!")
        return

    # Display the information for each account
    for i in range(len(list_accounts)):
        print(f"\nAccount number {i + 1}:"
              f"\nName: {list_accounts[i].account_holder}"
              f"\nBalance: {list_accounts[i].balance}"
              f"\nLoan details: {list_accounts[i].loan}")

def transfer_funds():
    """Transfer funds between two accounts."""

    sender = input("Enter the name of the sender account: ")
    index_sender = user_index(sender)
    receiver = input("Enter the name of the receiver account: ")
    index_receiver = user_index(receiver)

    if index_sender is not None and index_receiver is not None: # Check if the names exist
        transfer_money = input(f"\nHow much money would you like to transfer to {list_accounts[index_receiver].name}?"
                              "\nMoney: ")

        if list_accounts[index_sender].balance < transfer_money: # Check if there is enough money in the sender balance
            print(f"Insufficient funds in {list_accounts[index_sender].name}'s account.")
        else:
            # Get the money from the sender and add the transaction
            list_accounts[index_sender].balance -= transfer_money
            list_accounts[index_sender].transaction_history.append(f"-{transfer_money}")

            # Receive the money and add the transaction
            list_accounts[index_receiver].receiver += transfer_money
            list_accounts[index_receiver].transaction_history.append(f"+{transfer_money}")

            print("The transaction has been successful! ✅")

def view_transaction_history():
    """View transactions for an account."""

    target_account = input("Enter the name of the account whose transaction history you would like to view: ")
    index = user_index(target_account)

    if index is not None:
        counter = 1
        print()
        for transaction in list_accounts[index].transaction_history:
            print(f"{counter}. {transaction} dollars")
            counter += 1

def apply_for_loan():
    """Allow user to apply for a loan."""
    pass

def repay_loan():
    """Allow user to repay a loan."""
    pass

def identify_card_type():
    """Identify type of credit card."""
    pass

def main():
    """Run the banking system."""
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        # Map choices to functions
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            display_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            identify_card_type()
        elif choice == 0:
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()