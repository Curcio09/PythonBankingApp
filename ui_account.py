from tkinter import Label, Button, Frame
from PIL import Image, ImageTk
from auth import restart_program
from ui_transaction_history import open_transaction_history
from ui_transactions import open_deposit_window, open_withdraw_window, open_transfer_window

def show_account_screen(account, root):
    """
    Displays the user's account dashboard.

    - Clears previous UI elements.
    - Shows account holder’s name.
    - Displays account balances (Checking & Savings).
    - Provides options for deposits, withdrawals, transfers, and transaction history.
    - Includes a sign-out button.

    Args:
        account (dict): The currently logged-in user's account details.
        root (tk.Tk): The main application window.
    """

    # --- Clear Existing UI ---
    for widget in root.winfo_children():
        widget.destroy()

    # --- Create Top Frame (Logo & Sign Out Button) ---
    top_frame = Frame(root, bg="#242f40")
    top_frame.pack(fill="x", pady=(10, 20))

    # --- Load and Display Logo ---
    try:
        logo_image = Image.open("logo.png").resize((100, 100))
        logo_photo = ImageTk.PhotoImage(logo_image)
        
        logo_label = Label(top_frame, image=logo_photo, bg="#242f40")
        logo_label.image = logo_photo  # Prevent garbage collection
        logo_label.pack(side="left", padx=10)
    except Exception as e:
        print(f"Error loading logo: {e}")  # Debugging aid

    # --- Sign Out Button ---
    sign_out_button = Button(
        top_frame, text="Sign Out", font=("Arial", 12, "bold"),
        bg="red", fg="white", width=6, height=1,
        padx=10, pady=5, command=lambda: restart_program(root)
    )
    sign_out_button.pack(side="right", padx=10, pady=5)

    # --- Welcome Header ---
    Label(root, text=f"Welcome, {account['name']}", font=("Arial", 18, "bold"),
          bg="#242f40", fg="white").pack(pady=10)

    # --- Account Summary Section ---
    Label(root, text="Account Summary", font=("Arial", 16, "bold"),
          bg="#242f40", fg="white").pack(pady=(10, 5))

    # --- Table Wrapper (Adds Border) ---
    table_wrapper = Frame(root, bg="black", borderwidth=2, relief="solid")
    table_wrapper.pack(pady=10)

    # --- Table Frame (White Background) ---
    table_frame = Frame(table_wrapper, bg="white")
    table_frame.grid(padx=2, pady=2)

    # --- Table Headers ---
    header_frame = Frame(table_frame, bg="#1e2a38")
    header_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

    Label(header_frame, text="Account", font=("Arial", 12, "bold"),
          bg="#1e2a38", fg="#d4b270", width=25, padx=5, pady=5).grid(row=0, column=0, sticky="w")

    Label(header_frame, text="Balance", font=("Arial", 12, "bold"),
          bg="#1e2a38", fg="#d4b270", width=15, padx=5, pady=5).grid(row=0, column=1, sticky="e")

    # --- Checking Account Row ---
    Label(table_frame, text=f"Checking Account #{account['account_number']}",
          font=("Arial", 12), bg="white", fg="black", width=25, padx=5, pady=5).grid(row=1, column=0, sticky="w")

    Label(table_frame, text=f"${account['checking_balance']:.2f}",
          font=("Arial", 12, "bold"), bg="white", fg="black", width=15, padx=5, pady=5).grid(row=1, column=1, sticky="e")

    # --- Savings Account Row ---
    Label(table_frame, text=f"Savings Account #{account['account_number']}",
          font=("Arial", 12), bg="white", fg="black", width=25, padx=5, pady=5).grid(row=2, column=0, sticky="w")

    Label(table_frame, text=f"${account['savings_balance']:.2f}",
          font=("Arial", 12, "bold"), bg="white", fg="black", width=15, padx=5, pady=5).grid(row=2, column=1, sticky="e")

    # --- Action Buttons Frame ---
    buttons_frame = Frame(root, bg="#242f40")
    buttons_frame.pack(pady=20)

    # --- Deposit Button ---
    Button(buttons_frame, text="Deposit", font=("Arial", 14, "bold"), bg="#d4b270", fg="black",
           padx=17, pady=10, command=lambda: open_deposit_window(account, root)).grid(row=0, column=0, padx=10)

    # --- Withdraw Button ---
    Button(buttons_frame, text="Withdraw", font=("Arial", 14, "bold"), bg="#d4b270", fg="black",
           padx=17, pady=10, command=lambda: open_withdraw_window(account, root)).grid(row=0, column=1, padx=10)

    # --- Transfer Button ---
    Button(buttons_frame, text="Transfer", font=("Arial", 14, "bold"), bg="#d4b270", fg="black",
           padx=17, pady=10, command=lambda: open_transfer_window(account, root)).grid(row=0, column=2, padx=10)

    # --- Transaction History Section ---
    history_frame = Frame(root, bg="#242f40")
    history_frame.pack(pady=10)

    Button(history_frame, text="Checking History", font=("Arial", 14, "bold"),
           bg="#d4b270", fg="black", padx=18, pady=5,
           command=lambda: open_transaction_history(account, "Checking", root)).grid(row=0, column=0, padx=10)

    Button(history_frame, text="Savings History", font=("Arial", 14, "bold"),
           bg="#d4b270", fg="black", padx=18, pady=5,
           command=lambda: open_transaction_history(account, "Savings", root)).grid(row=0, column=1, padx=10)