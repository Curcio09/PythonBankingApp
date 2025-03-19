from tkinter import Toplevel, Label, Entry, Button, Frame, OptionMenu, StringVar, END
import tkinter as tk 
from transactions import process_deposit, process_withdraw, process_transfer
from database import load_accounts, get_account, update_account

def open_deposit_window(account, root):
    """
    Opens a deposit window where users can deposit funds into their account.

    Args:
        account (dict): The logged-in user's account data.
        root (tk.Tk): The main application window.
    """
    transaction_window = Toplevel(root)
    transaction_window.title("Deposit Funds")
    transaction_window.geometry("350x250")
    transaction_window.configure(bg="#242f40")

    Label(transaction_window, text="Select Account:", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    account_var = StringVar(transaction_window)
    account_var.set("Checking")  
    OptionMenu(transaction_window, account_var, "Checking", "Savings").pack(pady=5)

    Label(transaction_window, text="Enter Amount ($):", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    amount_entry = Entry(transaction_window, font=("Arial", 12), width=15)
    amount_entry.pack(pady=5)

    _add_confirm_cancel_buttons(transaction_window, account, root, account_var, amount_entry, "Deposit")


def open_withdraw_window(account, root):
    """
    Opens a withdrawal window where users can withdraw funds.

    Args:
        account (dict): The logged-in user's account data.
        root (tk.Tk): The main application window.
    """
    transaction_window = Toplevel(root)
    transaction_window.title("Withdraw Funds")
    transaction_window.geometry("350x250")
    transaction_window.configure(bg="#242f40")

    Label(transaction_window, text="Select Account:", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    account_var = StringVar(transaction_window)
    account_var.set("Checking")  
    OptionMenu(transaction_window, account_var, "Checking", "Savings").pack(pady=5)

    Label(transaction_window, text="Enter Amount ($):", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    amount_entry = Entry(transaction_window, font=("Arial", 12), width=15)
    amount_entry.pack(pady=5)

    _add_confirm_cancel_buttons(transaction_window, account, root, account_var, amount_entry, "Withdraw")


def open_transfer_window(account, root):
    """
    Opens a transfer window where users can transfer funds to other accounts.

    Args:
        account (dict): The logged-in user's account data.
        root (tk.Tk): The main application window.
    """
    transaction_window = Toplevel(root)
    transaction_window.title("Transfer Funds")
    transaction_window.geometry("400x350")
    transaction_window.configure(bg="#242f40")

    Label(transaction_window, text="Transfer From:", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    from_account_var = StringVar(transaction_window)
    from_account_var.set("Checking")  
    OptionMenu(transaction_window, from_account_var, "Checking", "Savings").pack(pady=5)

    # --- Load valid recipient accounts ---
    accounts_list, full_account_mapping = _get_recipient_accounts(account)

    Label(transaction_window, text="Recipient:", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    recipient_var = StringVar(transaction_window)
    recipient_var.set(accounts_list[0] if accounts_list else "No Accounts")
    OptionMenu(transaction_window, recipient_var, *accounts_list).pack(pady=5)

    Label(transaction_window, text="Enter Amount ($):", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    amount_entry = Entry(transaction_window, font=("Arial", 12), width=15)
    amount_entry.pack(pady=5)

    _add_confirm_cancel_buttons(transaction_window, account, root, from_account_var, amount_entry, "Transfer", recipient_var, full_account_mapping)


def _add_confirm_cancel_buttons(transaction_window, account, root, account_var, amount_entry, transaction_type, recipient_var=None, account_mapping=None):
    """
    Adds confirm and cancel buttons to the transaction window.

    Args:
        transaction_window (tk.Toplevel): The transaction pop-up window.
        account (dict): The logged-in user's account data.
        root (tk.Tk): The main application window.
        account_var (tk.StringVar): Selected account type (Checking/Savings).
        amount_entry (tk.Entry): The entry widget for transaction amount.
        transaction_type (str): The type of transaction ("Deposit", "Withdraw", "Transfer").
        recipient_var (tk.StringVar, optional): The recipient's selection for transfers.
        account_mapping (dict, optional): Maps recipient names to their usernames and account types.
    """
    button_frame = Frame(transaction_window, bg="#242f40")
    button_frame.pack(pady=10)

    confirm_button = Button(button_frame, text="Confirm", font=("Arial", 12, "bold"), bg="green", fg="white",
                            padx=10, command=lambda: handle_transaction(account, account_var.get(),
                                                                        amount_entry.get(), transaction_window, root,
                                                                        transaction_type, recipient_var, account_mapping))
    confirm_button.grid(row=0, column=0, padx=5)

    cancel_button = Button(button_frame, text="Cancel", font=("Arial", 12, "bold"), bg="red", fg="white",
                           padx=10, command=transaction_window.destroy)
    cancel_button.grid(row=0, column=1, padx=5)


def _get_recipient_accounts(account):
    """
    Retrieves a list of valid recipient accounts for transfers.

    Args:
        account (dict): The logged-in user's account data.

    Returns:
        tuple: (List of recipient account labels, Dictionary mapping labels to account details)
    """
    accounts_list = []
    full_account_mapping = {}

    for acc in load_accounts():
        if acc["username"] != account["username"]:
            checking_label = f"{acc['name']} - Checking"
            savings_label = f"{acc['name']} - Savings"
            
            accounts_list.append(checking_label)
            accounts_list.append(savings_label)
            full_account_mapping[checking_label] = (acc["username"], "Checking")
            full_account_mapping[savings_label] = (acc["username"], "Savings")

    return accounts_list, full_account_mapping

def handle_transaction(account, selected_account, amount, transaction_window, root, transaction_type, recipient=None, account_mapping=None):
    """
    Processes deposits, withdrawals, and transfers with correct validation.

    Args:
        account (dict): The logged-in user's account data.
        selected_account (str): The account type ("Checking" or "Savings").
        amount (str): The transaction amount as a string.
        transaction_window (tk.Toplevel): The transaction pop-up window.
        root (tk.Tk): The main application window.
        transaction_type (str): The type of transaction ("Deposit", "Withdraw", "Transfer").
        recipient (tk.StringVar, optional): The recipient's selection for transfers (StringVar object).
        account_mapping (dict, optional): Maps recipient names to their usernames and account types.
    """
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive.")
    except ValueError:
        tk.Label(transaction_window, text="⚠️ Invalid amount!", font=("Arial", 10), bg="#242f40", fg="red").pack(pady=5)
        return

    # Extract string value if recipient is a StringVar
    recipient_selection = recipient.get() if isinstance(recipient, tk.StringVar) else recipient

    # Process the transaction based on type
    if transaction_type == "Deposit":
        success, error = process_deposit(account, selected_account, amount)
    elif transaction_type == "Withdraw":
        success, error = process_withdraw(account, selected_account, amount)
    elif transaction_type == "Transfer":
        if not recipient_selection or not account_mapping:
            success, error = False, "⚠️ No valid recipient selected."
        else:
            success, error = process_transfer(account, selected_account, recipient_selection, account_mapping, amount)
    else:
        success, error = False, "⚠️ Invalid transaction type."

    # Handle success or display error message
    if success:
        transaction_window.destroy()
        from ui_account import show_account_screen  
        show_account_screen(account, root)  # Refresh account screen
    else:
        tk.Label(transaction_window, text=error, font=("Arial", 10), bg="#242f40", fg="red").pack(pady=5)