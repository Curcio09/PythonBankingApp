import tkinter as tk
import datetime
from database import update_account

def open_transaction_history(account, account_type, root):
    """Opens a transaction history window showing past transactions for a given account type."""
    history_window = tk.Toplevel(root)
    history_window.title(f"{account_type} Transaction History")
    history_window.geometry("500x400")
    history_window.configure(bg="#242f40")

    tk.Label(history_window, text=f"{account_type} Transactions", font=("Arial", 14, "bold"), bg="#242f40", fg="white").pack(pady=5)

    transaction_list = tk.Listbox(history_window, font=("Arial", 12), width=70, height=15)
    transaction_list.pack(pady=5)

    # Ensure transactions exist in account
    for transaction in account.get("transactions", []):
        if transaction["account"] == account_type:
            # Format transfer transactions to include recipient details
            if transaction["type"] == "Transfer Sent":
                recipient = transaction.get("recipient", "Unknown")  # Fixing recipient retrieval
                transaction_list.insert(
                    tk.END,
                    f"{transaction['date']} | {transaction['type']} | ${transaction['amount']:.2f} | To: {recipient}"
                )
            elif transaction["type"] == "Transfer Received":
                sender = transaction.get("sender", "Unknown")  # Fixing sender retrieval
                transaction_list.insert(
                    tk.END,
                    f"{transaction['date']} | {transaction['type']} | ${transaction['amount']:.2f} | From: {sender}"
                )
            else:
                # Regular deposit/withdraw transactions
                transaction_list.insert(
                    tk.END,
                    f"{transaction['date']} | {transaction['type']} | ${transaction['amount']:.2f}"
                )

def log_transaction(account, account_type, transaction_type, amount, recipient=None, sender=None):
    """Logs a transaction in the account's transaction history and saves it."""
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