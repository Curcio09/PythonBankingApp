import tkinter as tk
from PIL import Image, ImageTk  # Required for handling images
from auth import login, restart_program
from database import load_accounts

# Function to Show the Login Screen
def show_login_screen(root):
    # Clear the screen
    for widget in root.winfo_children():
        widget.destroy()

    # Load the logo image
    try:
        logo_image = Image.open("logo.png")
        logo_image = logo_image.resize((200, 200))  # Match original size
        logo_photo = ImageTk.PhotoImage(logo_image)

        # Display the logo
        logo_label = tk.Label(root, image=logo_photo, bg="#2e3b4d")  # Match background
        logo_label.image = logo_photo  # Prevent garbage collection
        logo_label.pack(pady=(30, 30))  # Adjust spacing
    except Exception as e:
        print("Error loading logo:", e)

    # Username Label and Entry
    username_label = tk.Label(root, text="Username:", font=("Arial", 14), bg="#242f40", fg="#d4b270")
    username_label.pack(pady=5)
    username_entry = tk.Entry(root, font=("Arial", 22), width=22)
    username_entry.pack(pady=5)

    # Password Label and Entry
    password_label = tk.Label(root, text="Password:", font=("Arial", 14), bg="#242f40", fg="#d4b270")
    password_label.pack(pady=5)
    password_entry = tk.Entry(root, font=("Arial", 22), width=22, show="*")
    password_entry.pack(pady=5)

    # Error Message Label
    error_label = tk.Label(root, text="", font=("Arial", 12), bg="#242f40", fg="red")
    error_label.pack(pady=5)

    # Submit Button
    submit_button = tk.Button(root, text="Submit", font=("Arial", 14, "bold"), bg="#d4b270", fg="black",
                              padx=20, pady=10, command=lambda: login(username_entry, password_entry, root, error_label, show_account_screen))
    submit_button.pack(pady=(30, 20))  # Adjusted spacing to match original

    # Bind Enter key to trigger login
    root.bind("<Return>", lambda event: login(username_entry, password_entry, root, error_label, show_account_screen))

    # Demo Accounts Table Title
    table_title = tk.Label(root, text="Demo Accounts", font=("Arial", 14, "bold"), bg="#242f40", fg="white")
    table_title.pack(pady=(40, 5))  # Adjusted to match original

    # Wrapper Frame to Create a White Border
    border_wrapper = tk.Frame(root, bg="white", padx=2, pady=2)  # White Border Effect
    border_wrapper.pack(pady=5)

    # Table Frame (Inside the White Border)
    table_frame = tk.Frame(border_wrapper, bg="#242f40", borderwidth=2, relief="solid")  
    table_frame.pack()

    # Demo Accounts Data
    demo_accounts = [
        {"username": "curcio_admin", "password": "SecureBank123!"},
        {"username": "richardC89", "password": "CNB$avings321"},
        {"username": "sarah_west", "password": "DepositNow789!"},
        {"username": "markT_CNB", "password": "TrustBank654@"}
    ]

    # Generate Table Rows
    for row_index, account in enumerate(demo_accounts, start=1):
        tk.Label(table_frame, text=account["username"], font=("Arial", 10), bg="#242f40", fg="white",
                 padx=30, pady=2).grid(row=row_index, column=0, padx=20, pady=2, sticky="nsew")
        tk.Label(table_frame, text=account["password"], font=("Arial", 10), bg="#242f40", fg="white",
                 padx=30, pady=2).grid(row=row_index, column=1, padx=20, pady=2, sticky="nsew")

