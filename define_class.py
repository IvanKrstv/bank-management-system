# 🏦 Data Structures to Store Information

class BankAccount:
    def __init__(self, name):
        self.account_holder = name # Account name
        self.balance = 0 # Account balance
        self.loan = 0 # Account loan details
        self.transaction_history = [] # Account transaction logs

    def deposit(self):
        """Deposit money into an account."""

        deposit_money = float(input("\nHow much money would you like to deposit?"
                                    "\nMoney: "))
        self.balance += deposit_money
        self.transaction_history.append(f"Deposited: {deposit_money}")
        print(f"{deposit_money} dollars have been successfully deposited to your account! ✅")

    def withdraw(self):
        """Withdraw money from an account."""

        withdraw_money = float(input("\nHow much money would you like to withdraw?"
                                     "\nMoney: "))
        if withdraw_money <= self.balance:  # Checks if the sufficient balance exists for the withdrawal
            self.balance -= withdraw_money
            self.transaction_history.append(f"Withdrew: {withdraw_money}")
            print(f"{withdraw_money} dollars have been successfully withdrawn from your account! ✅")
        else:
            print("You don't have enough funds to withdraw this amount!")

    def check_balance(self):
        """Check balance of an account."""

        print(f"\nCurrent balance: {self.balance}")

    def view_transaction_history(self):
        """View transactions for an account."""

        print()
        if self.transaction_history:
            for index, transaction in enumerate(self.transaction_history):
                print(f"{index + 1}. {transaction}")
        else:
            print("There are not any transactions to be shown for this account!")

    def apply_for_loan(self, max_loan: int, interest_rate: float):
        """Allow user to apply for a loan."""

        requested_amount = float(input("Enter the requested amount of the loan: "))
        if requested_amount > max_loan:  # Check if the requested amount is more than the maximum
            print("Sorry, this amount is more than what the bank could offer."
                  f"You may only apply for up to {max_loan} dollars.")
        else:
            print(f"Your loan of {requested_amount} has been accepted and added successfully to your account. ✅")

            # Adding loan to the account
            total_loan = requested_amount * (1 + interest_rate)  # Calculating the interest rate
            self.balance += requested_amount  # Adding the money to the balance
            self.loan += total_loan  # Adding the money + the interest rate to the loan
            self.transaction_history.append(f"Loan applied:{requested_amount} dollars"
                                                            f"with interest {requested_amount * interest_rate}")  # Adding the loan transaction

    def repay_loan(self):
        """Allow user to repay a loan."""

        print(f"How much would you like to repay? (Current loans due: {self.loan} dollars)")
        repaid_loan = float(input("Repay: "))
        if self.balance < repaid_loan:
            print("Insufficient amount of money in your balance! The transaction haas been canceled!")
        else:
            print(f"{repaid_loan} dollars have been successfully repaid. Thank you!")

            # Removing the repaid loan from the account
            if self.loan <= 0:
                print("You have paid all your loans! ✅")
                self.balance -= repaid_loan - abs(self.loan)
                self.transaction_history.append(f"Loan repaid:{repaid_loan - abs(self.loan)}")
                self.loan = 0
            else:
                self.balance -= repaid_loan  # Reducing the money from the balance
                self.loan -= repaid_loan  # Also from the loan
                self.transaction_history.append(f"Loan repaid:{repaid_loan}")
