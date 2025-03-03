import json
import os
import random

# File where account data is stored
DATA_FILE = "accounts.json"

# Function to Load Account Data from JSON
def load_accounts():
    """Loads account data from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []  # Return an empty list if no data exists

# Function to Save Account Data to JSON
def save_accounts(accounts):
    """Saves account data to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(accounts, file, indent=4)

# Function to Generate Account Data if Not Already Stored
def initialize_accounts():
    """Initializes account data if the file does not exist."""
    accounts = load_accounts()
    if not accounts:  # If no saved data exists, create new accounts
        accounts = [
            {
                "name": "Chris Curcio", "username": "curcio_admin", "password": "SecureBank123!",
                "account_number": random.randint(1000000000, 9999999999),
                "routing_number": random.randint(100000000, 999999999),
                "checking_balance": round(random.uniform(500, 5000), 2),
                "savings_balance": round(random.uniform(1000, 10000), 2),
                "transactions": []
            },
            {
                "name": "Richard Caldwell", "username": "richardC89", "password": "CNB$avings321",
                "account_number": random.randint(1000000000, 9999999999),
                "routing_number": random.randint(100000000, 999999999),
                "checking_balance": round(random.uniform(500, 5000), 2),
                "savings_balance": round(random.uniform(1000, 10000), 2),
                "transactions": []
            },
            {
                "name": "Sarah West", "username": "sarah_west", "password": "DepositNow789!",
                "account_number": random.randint(1000000000, 9999999999),
                "routing_number": random.randint(100000000, 999999999),
                "checking_balance": round(random.uniform(500, 5000), 2),
                "savings_balance": round(random.uniform(1000, 10000), 2),
                "transactions": []
            },
            {
                "name": "Mark Thompson", "username": "markT_CNB", "password": "TrustBank654@",
                "account_number": random.randint(1000000000, 9999999999),
                "routing_number": random.randint(100000000, 999999999),
                "checking_balance": round(random.uniform(500, 5000), 2),
                "savings_balance": round(random.uniform(1000, 10000), 2),
                "transactions": []
            }
        ]
        save_accounts(accounts)  # Save accounts to JSON for future use
    return accounts  # Return the list of accounts

# Function to Get a Specific Account by Username
def get_account(username):
    """Retrieves a specific account by username."""
    accounts = load_accounts()
    for account in accounts:
        if account["username"] == username:
            return account
    return None  # Return None if account is not found

# Function to Update Account Data
def update_account(account):
    """Updates an existing account's details and saves it back to the database."""
    accounts = load_accounts()
    for i, acc in enumerate(accounts):
        if acc["username"] == account["username"]:
            accounts[i] = account  # Update the account data
            save_accounts(accounts)  # Save the updated accounts
            return True
    return False  # Account not found

# Function to Record Transactions
def record_transaction(username, transaction_type, amount):
    """Records a transaction (deposit, withdrawal) for a given account."""
    account = get_account(username)
    if account:
        transaction = {"type": transaction_type, "amount": amount}
        account["transactions"].append(transaction)
        return update_account(account)  # Save updated data
    return False  # Account not found

# Initialize accounts if necessary
initialize_accounts()