# Function to Show the Account Screen
def show_account_screen(account, root):
    # Clear the login screen
    for widget in root.winfo_children():
        widget.destroy()

    # Create a top frame for logo and sign-out button
    top_frame = tk.Frame(root, bg="#242f40")
    top_frame.pack(fill="x", pady=(10, 20))

    # Load and display the bank logo
    try:
        logo_image = Image.open("logo.png")
        logo_image = logo_image.resize((100, 100))  # Adjust size
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

    # Table Wrapper (Adds Black Border)
    table_wrapper = tk.Frame(root, bg="black", borderwidth=2, relief="solid")
    table_wrapper.pack(pady=10)

    # Table Frame (White Background)
    table_frame = tk.Frame(table_wrapper, bg="white")
    table_frame.pack(padx=2, pady=2)

    # Table Headers (Account | Balance)
    header_frame = tk.Frame(table_frame, bg="#1e2a38")  # Darker Blue Background
    header_frame.pack(fill="x")

    account_header = tk.Label(header_frame, text="Account", font=("Arial", 12, "bold"),
                              bg="#1e2a38", fg="#d4b270", width=25, padx=5, pady=5)
    account_header.grid(row=0, column=0, sticky="w")

    balance_header = tk.Label(header_frame, text="Balance", font=("Arial", 12, "bold"),
                              bg="#1e2a38", fg="#d4b270", width=15, padx=5, pady=5)
    balance_header.grid(row=0, column=1, sticky="e")

    # Checking Account Row
    checking_frame = tk.Frame(table_frame, bg="white")
    checking_frame.pack(fill="x")

    checking_label = tk.Label(checking_frame, text=f"Checking Account #{account['account_number']}",
                              font=("Arial", 12), bg="white", fg="black", width=25, padx=5, pady=5)
    checking_label.grid(row=0, column=0, sticky="w")

    checking_balance = tk.Label(checking_frame, text=f"${account['checking_balance']:.2f}",
                                font=("Arial", 12, "bold"), bg="white", fg="black", width=15, padx=5, pady=5)
    checking_balance.grid(row=0, column=1, sticky="e")

    # Savings Account Row
    savings_frame = tk.Frame(table_frame, bg="white")
    savings_frame.pack(fill="x")

    savings_label = tk.Label(savings_frame, text=f"Savings Account #{account['account_number']}",
                             font=("Arial", 12), bg="white", fg="black", width=25, padx=5, pady=5)
    savings_label.grid(row=1, column=0, sticky="w")

    savings_balance = tk.Label(savings_frame, text=f"${account['savings_balance']:.2f}",
                               font=("Arial", 12, "bold"), bg="white", fg="black", width=15, padx=5, pady=5)
    savings_balance.grid(row=1, column=1, sticky="e")

    # Buttons Frame
    buttons_frame = tk.Frame(root, bg="#242f40")
    buttons_frame.pack(pady=20)

    # Deposit Button
    deposit_button = tk.Button(buttons_frame, text="Deposit", font=("Arial", 14, "bold"), bg="#d4b270", fg="black",
                            padx=20, pady=10, command=lambda: open_deposit_window(account, root))
    deposit_button.grid(row=0, column=0, padx=10)

    # Withdraw Button
    withdraw_button = tk.Button(buttons_frame, text="Withdraw", font=("Arial", 14, "bold"), bg="#d4b270", fg="black",
                                padx=20, pady=10, command=lambda: open_withdraw_window(account, root))
    withdraw_button.grid(row=0, column=1, padx=10)

    # Transfer Button
    transfer_button = tk.Button(buttons_frame, text="Transfer", font=("Arial", 14, "bold"), bg="#d4b270", fg="black",
                                padx=20, pady=10, command=lambda: open_transfer_window(account, root))
    transfer_button.grid(row=0, column=2, padx=10)

