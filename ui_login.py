# ui_login.py
import tkinter as tk
from PIL import Image, ImageTk
from auth import login
from ui_account import show_account_screen

def show_login_screen(root):
    """Displays the login screen where users enter credentials."""
    # Clear the screen
    for widget in root.winfo_children():
        widget.destroy()

    # Load the logo image
    try:
        logo_image = Image.open("logo.png")
        logo_image = logo_image.resize((200, 200))  
        logo_photo = ImageTk.PhotoImage(logo_image)

        logo_label = tk.Label(root, image=logo_photo, bg="#2e3b4d")
        logo_label.image = logo_photo  # Prevent garbage collection
        logo_label.pack(pady=(30, 30))
    except Exception as e:
        print("Error loading logo:", e)

    # Username Entry
    tk.Label(root, text="Username:", font=("Arial", 14), bg="#242f40", fg="#d4b270").pack(pady=5)
    username_entry = tk.Entry(root, font=("Arial", 22), width=22)
    username_entry.pack(pady=5)

    # Password Entry
    tk.Label(root, text="Password:", font=("Arial", 14), bg="#242f40", fg="#d4b270").pack(pady=5)
    password_entry = tk.Entry(root, font=("Arial", 22), width=22, show="*")
    password_entry.pack(pady=5)

    # Error Message Label
    error_label = tk.Label(root, text="", font=("Arial", 12), bg="#242f40", fg="red")
    error_label.pack(pady=5)

    # Submit Button
    submit_button = tk.Button(root, text="Submit", font=("Arial", 14, "bold"), bg="#d4b270", fg="black",
                              padx=20, pady=10,
                              command=lambda: login(username_entry, password_entry, root, error_label, show_account_screen))
    submit_button.pack(pady=(30, 20))

     # Demo Accounts Table
    demo_accounts = [
        {"username": "curcio_admin", "password": "SecureBank123!"},
        {"username": "richardC89", "password": "CNB$avings321"},
        {"username": "sarah_west", "password": "DepositNow789!"},
        {"username": "markT_CNB", "password": "TrustBank654@"}
    ]

    # Wrapper Frame for Table
    border_wrapper = tk.Frame(root, bg="white", padx=2, pady=2)
    border_wrapper.pack(pady=5)

    table_frame = tk.Frame(border_wrapper, bg="#242f40", borderwidth=2, relief="solid")
    table_frame.pack()

    # Table Headers
    tk.Label(table_frame, text="Username", font=("Arial", 10, "bold"), bg="#242f40", fg="white", padx=30).grid(row=0, column=0, padx=20, pady=2)
    tk.Label(table_frame, text="Password", font=("Arial", 10, "bold"), bg="#242f40", fg="white", padx=30).grid(row=0, column=1, padx=20, pady=2)

    # Add Rows for Each Demo Account
    for row_index, account in enumerate(demo_accounts, start=1):
        tk.Label(table_frame, text=account["username"], font=("Arial", 10), bg="#242f40", fg="white",
                 padx=30, pady=2).grid(row=row_index, column=0, padx=20, pady=2, sticky="nsew")
        tk.Label(table_frame, text=account["password"], font=("Arial", 10), bg="#242f40", fg="white",
                 padx=30, pady=2).grid(row=row_index, column=1, padx=20, pady=2, sticky="nsew")

    # Bind Enter key to trigger login
    root.bind("<Return>", lambda event: login(username_entry, password_entry, root, error_label, show_account_screen))









   

