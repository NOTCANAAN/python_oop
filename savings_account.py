from account import Account


class SavingsAccount(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self.interest_rate = 0.02
        self.withdraw_limit = 100

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of {interest} applied.")
        print(f"New balance: {self.get_balance()}")

    # Overriding the withdraw method here
    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"Withdrawal cannot exceed ${self.withdraw_limit}")
        else:
            super().withdraw(amount)

print("--- Savings Account ---")

savings = SavingsAccount("Alice", 1000)

print(f"Initial balance: {savings.get_balance()}")

savings.deposit(500)
savings.withdraw(200)
savings.apply_interest()
