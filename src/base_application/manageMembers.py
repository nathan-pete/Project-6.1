import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import *
from member_registration_gui import member_registration


def manage_members():
    # Create the main window
    root = tk.Tk()
    root.title("Manage members")
    root.geometry("1200x900")

    # Create a frame to hold the left section

    # connect to the database
    def retrieveDB(table):
        conn = sqlite3.connect('quintor.db')
        cursor = conn.cursor()
        cursor.execute("")
        rows = cursor.fetchall()
        conn.close()

        # Clear existing rows in the table
        table.delete(*table.get_children())

        # Insert retrieved data into the table
        for row in rows:
            table.insert("", "end", values=row)

    def back_button_click():
        root.destroy()

    def add_member_button_click():
        member_registration()

    left_frame = tk.Frame(root, bg="#D9D9D9")  # Set the background color to grey
    left_frame.pack(side="left", fill="both", expand=True)

    # Create a frame to hold the right section
    right_frame = tk.Frame(root, bg="#F0AFAF")  # Set the background color to pink
    right_frame.pack(side="right", fill="both", expand=True, padx=(0, 5))  # Add padding to prevent overlap

    # Headings
    heading1 = tk.Label(left_frame, text="Admin panel", font=("Roboto", 24), bg="#D9D9D9", fg="#000000",
                        justify="center")
    heading1.place(x=15, y=20, width=200, height=40)

    heading2 = tk.Label(left_frame, text="Welcome", font=("Roboto", 14), bg="#D9D9D9", fg="#000000", justify="center")
    heading2.place(x=16, y=75, width=100, height=50)

    heading3 = tk.Label(left_frame, text="Manage members", font=("Roboto", 24), bg="#D9D9D9", fg="#000000",
                        justify="center")
    heading3.place(x=25, y=180, width=500, height=50)

    # TABLE
    table = ttk.Treeview(left_frame, columns=("Member ID", "Name", "Email", "Edit"), show="headings",
                         style="Custom.Treeview")
    table.heading("Member ID", text="Member ID")
    table.heading("Name", text="Name")
    table.heading("Email", text="Email")
    table.heading("Edit", text="Edit")

    for column in table["columns"]:
        # Assigning the heading as text of the column
        table.heading(column, text=column, command=lambda: None)
        table.bind("<Button-1>", lambda event: "break")

        retrieveDB(table)

    style = ttk.Style()
    style.configure("Custom.Treeview", background="#D9D9D9")

    table.column("Member ID", width=80)
    table.column("Name", width=160)
    table.column("Email", width=160)
    table.column("Edit", width=160)

    table.config(height=8)

    table.pack(fill="both", expand=False)
    table.place(x=16, y=280)
    left_frame.pack_propagate(False)

    # Right side
    heading4 = tk.Label(right_frame, text="Overview", font=("Roboto", 24), bg="#F0AFAF", fg="#000000", justify="center")
    heading4.place(x=220, y=80, width=200, height=50)

    heading5 = tk.Label(right_frame, text="All members", font=("Roboto", 14), bg="#F0AFAF", fg="#000000",
                        justify="center")
    heading5.place(x=220, y=200, width=200, height=50)
    # Buttons

    back_button = ttk.Button(left_frame, text="Back", command=lambda: back_button_click())
    back_button.place(x=30, y=850, width=100, height=30)

    add_member_button = ttk.Button(left_frame, text="Add member", command=lambda: add_member_button_click())
    add_member_button.place(x=140, y=550, width=300, height=80)

    # Start the main event loop
    root.mainloop()
