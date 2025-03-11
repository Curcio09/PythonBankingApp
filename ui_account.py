import tkinter as tk
from PIL import Image, ImageTk
from auth import restart_program
from ui_transaction_history import open_transaction_history
from ui_transactions import open_deposit_window, open_withdraw_window, open_transfer_window

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
        logo_label.image = logo_photo  # Prevent garbage collection
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

    # Table Frame (White Background) using `grid()`
    table_frame = tk.Frame(table_wrapper, bg="white")
    table_frame.grid(padx=2, pady=2)

    # Table Headers (Account | Balance)
    header_frame = tk.Frame(table_frame, bg="#1e2a38")
    header_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

    tk.Label(header_frame, text="Account", font=("Arial", 12, "bold"),
             bg="#1e2a38", fg="#d4b270", width=25, padx=5, pady=5).grid(row=0, column=0, sticky="w")
    tk.Label(header_frame, text="Balance", font=("Arial", 12, "bold"),
             bg="#1e2a38", fg="#d4b270", width=15, padx=5, pady=5).grid(row=0, column=1, sticky="e")

    # Checking Account Row
    tk.Label(table_frame, text=f"Checking Account #{account['account_number']}",
             font=("Arial", 12), bg="white", fg="black", width=25, padx=5, pady=5).grid(row=1, column=0, sticky="w")
    tk.Label(table_frame, text=f"${account['checking_balance']:.2f}",
             font=("Arial", 12, "bold"), bg="white", fg="black", width=15, padx=5, pady=5).grid(row=1, column=1, sticky="e")

    # Savings Account Row
    tk.Label(table_frame, text=f"Savings Account #{account['account_number']}",
             font=("Arial", 12), bg="white", fg="black", width=25, padx=5, pady=5).grid(row=2, column=0, sticky="w")
    tk.Label(table_frame, text=f"${account['savings_balance']:.2f}",
             font=("Arial", 12, "bold"), bg="white", fg="black", width=15, padx=5, pady=5).grid(row=2, column=1, sticky="e")

    # Buttons Frame
    buttons_frame = tk.Frame(root, bg="#242f40")
    buttons_frame.pack(pady=20)

    # Deposit Button
    tk.Button(buttons_frame, text="Deposit", font=("Arial", 14, "bold"), bg="#d4b270", fg="black",
              padx=20, pady=10, command=lambda: open_deposit_window(account, root)).grid(row=0, column=0, padx=10)

    # Withdraw Button
    tk.Button(buttons_frame, text="Withdraw", font=("Arial", 14, "bold"), bg="#d4b270", fg="black",
              padx=20, pady=10, command=lambda: open_withdraw_window(account, root)).grid(row=0, column=1, padx=10)

    # Transfer Button
    tk.Button(buttons_frame, text="Transfer", font=("Arial", 14, "bold"), bg="#d4b270", fg="black",
              padx=20, pady=10, command=lambda: open_transfer_window(account, root)).grid(row=0, column=2, padx=10)

    # Transaction History Buttons Frame
    history_frame = tk.Frame(root, bg="#242f40")
    history_frame.pack(pady=10)

    tk.Button(history_frame, text="Checking History", font=("Arial", 12, "bold"),
              bg="#d4b270", fg="black", padx=20, pady=5,
              command=lambda: open_transaction_history(account, "Checking", root)).grid(row=0, column=0, padx=10)

    tk.Button(history_frame, text="Savings History", font=("Arial", 12, "bold"),
              bg="#d4b270", fg="black", padx=20, pady=5,
              command=lambda: open_transaction_history(account, "Savings", root)).grid(row=0, column=1, padx=10)

