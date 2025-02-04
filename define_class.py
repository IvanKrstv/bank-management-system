# 🏦 Data Structures to Store Information

class BankAccount:
    def __init__(self, name, balance, loan, transaction_history = None):
        self.account_holder = name # Account names
        self.balance = balance # Account balances
        self.loan = loan # Account loan details
        self.transaction_history = transaction_history if transaction_history is not None else [] # Account transaction logs
