import tkinter as tk
from ui import show_login_screen  # Import only the necessary UI function

# Function to create the main application window
def create_main_window():
    root = tk.Tk()
    root.title("Curcio National Bank (CNB)")
    root.geometry("600x800")
    root.configure(bg="#242f40")

    # Call the function to display the login screen
    show_login_screen(root)

    # Run the Tkinter event loop
    root.mainloop()

# Run the application if this script is executed directly
if __name__ == "__main__":
    create_main_window()