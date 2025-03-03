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
