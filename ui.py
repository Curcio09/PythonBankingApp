import tkinter as tk
from PIL import Image, ImageTk
from auth import restart_program
from database import load_accounts
from transactions import process_deposit, process_withdraw, process_transfer
from ui_transaction_history import open_transaction_history

# Function to Show the Account Screen
def show_account_screen(account, root):
    """Displays the account overview with balances and transaction options."""
    # Clear the login screen
    for widget in root.winfo_children():
        widget.destroy()

    # Create a top frame for logo and sign-out button
    top_frame = tk.Frame(root, bg="#242f40")
    top_frame.pack(fill="x", pady=(10, 20))

    # Load and display the bank logo
    try:
        logo_image = Image.open("logo.png")
        logo_image = logo_image.resize((100, 100))  
        logo_photo = ImageTk.PhotoImage(logo_image)

        logo_label = tk.Label(top_frame, image=logo_photo, bg="#242f40")
        logo_label.image = logo_photo
        logo_label.pack(side="left", padx=10)
    except Exception as e:
        print("Error loading logo:", e)

    # Sign Out Button
    sign_out_button = tk.Button(top_frame, text="Sign Out", font=("Arial", 12, "bold"),
                                bg="red", fg="white", command=lambda: restart_program(root))
    sign_out_button.pack(side="right", padx=10)

    # Account Screen Header
    account_header = tk.Label(root, text=f"Welcome, {account['name']}", font=("Arial", 18, "bold"),
                              bg="#242f40", fg="white")
    account_header.pack(pady=10)

    # Account Summary Header
    summary_label = tk.Label(root, text="Account Summary", font=("Arial", 16, "bold"),
                             bg="#242f40", fg="white")
    summary_label.pack(pady=(10, 5))

    # Table Wrapper (Adds Border)
    table_wrapper = tk.Frame(root, bg="black", borderwidth=2, relief="solid")
    table_wrapper.pack(pady=10)

    # Table Frame
    table_frame = tk.Frame(table_wrapper, bg="white")
    table_frame.pack(padx=2, pady=2)

    # Table Headers
    header_frame = tk.Frame(table_frame, bg="#1e2a38")
    header_frame.pack(fill="x")

    tk.Label(header_frame, text="Account", font=("Arial", 12, "bold"),
             bg="#1e2a38", fg="#d4b270", width=25, padx=5, pady=5).grid(row=0, column=0, sticky="w")

    tk.Label(header_frame, text="Balance", font=("Arial", 12, "bold"),
             bg="#1e2a38", fg="#d4b270", width=15, padx=5, pady=5).grid(row=0, column=1, sticky="e")

    # Checking Account Row
    checking_frame = tk.Frame(table_frame, bg="white")
    checking_frame.pack(fill="x")

    tk.Label(checking_frame, text=f"Checking Account #{account['account_number']}",
             font=("Arial", 12), bg="white", fg="black", width=25, padx=5, pady=5).grid(row=0, column=0, sticky="w")

    tk.Label(checking_frame, text=f"${account['checking_balance']:.2f}",
             font=("Arial", 12, "bold"), bg="white", fg="black", width=15, padx=5, pady=5).grid(row=0, column=1, sticky="e")

    # Savings Account Row
    savings_frame = tk.Frame(table_frame, bg="white")
    savings_frame.pack(fill="x")

    tk.Label(savings_frame, text=f"Savings Account #{account['account_number']}",
             font=("Arial", 12), bg="white", fg="black", width=25, padx=5, pady=5).grid(row=1, column=0, sticky="w")

    tk.Label(savings_frame, text=f"${account['savings_balance']:.2f}",
             font=("Arial", 12, "bold"), bg="white", fg="black", width=15, padx=5, pady=5).grid(row=1, column=1, sticky="e")

    # Buttons Frame
    buttons_frame = tk.Frame(root, bg="#242f40")
    buttons_frame.pack(pady=20)

    # Deposit Button
    tk.Button(buttons_frame, text="Deposit", font=("Arial", 14, "bold"), bg="#d4b270", fg="black",
              padx=20, pady=10, command=lambda: open_transaction_window(account, root, "Deposit")).grid(row=0, column=0, padx=10)

    # Withdraw Button
    tk.Button(buttons_frame, text="Withdraw", font=("Arial", 14, "bold"), bg="#d4b270", fg="black",
              padx=20, pady=10, command=lambda: open_transaction_window(account, root, "Withdraw")).grid(row=0, column=1, padx=10)

    # Transfer Button
    tk.Button(buttons_frame, text="Transfer", font=("Arial", 14, "bold"), bg="#d4b270", fg="black",
              padx=20, pady=10, command=lambda: open_transaction_window(account, root, "Transfer")).grid(row=0, column=2, padx=10)

    # Transaction History Buttons
    history_frame = tk.Frame(root, bg="#242f40")
    history_frame.pack(pady=10)

    tk.Button(history_frame, text="Checking History", font=("Arial", 12, "bold"),
              bg="#d4b270", fg="black", padx=20, pady=5,
              command=lambda: open_transaction_history(account, "Checking", root)).grid(row=0, column=0, padx=10)

    tk.Button(history_frame, text="Savings History", font=("Arial", 12, "bold"),
              bg="#d4b270", fg="black", padx=20, pady=5,
              command=lambda: open_transaction_history(account, "Savings", root)).grid(row=0, column=1, padx=10)

# Function to Open a Deposit/Withdraw/Transfer Window
def open_transaction_window(account, root, transaction_type):
    """Creates a pop-up window for deposit, withdrawal, or transfer."""
    transaction_window = tk.Toplevel(root)
    transaction_window.title(f"{transaction_type} Funds")
    transaction_window.geometry("350x300")
    transaction_window.configure(bg="#242f40")

    tk.Label(transaction_window, text=f"{transaction_type} Amount:", font=("Arial", 12),
             bg="#242f40", fg="white").pack(pady=5)
    amount_entry = tk.Entry(transaction_window, font=("Arial", 12), width=15)
    amount_entry.pack(pady=5)

    # Confirm and Cancel Buttons
    button_frame = tk.Frame(transaction_window, bg="#242f40")
    button_frame.pack(pady=10)

    confirm_button = tk.Button(button_frame, text="Confirm", font=("Arial", 12, "bold"),
                               bg="green", fg="white", padx=10,
                               command=lambda: process_transaction(account, transaction_type, amount_entry, transaction_window, root))
    confirm_button.grid(row=0, column=0, padx=5)

    cancel_button = tk.Button(button_frame, text="Cancel", font=("Arial", 12, "bold"),
                              bg="red", fg="white", padx=10, command=transaction_window.destroy)
    cancel_button.grid(row=0, column=1, padx=5)

# Function to Process Deposit, Withdrawal, or Transfer
def process_transaction(account, transaction_type, amount_entry, transaction_window, root):
    """Handles processing of deposits, withdrawals, and transfers."""
    amount = amount_entry.get()

    if transaction_type == "Deposit":
        success, error = process_deposit(account, "Checking", amount)  # Default to checking
    elif transaction_type == "Withdraw":
        success, error = process_withdraw(account, "Checking", amount)  # Default to checking
    else:  # Transfer
        success, error = process_transfer(account, "Checking", "Recipient", {}, amount)  # Simplified for now

    if success:
        transaction_window.destroy()
        show_account_screen(account, root)  # Refresh UI
    else:
        tk.Label(transaction_window, text=f"⚠️ {error}", font=("Arial", 10), bg="#242f40", fg="red").pack(pady=5)