import tkinter as tk
from PIL import Image, ImageTk  # Required for handling images
import json
import os
import random

# File where account data is stored
DATA_FILE = "accounts.json"

# Function to Load Account Data from JSON
def load_accounts():
    if os.path.exists(DATA_FILE):  # Check if the file exists
        with open(DATA_FILE, "r") as file:  # Open the file in read mode
            return json.load(file)  # Load the JSON data into a Python dictionary
    else:
        return None  # No data exists yet

# Function to Save Account Data to JSON
def save_accounts(accounts):
    with open(DATA_FILE, "w") as file:  # Open the file in write mode
        json.dump(accounts, file, indent=4)  # Convert Python data to JSON and save

# Function to Generate Account Data if Not Already Stored
def initialize_accounts():
    accounts = load_accounts()  # Try to load existing accounts from JSON
    if accounts is None:  # If no saved data exists, create new accounts
        accounts = [
            {"name": "Chris Curcio", "username": "curcio_admin", "password": "SecureBank123!",
             "account_number": random.randint(1000000000, 9999999999),  # Generate a 10-digit account number
             "routing_number": random.randint(100000000, 999999999),    # Generate a 9-digit routing number
             "checking_balance": round(random.uniform(500, 5000), 2),  # Random balance between $500-$5000
             "savings_balance": round(random.uniform(1000, 10000), 2)}, # Random balance between $1000-$10000

            {"name": "Richard Caldwell", "username": "richardC89", "password": "CNB$avings321",
             "account_number": random.randint(1000000000, 9999999999),
             "routing_number": random.randint(100000000, 999999999),
             "checking_balance": round(random.uniform(500, 5000), 2),
             "savings_balance": round(random.uniform(1000, 10000), 2)},

            {"name": "Sarah West", "username": "sarah_west", "password": "DepositNow789!",
             "account_number": random.randint(1000000000, 9999999999),
             "routing_number": random.randint(100000000, 999999999),
             "checking_balance": round(random.uniform(500, 5000), 2),
             "savings_balance": round(random.uniform(1000, 10000), 2)},

            {"name": "Mark Thompson", "username": "markT_CNB", "password": "TrustBank654@",
             "account_number": random.randint(1000000000, 9999999999),
             "routing_number": random.randint(100000000, 999999999),
             "checking_balance": round(random.uniform(500, 5000), 2),
             "savings_balance": round(random.uniform(1000, 10000), 2)}
        ]
        save_accounts(accounts)  # Save accounts to JSON for future use
    return accounts  # Return the list of accounts

# Load accounts from JSON (or create them if they don't exist)
accounts = initialize_accounts()

# Function to Show the Account Screen
def show_account_screen(account):
    # Clear the login screen
    for widget in root.winfo_children():
        widget.destroy()

    # Account Screen Header
    account_header = tk.Label(root, text=f"Welcome, {account['name']}", font=("Arial", 18, "bold"), bg="#242f40", fg="white")
    account_header.pack(pady=20)

    # Display Account Information
    info_text = f"""
    Account Number: {account['account_number']}
    Routing Number: {account['routing_number']}

    Checking Balance: ${account['checking_balance']:.2f}
    Savings Balance: ${account['savings_balance']:.2f}
    """
    account_info = tk.Label(root, text=info_text, font=("Arial", 14), bg="#242f40", fg="white", justify="left")
    account_info.pack(pady=10)

    # Sign Out Button (Takes user back to login screen)
    sign_out_button = tk.Button(root, text="Sign Out", font=("Arial", 14, "bold"), bg="red", fg="white", command=restart_program)
    sign_out_button.pack(pady=20)

# Function to Restart the Program (Sign Out)
def restart_program():
    root.destroy()  # Closes the window
    os.system("python bankMain.py")  # Reopens the program (Ensure the filename is correct)

# Function to Handle Login
def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    # Check if fields are empty
    if not username or not password:
        error_label.config(text="⚠️ Username and Password cannot be empty!", fg="red")
        return

    # Check credentials against accounts.json
    for account in accounts:
        if account["username"] == username and account["password"] == password:
            error_label.config(text="✅ Login successful!", fg="green")
            show_account_screen(account)  # Call the function to load the account screen
            return
    
    # If no match was found
    error_label.config(text="❌ Invalid username or password!", fg="red")

# Create the main window
root = tk.Tk()
root.title("Curcio National Bank (CNB)")
root.geometry("600x800")
root.configure(bg="#242f40")  # Background color

# Load the logo image
logo_image = Image.open("logo.png")  # Open the image file
logo_image = logo_image.resize((200, 200))  # Resize the logo
logo_photo = ImageTk.PhotoImage(logo_image)  # Convert to Tkinter-compatible format

# Display the logo
logo_label = tk.Label(root, image=logo_photo, bg="#2e3b4d")
logo_label.pack(pady=(30, 30))  # Moves it down slightly

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

# Submit Button
submit_button = tk.Button(root, text="Submit", font=("Arial", 14, "bold"), bg="#d4b270", fg="black", padx=20, pady=10, command=login)
submit_button.pack(pady=(30, 20))

# Bind Enter key to trigger login
root.bind("<Return>", lambda event: login())

# Error Message Label (Hidden Initially)
error_label = tk.Label(root, text="", font=("Arial", 12), bg="#242f40", fg="red")
error_label.pack(pady=5)

# Sample Login Table Title
table_title = tk.Label(root, text="Demo Accounts", font=("Arial", 14, "bold"), bg="#242f40", fg="white")
table_title.pack(pady=(40, 5))

# Wrapper Frame to Create a White Border
border_wrapper = tk.Frame(root, bg="white", padx=2, pady=2)  # White Border Effect
border_wrapper.pack(pady=5)

# Table Frame (Inside the White Border)
table_frame = tk.Frame(border_wrapper, bg="#242f40", borderwidth=2, relief="solid")  
table_frame.pack()

# Display Table Rows using `accounts` data from JSON
for row_index, account in enumerate(accounts, start=1):
    tk.Label(table_frame, text=account["username"], font=("Arial", 10), bg="#242f40", fg="white", padx=30, pady=2).grid(row=row_index, column=0, padx=20, pady=2, sticky="nsew")
    tk.Label(table_frame, text=account["password"], font=("Arial", 10), bg="#242f40", fg="white", padx=30, pady=2).grid(row=row_index, column=1, padx=20, pady=2, sticky="nsew")

# Run the application
root.mainloop()