# Enhanced Bank Account Management System
from define_class import BankAccount
from os import system
list_accounts = [] # Initialize list for all the accounts

MAX_LOAN_AMOUNT = 10000
INTEREST_RATE = 0.03

def user_index(account) -> int or None:
    """
    Function for verification that checks if the target user exists
    :parameter: target account
    :return: index or None
    """

    # Goes through the list of accounts to check if the target name is there
    for index, acc in enumerate(list_accounts):
        if acc.account_holder == account.strip():
            return index

    print(f"\nNo account with the name {account} has been found! ❌")
    return None

def clear_screen():
    print()
    system("pause")
    system("cls")

def display_menu() -> None:
    """Main menu for banking system."""

    print("🌟 Welcome to Enhanced Bank System 🌟")
    print("\n1️⃣ Create Account")
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

def create_account() -> None:
    """Create a new account."""

    account_name = input("Enter your name: ")
    list_accounts.append(BankAccount(account_name)) # Appends the new account to the accounts list
    print("Account has been successfully created! ✅")

def display_accounts() -> None:
    """List all account holders and details."""

    # Display the information for each account
    for i in range(len(list_accounts)):
        print(f"\nAccount number {i + 1}:"
              f"\nName: {list_accounts[i].account_holder}"
              f"\nBalance: {list_accounts[i].balance}"
              f"\nLoan details: {list_accounts[i].loan}")

def transfer_funds(sender: str, receiver: str, index_sender: int, index_receiver: int) -> None:
    """Transfer funds between two accounts."""

    transfer_money = float(input(f"\nHow much money would you like to transfer to {list_accounts[index_receiver].name}?"
                          "\nMoney: "))

    if list_accounts[index_sender].balance < transfer_money: # Check if there is enough money in the sender balance
        print(f"Insufficient funds in {list_accounts[index_sender].name}'s account.")
    else:
        # Get the money from the sender and add the transaction
        list_accounts[index_sender].balance -= transfer_money
        list_accounts[index_sender].transaction_history.append(f"Sent {transfer_money} dollars to {receiver}.")

        # Receive the money and add the transaction
        list_accounts[index_receiver].receiver += transfer_money
        list_accounts[index_receiver].transaction_history.append(f"Received {transfer_money} dollars from {sender}.")

        print("The transaction has been successful! ✅")

def identify_card_type() -> str or -1:
    """Identify type of credit card."""

    user_card = input("Enter your card number: ")
    if len(user_card) < 15 or len(user_card) > 16: # Check if the length of the card is real
        return -1

    # Find the type of the card, based on the prefixes
    if user_card[0] == '4':
        card_type = "Visa"
    elif 51 <= int(user_card[:2]) <= 55:
        card_type = "MasterCard"
    elif 34 <= int(user_card[:2]) <= 37:
        card_type = "American Express"
    else:
        card_type = "Other"

    return card_type

def main():
    """Run the banking system."""

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        # Map choices to functions
        if choice == '1':
            create_account()

        elif choice == '2':
            if list_accounts:
                target_account = input("Enter the name of the account you would like to deposit money to: ")
                index = user_index(target_account)  # Index of the target account

                if index is not None: # Allows the user to deposit money to the account
                    account = list_accounts[index]
                    account.deposit()

            else:
                print("There are no created accounts!")

        elif choice == '3':
            if list_accounts:
                target_account = input("Enter the name of the account you would like to withdraw money from: ")
                index = user_index(target_account)  # Index of the target account

                if index is not None:  # Allows the user to withdraw money from the account
                    account = list_accounts[index]
                    account.withdraw(list_accounts)

            else:
                print("There are no created accounts!")

        elif choice == '4':
            if list_accounts:
                target_account = input("Enter the name of the account you would like to check the balance of: ")
                index = user_index(target_account)

                if index is not None:  # Prints the current balance
                    account = list_accounts[index]
                    account.check_balance(list_accounts)

            else:
                print("There are no created accounts!")

        elif choice == '5':
            if list_accounts:
                display_accounts()
            else:
                print("There are no created accounts!")

        elif choice == '6':
            if list_accounts:
                send = input("Enter the name of the sender account: ")
                index_send = user_index(send)
                receive = input("Enter the name of the receiver account: ")
                index_receive = user_index(receive)

                if index_send is not None and index_receive is not None:  # Check if the names exist
                    transfer_funds(send, receive, index_send, index_receive)
            else:
                print("There are no created accounts!")

        elif choice == '7':
            if list_accounts:
                target_account = input("Enter the name of the account whose transaction history you would like to view: ")
                index = user_index(target_account)

                if index is not None:
                    account = list_accounts[index]
                    account.transaction_history()

            else:
                print("There are no created accounts!")

        elif choice == '8':
            if list_accounts:
                target_account = input("Enter the name of the account you would like to apply for loan from: ")
                index = user_index(target_account)

                if index is not None:
                    account = list_accounts[index]
                    account.apply_for_loan(MAX_LOAN_AMOUNT, INTEREST_RATE)

            else:
                print("There are no created accounts!")

        elif choice == '9':
            if list_accounts:
                target_account = input("Enter the name of the account you would like to apply for loan from: ")
                index = user_index(target_account)

                if index is not None:
                    account = list_accounts[index]
                    account.repay_loan()

            else:
                print("There are no created accounts!")

        elif choice == '10':
            if identify_card_type() == -1:
                print("Invalid card number!")
            else:
                print(f"Your card is: {identify_card_type()}")

        elif choice == '0':
            print("Goodbye! 👋")
            break

        else:
            print("❌ Invalid choice. Try again!")

        clear_screen() # Clearing the screen for every iteration

if __name__ == "__main__":
    main()