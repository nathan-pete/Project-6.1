import tkinter as tk

def create_window():
    """Create a Tkinter window with a label and a title."""
    # Create the main window
    root = tk.Tk()
    root.title("Tkinter Window")
    root.geometry("400x400")

    # Create a label with text
    label = tk.Label(root, text="Hello, Tkinter!")
    label.pack()

    # Start the main event loop
    root.mainloop()

# Call the function to create the window
create_window()