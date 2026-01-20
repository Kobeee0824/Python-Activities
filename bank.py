class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    def display_balance(self):
        print(f"Account Balance: ${self.balance:.2f}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        acc_no = input("Enter account number: ")
        name = input("Enter account holder name: ")
        self.accounts[acc_no] = BankAccount(acc_no, name)
        print("Account created successfully.")

    def get_account(self, acc_no):
        return self.accounts.get(acc_no)

    def transfer(self):
        from_acc = input("From account number: ")
        to_acc = input("To account number: ")
        amount = float(input("Amount to transfer: "))

        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)

        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print("Transfer successful.")
            else:
                print("Insufficient funds.")
        else:
            print("One or both accounts not found.")


def main():
    bank = Bank()

    while True:
        print("\n--- BANKING SYSTEM ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            bank.create_account()

        elif choice == "2":
            acc = input("Account number: ")
            amount = float(input("Amount: "))
            account = bank.get_account(acc)
            if account:
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            acc = input("Account number: ")
            amount = float(input("Amount: "))
            account = bank.get_account(acc)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            acc = input("Account number: ")
            account = bank.get_account(acc)
            if account:
                account.display_balance()
            else:
                print("Account not found.")

        elif choice == "5":
            bank.transfer()

        elif choice == "6":
            print("Thank you for using the banking system.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
