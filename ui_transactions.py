import tkinter as tk
from transactions import process_deposit, process_withdraw, process_transfer
from database import load_accounts, get_account, update_account

def open_deposit_window(account, root):
    """Creates a pop-up window for deposits."""
    transaction_window = tk.Toplevel(root)
    transaction_window.title("Deposit Funds")
    transaction_window.geometry("350x250")
    transaction_window.configure(bg="#242f40")

    tk.Label(transaction_window, text="Select Account:", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    account_var = tk.StringVar(transaction_window)
    account_var.set("Checking")  
    account_dropdown = tk.OptionMenu(transaction_window, account_var, "Checking", "Savings")
    account_dropdown.pack(pady=5)

    tk.Label(transaction_window, text="Enter Amount ($):", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    amount_entry = tk.Entry(transaction_window, font=("Arial", 12), width=15)
    amount_entry.pack(pady=5)

    button_frame = tk.Frame(transaction_window, bg="#242f40")
    button_frame.pack(pady=10)

    confirm_button = tk.Button(button_frame, text="Confirm", font=("Arial", 12, "bold"), bg="green", fg="white",
                               padx=10, command=lambda: handle_transaction(account, account_var.get(), amount_entry.get(), transaction_window, root, "Deposit"))
    confirm_button.grid(row=0, column=0, padx=5)

    cancel_button = tk.Button(button_frame, text="Cancel", font=("Arial", 12, "bold"), bg="red", fg="white",
                              padx=10, command=transaction_window.destroy)
    cancel_button.grid(row=0, column=1, padx=5)

def open_withdraw_window(account, root):
    """Creates a pop-up window for withdrawals."""
    transaction_window = tk.Toplevel(root)
    transaction_window.title("Withdraw Funds")
    transaction_window.geometry("350x250")
    transaction_window.configure(bg="#242f40")

    tk.Label(transaction_window, text="Select Account:", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    account_var = tk.StringVar(transaction_window)
    account_var.set("Checking")  
    account_dropdown = tk.OptionMenu(transaction_window, account_var, "Checking", "Savings")
    account_dropdown.pack(pady=5)

    tk.Label(transaction_window, text="Enter Amount ($):", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    amount_entry = tk.Entry(transaction_window, font=("Arial", 12), width=15)
    amount_entry.pack(pady=5)

    button_frame = tk.Frame(transaction_window, bg="#242f40")
    button_frame.pack(pady=10)

    confirm_button = tk.Button(button_frame, text="Confirm", font=("Arial", 12, "bold"), bg="green", fg="white",
                               padx=10, command=lambda: handle_transaction(account, account_var.get(), amount_entry.get(), transaction_window, root, "Withdraw"))
    confirm_button.grid(row=0, column=0, padx=5)

    cancel_button = tk.Button(button_frame, text="Cancel", font=("Arial", 12, "bold"), bg="red", fg="white",
                              padx=10, command=transaction_window.destroy)
    cancel_button.grid(row=0, column=1, padx=5)

def open_transfer_window(account, root):
    """Creates a pop-up window for transfers between accounts."""
    transaction_window = tk.Toplevel(root)
    transaction_window.title("Transfer Funds")
    transaction_window.geometry("400x350")
    transaction_window.configure(bg="#242f40")

    tk.Label(transaction_window, text="Transfer From:", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    from_account_var = tk.StringVar(transaction_window)
    from_account_var.set("Checking")  
    from_account_dropdown = tk.OptionMenu(transaction_window, from_account_var, "Checking", "Savings")
    from_account_dropdown.pack(pady=5)

    # Load valid recipient accounts
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

    tk.Label(transaction_window, text="Recipient:", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    recipient_var = tk.StringVar(transaction_window)
    recipient_var.set(accounts_list[0] if accounts_list else "No Accounts")
    recipient_dropdown = tk.OptionMenu(transaction_window, recipient_var, *accounts_list)
    recipient_dropdown.pack(pady=5)

    tk.Label(transaction_window, text="Enter Amount ($):", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    amount_entry = tk.Entry(transaction_window, font=("Arial", 12), width=15)
    amount_entry.pack(pady=5)

    button_frame = tk.Frame(transaction_window, bg="#242f40")
    button_frame.pack(pady=10)

    confirm_button = tk.Button(button_frame, text="Confirm", font=("Arial", 12, "bold"), bg="green", fg="white",
                               padx=10, command=lambda: handle_transaction(account, from_account_var.get(), 
                                                                           amount_entry.get(), transaction_window, root, 
                                                                           "Transfer", recipient_var.get(), full_account_mapping))
    confirm_button.grid(row=0, column=0, padx=5)

    cancel_button = tk.Button(button_frame, text="Cancel", font=("Arial", 12, "bold"), bg="red", fg="white",
                              padx=10, command=transaction_window.destroy)
    cancel_button.grid(row=0, column=1, padx=5)

def handle_transaction(account, selected_account, amount, transaction_window, root, transaction_type, recipient=None, account_mapping=None):
    """Handles deposits, withdrawals, and transfers with correct data validation."""
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive.")
    except ValueError:
        tk.Label(transaction_window, text="⚠️ Invalid amount!", font=("Arial", 10), bg="#242f40", fg="red").pack(pady=5)
        return

    if transaction_type == "Deposit":
        success, error = process_deposit(account, selected_account, amount)

    elif transaction_type == "Withdraw":
        success, error = process_withdraw(account, selected_account, amount)

    elif transaction_type == "Transfer":
        if recipient is None or account_mapping is None:
            error = "⚠️ No valid recipient selected."
            success = False
        else:
            print(f"DEBUG: Raw recipient selection - {recipient}")  # Debugging
            success, error = process_transfer(account, selected_account, recipient, account_mapping, amount)

    if success:
        transaction_window.destroy()
        from ui_account import show_account_screen  
        show_account_screen(account, root)  # Refresh UI
    else:
        tk.Label(transaction_window, text=error, font=("Arial", 10), bg="#242f40", fg="red").pack(pady=5)