from tkinter import Toplevel, Label, Listbox, END
import datetime
from database import update_account

def open_transaction_history(account, account_type, root):
    """
    Opens a window displaying the transaction history for a given account type.

    - Retrieves and formats past transactions.
    - Displays deposits, withdrawals, and transfers.
    - Ensures correct recipient/sender details for transfers.

    Args:
        account (dict): The currently logged-in user's account details.
        account_type (str): The type of account ("Checking" or "Savings").
        root (tk.Tk): The main application window.
    """

    # --- Create Transaction History Window ---
    history_window = Toplevel(root)
    history_window.title(f"{account_type} Transaction History")
    history_window.geometry("500x400")
    history_window.configure(bg="#242f40")

    # --- Header Label ---
    Label(history_window, text=f"{account_type} Transactions", font=("Arial", 14, "bold"),
          bg="#242f40", fg="white").pack(pady=5)

    # --- Transaction List Box ---
    transaction_list = Listbox(history_window, font=("Arial", 12), width=70, height=15)
    transaction_list.pack(pady=5)

    # --- Populate Transaction History ---
    for transaction in account.get("transactions", []):
        if transaction["account"] == account_type:
            transaction_type = transaction["type"]
            amount = transaction["amount"]
            date = transaction["date"]

            # --- Format Transfer Transactions ---
            if transaction_type == "Transfer Sent":
                recipient = transaction.get("recipient", "Unknown")  
                transaction_list.insert(
                    END, f"{date} | {transaction_type} | ${amount:.2f} | To: {recipient}"
                )
            elif transaction_type == "Transfer Received":
                sender = transaction.get("sender", "Unknown")  
                transaction_list.insert(
                    END, f"{date} | {transaction_type} | ${amount:.2f} | From: {sender}"
                )
            else:
                # --- Format Regular Transactions (Deposit/Withdraw) ---
                transaction_list.insert(
                    END, f"{date} | {transaction_type} | ${amount:.2f}"
                )

def log_transaction(account, account_type, transaction_type, amount, recipient=None, sender=None):
    """
    Logs a transaction in the account's transaction history and saves it.

    - Handles deposits, withdrawals, and transfers.
    - Ensures correct recipient/sender details for transfers.

    Args:
        account (dict): The account where the transaction is recorded.
        account_type (str): The type of account ("Checking" or "Savings").
        transaction_type (str): The type of transaction ("Deposit", "Withdraw", "Transfer Sent", "Transfer Received").
        amount (float): The transaction amount.
        recipient (str, optional): The recipient's full name for transfers.
        sender (str, optional): The sender's full name for transfers.
    """

    # Ensure the account has a transaction history list
    if "transactions" not in account:  
        account["transactions"] = []  

    # --- Create Transaction Record ---
    transaction = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": transaction_type,
        "account": account_type,
        "amount": amount
    }

    # --- Include Transfer Details (Recipient/Sender) ---
    if recipient:
        transaction["recipient"] = recipient
    if sender:
        transaction["sender"] = sender

    # --- Save Transaction & Update Database ---
    account["transactions"].append(transaction)  
    update_account(account)  