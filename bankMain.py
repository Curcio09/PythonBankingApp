import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Curcio National Bank (CNB)")
root.geometry("600x800")
root.configure(bg="#547a9a")  # Darker blue background

# Heading Label (Gold text, centered with padding)
heading = tk.Label(root, text="Curcio National Bank (CNB)", font=("Garamond", 30, "bold"), bg="#547a9a", fg="#FFD700")
heading.pack(pady=(150, 15))  # Moves it down

# Username Label and Entry
username_label = tk.Label(root, text="Username:", font=("Arial", 14), bg="#547a9a", fg="white")
username_label.pack(pady=5)
username_entry = tk.Entry(root, font=("Arial", 22), width=25)
username_entry.pack(pady=10)

# Password Label and Entry
password_label = tk.Label(root, text="Password:", font=("Arial", 14), bg="#547a9a", fg="white")
password_label.pack(pady=5)
password_entry = tk.Entry(root, font=("Arial", 22), width=25, show="*")
password_entry.pack(pady=10)

# Submit Button (Gold color)
submit_button = tk.Button(root, text="Submit", font=("Arial", 14, "bold"), bg="white", fg="black", padx=20, pady=10)
submit_button.pack(pady=(30, 20))  # Adds spacing below password entry

# Run the application
root.mainloop()
