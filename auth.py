import os
from database import load_accounts

def get_accounts():
    """
    Loads account data from JSON file.

    Returns:
        list: A list of account dictionaries containing username and password.
    """
    return load_accounts()

def authenticate_user(username, password):
    """
    Checks if the provided username and password match an existing account.

    Args:
        username (str): The entered username.
        password (str): The entered password.

    Returns:
        dict or None: The matched account dictionary if credentials are correct, otherwise None.
    """
    accounts = get_accounts()
    for account in accounts:
        if account["username"] == username and account["password"] == password:
            return account
    return None

def login(username_entry, password_entry, root, error_label, show_account_screen):
    """
    Handles user login by validating credentials and displaying the appropriate screen.

    Args:
        username_entry (tk.Entry): Entry widget for the username.
        password_entry (tk.Entry): Entry widget for the password.
        root (tk.Tk): The main Tkinter window.
        error_label (tk.Label): Label to display error messages.
        show_account_screen (function): Function to load the account screen.

    Returns:
        None
    """
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        error_label.config(text="⚠️ Username and Password cannot be empty!", fg="red")
        return

    account = authenticate_user(username, password)
    
    if account:
        error_label.config(text="✅ Login successful!", fg="green")
        show_account_screen(account, root)
    else:
        error_label.config(text="❌ Invalid username or password!", fg="red")

def restart_program(root):
    """
    Restarts the program by closing the window and re-executing main.py.

    Args:
        root (tk.Tk): The main Tkinter window.

    Returns:
        None
    """
    root.destroy()  # Close the window
    try:
        os.system("python main.py")  # Restart the program
    except Exception as e:
        print(f"Error restarting program: {e}")