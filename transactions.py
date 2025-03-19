import datetime
from database import get_account, update_account

def log_transaction(account, account_type, transaction_type, amount, recipient=None, sender=None):
    """
    Logs a transaction in the account's transaction history and updates the database.

    Args:
        account (dict): The account performing the transaction.
        account_type (str): Type of account ("Checking" or "Savings").
        transaction_type (str): Type of transaction ("Deposit", "Withdraw", "Transfer Sent", "Transfer Received").
        amount (float): The amount of money involved in the transaction.
        recipient (str, optional): Full name of the recipient for transfers.
        sender (str, optional): Full name of the sender for transfers.
    """
    if "transactions" not in account:
        account["transactions"] = []  # Ensure transactions key exists

    transaction = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": transaction_type,
        "account": account_type,
        "amount": amount
    }

    # Add recipient/sender details for transfers
    if recipient:
        transaction["recipient"] = recipient
    if sender:
        transaction["sender"] = sender

    account["transactions"].append(transaction)  # Add to history
    update_account(account)  # Save changes


def process_deposit(account, selected_account, amount):
    """
    Processes a deposit transaction.

    Args:
        account (dict): The account performing the deposit.
        selected_account (str): Type of account ("Checking" or "Savings").
        amount (str): The amount being deposited.

    Returns:
        tuple: (bool success, str error_message)
    """
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        # Update the selected account balance
        account[f"{selected_account.lower()}_balance"] += amount

        log_transaction(account, selected_account, "Deposit", amount)
        update_account(account)  # Save changes
        return True, None  # Success
    except ValueError as e:
        return False, str(e)  # Return error message


def process_withdraw(account, selected_account, amount):
    """
    Processes a withdrawal transaction.

    Args:
        account (dict): The account performing the withdrawal.
        selected_account (str): Type of account ("Checking" or "Savings").
        amount (str): The amount being withdrawn.

    Returns:
        tuple: (bool success, str error_message)
    """
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        # Check for sufficient funds
        balance_key = f"{selected_account.lower()}_balance"
        if amount > account[balance_key]:
            raise ValueError("Insufficient funds.")

        account[balance_key] -= amount  # Deduct from balance

        log_transaction(account, selected_account, "Withdraw", amount)
        update_account(account)  # Save changes
        return True, None  # Success
    except ValueError as e:
        return False, str(e)  # Return error message


def process_transfer(sender_account, from_account, recipient_selection, account_mapping, amount):
    """
    Processes a transfer from one account to another.

    Args:
        sender_account (dict): The account sending funds.
        from_account (str): Type of sender's account ("Checking" or "Savings").
        recipient_selection (str): The recipient's name and account type.
        account_mapping (dict): Maps recipient selection to (username, account_type).
        amount (str): The amount being transferred.

    Returns:
        tuple: (bool success, str error_message)
    """
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        # Ensure sender has sufficient funds
        sender_balance_key = f"{from_account.lower()}_balance"
        if amount > sender_account[sender_balance_key]:
            raise ValueError("Insufficient funds.")

        # Validate recipient selection
        if recipient_selection not in account_mapping:
            raise ValueError("Recipient account not found.")

        # Retrieve recipient details
        recipient_username, recipient_account_type = account_mapping[recipient_selection]
        recipient_account = get_account(recipient_username)
        if not recipient_account:
            raise ValueError("Recipient account not found.")

        # Retrieve recipient's full name
        recipient_full_name = recipient_account["name"]

        # Perform transaction
        sender_account[sender_balance_key] -= amount
        recipient_balance_key = f"{recipient_account_type.lower()}_balance"
        recipient_account[recipient_balance_key] += amount

        # Log transactions for both sender and recipient
        log_transaction(sender_account, from_account, "Transfer Sent", amount, recipient=recipient_full_name)
        log_transaction(recipient_account, recipient_account_type, "Transfer Received", amount, sender=sender_account["name"])

        # Save changes
        update_account(sender_account)
        update_account(recipient_account)

        return True, None  # Success
    except ValueError as e:
        return False, str(e)  # Return error message