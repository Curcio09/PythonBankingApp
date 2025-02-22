import tkinter as tk
from PIL import Image, ImageTk  # Required for handling images

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
submit_button = tk.Button(root, text="Submit", font=("Arial", 14, "bold"), bg="#d4b270", fg="black", padx=20, pady=10)
submit_button.pack(pady=(30, 20))

# Sample Login Table Title
table_title = tk.Label(root, text="Demo Accounts", font=("Arial", 14, "bold"), bg="#242f40", fg="white")
table_title.pack(pady=(40, 5))

# Wrapper Frame to Create a White Border
border_wrapper = tk.Frame(root, bg="white", padx=2, pady=2)  # White Border Effect
border_wrapper.pack(pady=5)

# Table Frame (Inside the White Border)
table_frame = tk.Frame(border_wrapper, bg="#242f40", borderwidth=2, relief="solid")  
table_frame.pack()

# Table Headers
headers = ["Username", "Password"]
for i, text in enumerate(headers):
    tk.Label(
        table_frame, text=text, font=("Arial", 12, "bold"), bg="#242f40", fg="#d4b270",
        padx=30, pady=5
    ).grid(row=0, column=i, padx=20, pady=2, sticky="nsew")

# Sample User Data (Top 5)
sample_accounts = [
    ("curcio_admin", "SecureBank123!"),
    ("richardC89", "CNB$avings321"),
    ("sarah_west", "DepositNow789!"),
    ("markT_CNB", "TrustBank654@")
]

# Display Table Rows
for row_index, (username, password) in enumerate(sample_accounts, start=1):
    tk.Label(
        table_frame, text=username, font=("Arial", 10), bg="#242f40", fg="white",
        padx=30, pady=2
    ).grid(row=row_index, column=0, padx=20, pady=2, sticky="nsew")

    tk.Label(
        table_frame, text=password, font=("Arial", 10), bg="#242f40", fg="white",
        padx=30, pady=2
    ).grid(row=row_index, column=1, padx=20, pady=2, sticky="nsew")

# Keep a reference to the image (important to prevent garbage collection)
logo_label.image = logo_photo  

# Run the application
root.mainloop()