import datetime
from database import get_account, update_account

def log_transaction(account, account_type, transaction_type, amount):
    """Logs a transaction in the account's transaction history and saves it."""
    if "transactions" not in account:  
        account["transactions"] = []  # Ensure transactions key exists

    transaction = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": transaction_type,
        "account": account_type,
        "amount": amount
    }
    
    account["transactions"].append(transaction)  # Add to history
    update_account(account)  # Save changes

def process_deposit(account, selected_account, amount):
    """Processes a deposit transaction and updates account balance."""
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        # Update balance
        if selected_account == "Checking":
            account["checking_balance"] += amount
        else:
            account["savings_balance"] += amount

        log_transaction(account, selected_account, "Deposit", amount)
        update_account(account)  # Save changes
        return True, None  # Success
    except ValueError as e:
        return False, str(e)  # Return error message

def process_withdraw(account, selected_account, amount):
    """Processes a withdrawal transaction and updates account balance."""
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        # Check for sufficient funds
        if selected_account == "Checking":
            if amount > account["checking_balance"]:
                raise ValueError("Insufficient funds.")
            account["checking_balance"] -= amount
        else:
            if amount > account["savings_balance"]:
                raise ValueError("Insufficient funds.")
            account["savings_balance"] -= amount

        log_transaction(account, selected_account, "Withdraw", amount)
        update_account(account)  # Save changes
        return True, None  # Success
    except ValueError as e:
        return False, str(e)  # Return error message

def process_transfer(sender_account, from_account, recipient_selection, account_mapping, amount):
    """Processes a transfer from one account to another."""
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        # Ensure sender has sufficient funds
        if from_account == "Checking":
            if amount > sender_account["checking_balance"]:
                raise ValueError("Insufficient funds.")
            sender_account["checking_balance"] -= amount
        else:
            if amount > sender_account["savings_balance"]:
                raise ValueError("Insufficient funds.")
            sender_account["savings_balance"] -= amount

        # Retrieve recipient's account
        if recipient_selection not in account_mapping:
            raise ValueError("Recipient account not found.")
        
        recipient_username, recipient_account_type = account_mapping[recipient_selection]
        recipient_account = get_account(recipient_username)

        if not recipient_account:
            raise ValueError("Recipient account not found.")

        # Update recipient balance
        if recipient_account_type == "Checking":
            recipient_account["checking_balance"] += amount
        else:
            recipient_account["savings_balance"] += amount

        # Log transactions for both sender and recipient
        log_transaction(sender_account, from_account, "Transfer Sent", amount)
        log_transaction(recipient_account, recipient_account_type, "Transfer Received", amount)

        # Save changes
        update_account(sender_account)
        update_account(recipient_account)
        return True, None  # Success
    except ValueError as e:
        return False, str(e)  # Return error message
