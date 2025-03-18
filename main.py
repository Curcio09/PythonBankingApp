from tkinter import Tk
from ui_login import show_login_screen

# GUI Configuration Constants
WINDOW_TITLE = "Curcio National Bank (CNB)"
WINDOW_SIZE = "600x800"
WINDOW_BG = "#242f40"

def create_main_window():
    """
    Initializes and configures the main application window.
    
    - Sets the title, size, and background color.
    - Displays the login screen.
    - Starts the Tkinter event loop.
    """
    root = Tk()
    root.title(WINDOW_TITLE)
    root.geometry(WINDOW_SIZE)
    root.minsize(600, 800)  # Prevents shrinking below 600x800
    root.configure(bg=WINDOW_BG)

    show_login_screen(root)  # Load the login screen UI

    root.mainloop()  # Start the Tkinter event loop

if __name__ == "__main__":
    create_main_window()  # Execute only if the script is run directly