from tkinter import Label, Entry, Button, Frame
from PIL import Image, ImageTk
from auth import login
from ui_account import show_account_screen

def show_login_screen(root):
    """
    Displays the login screen where users enter credentials.

    - Clears any existing widgets from the root window.
    - Loads and displays the logo.
    - Creates input fields for username and password.
    - Adds a submit button that triggers login validation.
    - Displays demo account credentials for testing.
    - Allows pressing 'Enter' to submit login credentials.
    """
    
    # Clear any existing widgets from the root window before displaying login UI
    for widget in root.winfo_children():
        widget.destroy()

    # --- Load and Display Logo ---
    try:
        logo_image = Image.open("logo.png").resize((200, 200))  
        logo_photo = ImageTk.PhotoImage(logo_image)
        
        logo_label = Label(root, image=logo_photo, bg="#2e3b4d")
        logo_label.image = logo_photo  # Prevent garbage collection
        logo_label.pack(pady=(45, 30))
    except Exception as e:
        print(f"Error loading logo: {e}")  # Debugging aid

    # --- Username Input ---
    Label(root, text="Username:", font=("Arial", 14), bg="#242f40", fg="#d4b270").pack(pady=5)
    username_entry = Entry(root, font=("Arial", 16), width=22)
    username_entry.pack(pady=5, ipady=5)

    # --- Password Input ---
    Label(root, text="Password:", font=("Arial", 14), bg="#242f40", fg="#d4b270").pack(pady=5)
    password_entry = Entry(root, font=("Arial", 16), width=22, show="*")
    password_entry.pack(pady=5, ipady=5)

    # --- Error Message Label ---
    error_label = Label(root, text="", font=("Arial", 12), bg="#242f40", fg="red")
    error_label.pack(pady=5)

    # --- Submit Button ---
    submit_button = Button(
        root, text="Submit", font=("Arial", 12, "bold"),
        bg="#d4b270", fg="black", width=12, height=1,
        padx=10, pady=5,
        command=lambda: login(username_entry, password_entry, root, error_label, show_account_screen)
    )
    submit_button.pack(pady=(5, 15))  

    # --- Demo Accounts Table ---
    Label(root, text="Demo Accounts", font=("Arial", 14, "bold"), bg="#242f40", fg="#d4b270").pack(pady=(15, 5))

    demo_accounts = [
        {"username": "curcio_admin", "password": "SecureBank123!"},
        {"username": "richardC89", "password": "CNB$avings321"},
        {"username": "sarah_west", "password": "DepositNow789!"},
        {"username": "markT_CNB", "password": "TrustBank654@"}
    ]

    # Wrapper Frame for Table
    border_wrapper = Frame(root, bg="white", padx=2, pady=2)
    border_wrapper.pack(pady=5)

    table_frame = Frame(border_wrapper, bg="#242f40", borderwidth=2, relief="solid")
    table_frame.pack()

    # Table Headers
    Label(table_frame, text="Username", font=("Arial", 10, "bold"), bg="#242f40", fg="white", padx=30).grid(row=0, column=0, padx=20, pady=2)
    Label(table_frame, text="Password", font=("Arial", 10, "bold"), bg="#242f40", fg="white", padx=30).grid(row=0, column=1, padx=20, pady=2)

    # Add Rows for Each Demo Account
    for row_index, account in enumerate(demo_accounts, start=1):
        Label(table_frame, text=account["username"], font=("Arial", 10), bg="#242f40", fg="white",
              padx=30, pady=2).grid(row=row_index, column=0, padx=20, pady=2, sticky="nsew")
        Label(table_frame, text=account["password"], font=("Arial", 10), bg="#242f40", fg="white",
              padx=30, pady=2).grid(row=row_index, column=1, padx=20, pady=2, sticky="nsew")

    # --- Bind Enter Key to Submit ---
    root.bind("<Return>", lambda event: login(username_entry, password_entry, root, error_label, show_account_screen))