def open_deposit_window(account, root):
    # Create a popup window
    deposit_window = tk.Toplevel(root)
    deposit_window.title("Deposit Funds")
    deposit_window.geometry("300x250")
    deposit_window.configure(bg="#242f40")

    # Dropdown for Account Selection (Checking or Savings)
    tk.Label(deposit_window, text="Select Account:", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    account_var = tk.StringVar(deposit_window)
    account_var.set("Checking")  # Default selection
    account_dropdown = tk.OptionMenu(deposit_window, account_var, "Checking", "Savings")
    account_dropdown.pack(pady=5)

    # Amount Entry
    tk.Label(deposit_window, text="Enter Amount ($):", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    amount_entry = tk.Entry(deposit_window, font=("Arial", 12), width=15)
    amount_entry.pack(pady=5)

    # Confirm and Cancel Buttons
    button_frame = tk.Frame(deposit_window, bg="#242f40")
    button_frame.pack(pady=10)

    confirm_button = tk.Button(button_frame, text="Confirm", font=("Arial", 12, "bold"), bg="green", fg="white",
                               padx=10, command=lambda: process_deposit(account, account_var.get(), amount_entry.get(), deposit_window, root))
    confirm_button.grid(row=0, column=0, padx=5)

    cancel_button = tk.Button(button_frame, text="Cancel", font=("Arial", 12, "bold"), bg="red", fg="white",
                              padx=10, command=deposit_window.destroy)
    cancel_button.grid(row=0, column=1, padx=5)

from database import update_account  # Import to save changes

def process_deposit(account, selected_account, amount, deposit_window, root):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        # Update the selected account balance
        if selected_account == "Checking":
            account["checking_balance"] += amount
        else:
            account["savings_balance"] += amount

        # Save updated balance
        update_account(account)

        # Close the deposit window
        deposit_window.destroy()

        # Refresh the account screen to show the new balance
        show_account_screen(account, root)

    except ValueError:
        # Show error if input is invalid
        error_label = tk.Label(deposit_window, text="⚠️ Invalid amount!", font=("Arial", 10), bg="#242f40", fg="red")
        error_label.pack(pady=5)

def open_withdraw_window(account, root):
    # Create a popup window
    withdraw_window = tk.Toplevel(root)
    withdraw_window.title("Withdraw Funds")
    withdraw_window.geometry("300x250")
    withdraw_window.configure(bg="#242f40")

    # Dropdown for Account Selection (Checking or Savings)
    tk.Label(withdraw_window, text="Select Account:", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    account_var = tk.StringVar(withdraw_window)
    account_var.set("Checking")  # Default selection
    account_dropdown = tk.OptionMenu(withdraw_window, account_var, "Checking", "Savings")
    account_dropdown.pack(pady=5)

    # Amount Entry
    tk.Label(withdraw_window, text="Enter Amount ($):", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    amount_entry = tk.Entry(withdraw_window, font=("Arial", 12), width=15)
    amount_entry.pack(pady=5)

    # Confirm and Cancel Buttons
    button_frame = tk.Frame(withdraw_window, bg="#242f40")
    button_frame.pack(pady=10)

    confirm_button = tk.Button(button_frame, text="Confirm", font=("Arial", 12, "bold"), bg="green", fg="white",
                               padx=10, command=lambda: process_withdraw(account, account_var.get(), amount_entry.get(), withdraw_window, root))
    confirm_button.grid(row=0, column=0, padx=5)

    cancel_button = tk.Button(button_frame, text="Cancel", font=("Arial", 12, "bold"), bg="red", fg="white",
                              padx=10, command=withdraw_window.destroy)
    cancel_button.grid(row=0, column=1, padx=5)

from database import update_account  # Ensure this is imported

def process_withdraw(account, selected_account, amount, withdraw_window, root):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        # Determine which balance to check and update
        if selected_account == "Checking":
            if amount > account["checking_balance"]:
                raise ValueError("Insufficient funds.")
            account["checking_balance"] -= amount
        else:
            if amount > account["savings_balance"]:
                raise ValueError("Insufficient funds.")
            account["savings_balance"] -= amount

        # Save updated balance
        update_account(account)

        # Close the withdraw window
        withdraw_window.destroy()

        # Refresh the account screen to show the new balance
        show_account_screen(account, root)

    except ValueError as e:
        # Show error if input is invalid or insufficient funds
        error_label = tk.Label(withdraw_window, text=f"⚠️ {str(e)}", font=("Arial", 10), bg="#242f40", fg="red")
        error_label.pack(pady=5)

def open_transfer_window(account, root):
    # Create a popup window
    transfer_window = tk.Toplevel(root)
    transfer_window.title("Transfer Funds")
    transfer_window.geometry("350x300")
    transfer_window.configure(bg="#242f40")

    # Dropdown for Selecting Account to Transfer From
    tk.Label(transfer_window, text="Transfer From:", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    from_account_var = tk.StringVar(transfer_window)
    from_account_var.set("Checking")  # Default selection
    from_account_dropdown = tk.OptionMenu(transfer_window, from_account_var, "Checking", "Savings")
    from_account_dropdown.pack(pady=5)

    # Dropdown for Selecting Recipient (Now Shows Full Name and Account Type)
    tk.Label(transfer_window, text="Send To:", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    
    # Generate a list of recipient options in "Full Name - Account Type" format
    accounts_list = []
    full_account_mapping = {}  # Dictionary to map dropdown text to username
    
    for acc in load_accounts():
        if acc["username"] != account["username"]:  # Exclude the sender
            checking_label = f"{acc['name']} - Checking"
            savings_label = f"{acc['name']} - Savings"
            
            accounts_list.append(checking_label)
            accounts_list.append(savings_label)
            
            # Store the actual username and account type
            full_account_mapping[checking_label] = (acc["username"], "Checking")
            full_account_mapping[savings_label] = (acc["username"], "Savings")

    recipient_var = tk.StringVar(transfer_window)
    recipient_var.set(accounts_list[0] if accounts_list else "No Accounts")  # Default selection
    recipient_dropdown = tk.OptionMenu(transfer_window, recipient_var, *accounts_list)
    recipient_dropdown.pack(pady=5)

    # Amount Entry
    tk.Label(transfer_window, text="Enter Amount ($):", font=("Arial", 12), bg="#242f40", fg="white").pack(pady=5)
    amount_entry = tk.Entry(transfer_window, font=("Arial", 12), width=15)
    amount_entry.pack(pady=5)

    # Confirm and Cancel Buttons
    button_frame = tk.Frame(transfer_window, bg="#242f40")
    button_frame.pack(pady=10)

    confirm_button = tk.Button(button_frame, text="Confirm", font=("Arial", 12, "bold"), bg="green", fg="white",
                               padx=10, command=lambda: process_transfer(account, from_account_var.get(), recipient_var.get(), full_account_mapping, amount_entry.get(), transfer_window, root))
    confirm_button.grid(row=0, column=0, padx=5)

    cancel_button = tk.Button(button_frame, text="Cancel", font=("Arial", 12, "bold"), bg="red", fg="white",
                              padx=10, command=transfer_window.destroy)
    cancel_button.grid(row=0, column=1, padx=5)

from database import get_account, update_account  # Ensure these are imported

def process_transfer(account, from_account, recipient_selection, account_mapping, amount, transfer_window, root):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        # Determine sender's account balance
        if from_account == "Checking":
            if amount > account["checking_balance"]:
                raise ValueError("Insufficient funds.")
            account["checking_balance"] -= amount
        else:
            if amount > account["savings_balance"]:
                raise ValueError("Insufficient funds.")
            account["savings_balance"] -= amount

        # Retrieve recipient username and target account type
        if recipient_selection not in account_mapping:
            raise ValueError("Recipient account not found.")
        
        recipient_username, recipient_account_type = account_mapping[recipient_selection]
        recipient_account = get_account(recipient_username)

        if not recipient_account:
            raise ValueError("Recipient account not found.")

        # Update recipient's balance
        if recipient_account_type == "Checking":
            recipient_account["checking_balance"] += amount
        else:
            recipient_account["savings_balance"] += amount

        # Save updates
        update_account(account)
        update_account(recipient_account)

        # Close the transfer window
        transfer_window.destroy()

        # Refresh sender's UI to show new balance
        show_account_screen(account, root)

    except ValueError as e:
        # Show error if input is invalid
        error_label = tk.Label(transfer_window, text=f"⚠️ {str(e)}", font=("Arial", 10), bg="#242f40", fg="red")
        error_label.pack(pady=5)
