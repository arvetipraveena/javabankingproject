class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0.0
        self.transactions = ["Account created with balance ₹0.0"]

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}, Current Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew ₹{amount}, Current Balance: ₹{self.balance}")
            return True
        else:
            self.transactions.append(f"Failed withdrawal attempt of ₹{amount} (Insufficient Funds)")
            return False

    def receive_transfer(self, from_user, amount):
        self.balance += amount
        self.transactions.append(f"Received ₹{amount} from {from_user}, Current Balance: ₹{self.balance}")

    def send_transfer(self, to_user, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Sent ₹{amount} to {to_user.username}, Current Balance: ₹{self.balance}")
            to_user.receive_transfer(self.username, amount)
            return True
        else:
            self.transactions.append(f"Failed transfer of ₹{amount} to {to_user.username} (Insufficient Funds)")
            return False

    def print_transactions(self):
        print(f"Transaction History for {self.username}:")
        for t in self.transactions:
            print("- " + t)


users = {}

def sign_up():
    username = input("Choose a username: ")
    if username in users:
        print("Username already exists. Try login.")
        return

    password = input("Choose a password: ")
    users[username] = User(username, password)
    print("Signup successful! You can now log in.")


def login():
    username = input("Enter username: ")
    if username not in users:
        print("User doesn't exist. Please sign up first.")
        return

    password = input("Enter password: ")
    user = users[username]

    if user.password != password:
        print("Incorrect password!")
        return

    print(f"Login successful! Welcome {username}")
    user_dashboard(user)


def user_dashboard(current_user):
    while True:
        print("\n-- Menu --")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transactions")
        print("5. Transfer Money")
        print("6. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Current Balance: ₹{current_user.balance}")
        elif choice == "2":
            amount = float(input("Enter deposit amount: ₹"))
            current_user.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter withdraw amount: ₹"))
            if not current_user.withdraw(amount):
                print("Insufficient balance!")
        elif choice == "4":
            current_user.print_transactions()
        elif choice == "5":
            to_username = input("Enter recipient username: ")
            if to_username not in users:
                print("Recipient not found!")
                continue
            if to_username == current_user.username:
                print("You can't send money to yourself.")
                continue
            amount = float(input("Enter amount to transfer: ₹"))
            if current_user.send_transfer(users[to_username], amount):
                print("Transfer successful.")
            else:
                print("Transfer failed due to insufficient funds.")
        elif choice == "6":
            print("Logged out.")
            break
        else:
            print("Invalid option!")


def main():
    print("=== Welcome to CLI Bank System ===")
    while True:
        print("\n1. Login\n2. Sign Up\n3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            login()
        elif choice == "2":
            sign_up()
        elif choice == "3":
            print("Thank you for using CLI Bank!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
