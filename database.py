import json
import os
import random
from datetime import datetime

# File where account data is stored
DATA_FILE = "accounts.json"


def load_accounts():
    """
    Loads account data from the JSON file.

    Returns:
        list: A list of account dictionaries.
    """
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []  # Return an empty list if no data exists


def save_accounts(accounts):
    """
    Saves account data to the JSON file.

    Args:
        accounts (list): List of account dictionaries to be saved.
    """
    with open(DATA_FILE, "w") as file:
        json.dump(accounts, file, indent=4)


def generate_random_account():
    """
    Generates a new random bank account with realistic data.

    Returns:
        dict: A dictionary containing account details.
    """
    return {
        "account_number": random.randint(1000000000, 9999999999),
        "routing_number": random.randint(100000000, 999999999),
        "checking_balance": round(random.uniform(500, 5000), 2),
        "savings_balance": round(random.uniform(1000, 10000), 2),
        "transactions": []
    }


def initialize_accounts():
    """
    Initializes account data if the file does not exist or is empty.

    Returns:
        list: The list of initialized accounts.
    """
    accounts = load_accounts()

    if not accounts:  # If no saved data exists, create new accounts
        accounts = [
            {
                "name": "Chris Curcio", "username": "curcio_admin", "password": "SecureBank123!",
                **generate_random_account()
            },
            {
                "name": "Richard Caldwell", "username": "richardC89", "password": "CNB$avings321",
                **generate_random_account()
            },
            {
                "name": "Sarah West", "username": "sarah_west", "password": "DepositNow789!",
                **generate_random_account()
            },
            {
                "name": "Mark Thompson", "username": "markT_CNB", "password": "TrustBank654@",
                **generate_random_account()
            }
        ]
        save_accounts(accounts)  # Save new accounts

    return accounts  # Return initialized or loaded accounts


def get_account(username):
    """
    Retrieves a specific account by username.

    Args:
        username (str): The username of the account to retrieve.

    Returns:
        dict | None: The account dictionary if found, else None.
    """
    return next((acc for acc in load_accounts() if acc["username"] == username), None)


def update_account(account):
    """
    Updates an existing account's details in the database.

    Args:
        account (dict): The updated account dictionary.

    Returns:
        bool: True if the account was updated, False if not found.
    """
    accounts = load_accounts()
    for i, acc in enumerate(accounts):
        if acc["username"] == account["username"]:
            accounts[i] = account  # Update account data
            save_accounts(accounts)  # Save updated accounts
            return True
    return False  # Account not found


def record_transaction(username, transaction_type, amount):
    """
    Records a transaction (deposit, withdrawal, transfer) for a given account.

    Args:
        username (str): The username of the account making the transaction.
        transaction_type (str): Type of transaction (Deposit, Withdraw, Transfer Sent, Transfer Received).
        amount (float): The amount involved in the transaction.

    Returns:
        bool: True if transaction was recorded, False if account was not found.
    """
    account = get_account(username)
    if account:
        transaction = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": transaction_type,
            "amount": amount
        }
        account["transactions"].append(transaction)  # Add transaction
        return update_account(account)  # Save updated data
    return False  # Account not found


# Initialize accounts if necessary
initialize_accounts()