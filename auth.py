import os
import json
from database import load_accounts

# Load accounts from JSON
accounts = load_accounts()

# Function to Handle Login
def login(username_entry, password_entry, root, error_label, show_account_screen):
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
            show_account_screen(account, root)  # Call function to load the account screen
            return
    
    # If no match was found
    error_label.config(text="❌ Invalid username or password!", fg="red")

# Function to Restart the Program (Fixing ImportError)
def restart_program(root):
    root.destroy()  # Close the window
    os.system("python main.py")  # Restart the program