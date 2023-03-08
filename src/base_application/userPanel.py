import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
from tkinter import ttk
from adminLogin import login_admin_page




def create_window():
    """Create a Tkinter window with two equal sections."""

    # Create the main window
    root = tk.Tk()
    root.title("Tkinter Window")
    root.geometry("1200x900")

    def admin_login_button_click():
        root.destroy()
        login_admin_page()

    root.resizable(False, False)  # Prevent the window from being resized

    # Create a frame to hold the left section
    left_frame = tk.Frame(root, width=600, height=900, bg="#D9D9D9")  # Set the background color to grey
    left_frame.pack(side="left")

    # Create a label and text area for the User Panel
    label = tk.Label(left_frame, text="User Panel", font=("Inter", 24, "normal"), bg="#D9D9D9", fg="#000000",
                     justify="left")
    label.place(x=20, y=20, width=190, height=50)

    # Create a label and text area for the Welcome message
    label = tk.Label(left_frame, text="Welcome", font=("Inter", 18, "bold"), bg="#D9D9D9", fg="#000000", justify="left",
                     underline=len("Welcome"))
    label.place(x=30, y=200, width=190, height=50)

    # Create a label and text area for the User name
    entry = tk.Entry(left_frame, font=("Inter", 14))
    entry.place(x=70, y=300, width=280, height=24)

    style = ttk.Style()
    style.configure("RoundedButton.TButton", padding=6, relief="flat",
                    background="#000000", foreground="#FFFFFF",
                    font=("Inter", 14), borderwidth=0, bordercolor="#000000")
    style.map("RoundedButton.TButton", background=[("active", "#333333")])

    button1 = ttk.Button(left_frame, text="Keyboard Search",
                         command=lambda: print("Button 1 clicked!"))

    button1.place(x=70, y=400, width=150, height=24)

    style = ttk.Style()
    style.configure("RoundedButton.TButton", padding=6, relief="flat",
                    background="#000000", foreground="#FFFFFF",
                    font=("Inter", 14), borderwidth=0, bordercolor="#000000")
    style.map("RoundedButton.TButton", background=[("active", "#333333")])

    button2 = ttk.Button(left_frame, text="Admin Login",
                         command=admin_login_button_click)

    button2.place(x=250, y=400, width=150, height=24)

    # Create a frame to hold the right section
    right_frame = tk.Frame(root, width=600, height=900, bg="#F0AFAF")
    # Set the background color to pink
    right_frame.pack(side="right")  # Add padding to prevent overlap

    # Create a Treeview widget to display the table
    table = ttk.Treeview(right_frame, columns=("Date", "Details", "Description", "Ref", "Amount", "Edit"),
                         show="headings", style="Custom.Treeview")
    table.heading("Date", text="Date")
    table.heading("Details", text="Company Name")
    table.heading("Description", text="Description")
    table.heading("Ref", text="Ref")
    table.heading("Amount", text="Amount")
    table.heading("Edit", text="Edit")


    # Looping through the columns and get the heading
    for column in table["columns"]:
        # Assigning the heading as text of the column
        table.heading(column, text=column, command=lambda: None)
        # For each heading we are disabling the property of resizing the column
        table.bind("<Button-1>", lambda event: "break")

    # Apply the background color to the entire table
    style = ttk.Style()
    style.configure("Custom.Treeview", background="#F0AFAF")

    table.column("Date", width=100)  # Set the width of the first column
    table.column("Details", width=100)  # Set the width of the second column
    table.column("Description", width=100)  # Set the width of the third column
    table.column("Ref", width=50)  # Set the width of the forth column
    table.column("Amount", width=100)  # Set the width of the fifth
    table.column("Edit", width=100)  # Set the width of the fifth column to 20% of the table width
    table.config(height=2)  # Set the height of the table to 10 rows

    # Insert the data into the table
    # table.insert("", "end", values=("1/1/2021", "Company Name", "Description", "Ref", "Amount", "Edit"))
    # table.insert("", "end", values=("1/1/2021", "Company Name", "Description", "Ref", "Amount", "Edit"))
    # table.insert("", "end", values=("1/1/2021", "Company Name", "Description", "Ref", "Amount", "Edit"))

    retrieveDB(table)

    # Pack the table into the frame and center it horizontally
    table.pack(fill="both", expand=False)  # Fill the frame with the table
    table.place(x=30, y=150)  # Place the table 30 pixels from the left and 150 pixels from the top
    right_frame.pack_propagate(False)  # Prevent the frame from resizing to fit the table

    def on_closing():
        root.destroy()

    # Bind the on_closing function to the window close event
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Start the main event loop
    root.mainloop()

def retrieveDB(table):
    """Retrieve data from the database and insert it into the table."""

    # Retrieve data from the database
    conn = sqlite3.connect('quintor.db')
    cursor = conn.cursor()
    cursor.execute("SELECT transaction_date, transactionDetail, description, amount, referenceNumber FROM transactions")
    rows = cursor.fetchall()
    conn.close()

    # Clear existing rows in the table
    table.delete(*table.get_children())

    # Insert retrieved data into the table
    for row in rows:
        table.insert("", "end", values=row)
