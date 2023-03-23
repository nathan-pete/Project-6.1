# ----------------------------------------------------- Imports ------------------------------------------------------ #
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from manageMembers import manage_members
from fileUpload import main
import requests
from src.base_application import api_server_ip


def adminPanel():
    selected_row = None
    window = tk.Tk()
    window.geometry("1200x900")
    window.title("Sports Accounting - Admin Panel")

    window.resizable(False, False)

    frame1 = tk.Frame(window, width=600, height=900, bg="#D9D9D9")
    frame2 = tk.Frame(window, width=600, height=900, bg="#F0AFAF")

    frame1.pack(side="left")
    frame2.pack(side="right")

    # Get balance from db
    balance = "No data"
    response = requests.get(api_server_ip + "/api/getFile")
    if len(response.json()) != 0:
        balance = response.json()[0][4]

    # --------------------------------------------------- Functions -------------------------------------------------- #
    def save_text():
        global input_text
        input_text = searchBar.get()
        savedText.config(text="Search Results for: " + input_text)
        print("Saved:", input_text)

    def manage_members_button():
        window.destroy()
        manage_members()

    def upload_button_click():
        main()

    def logout_button():
        # create_window()
        window.destroy()
        from userPanel import create_window
        create_window()

    # Define a function to be called when a row of the table is clicked
    def on_click_table_row(event):
        global selected_row
        # Get the selected item
        item = table.selection()[0]
        # Get the values of the selected item
        values = table.item(item, "values")
        selected_row = values[0]
        print(selected_row)

    def edit_button_click():
        global selected_row
        if selected_row is None:
            return
        window.destroy()
        from editTransaction import edit_transaction_page_admin
        edit_transaction_page_admin(selected_row)

    def retrieveDB():
        response = requests.get(api_server_ip + "/api/getTransactionsSQL")
        if len(response.json()) == 0:
            return

        # Convert JSON object into an array of tuples
        rows_out = []
        for entry in response.json():
            temp_tuple = (entry[0], entry[6], entry[2], entry[3], entry[1], entry[4])
            rows_out.append(tuple(temp_tuple))

        return rows_out

    # ---------------------------------------------------- Frame 1 --------------------------------------------------- #
    label = tk.Label(frame1, text="Admin Panel", font=("Inter", 24, "normal"), bg="#D9D9D9", fg="black", justify="left")
    label.place(x=20, y=20, width=190, height=50)

    label.config(anchor="nw", pady=0, padx=0, wraplength=0, height=0, width=0)

    line = tk.Label(frame1, text="_______________________________________________________",
                    font=("Inter", 18, "normal"), bg="#D9D9D9", fg="black", justify="left")
    line.place(x=61, y=180, width=450, height=30)

    welcome = tk.Label(frame1, text="Welcome", font=("Inter", 18, "normal"), bg="#D9D9D9",
                       fg="black", justify="left")
    welcome.place(x=15, y=175, width=190, height=30)

    button = tk.Button(frame1, text="Logout", font=("Inter", 12, "normal"), bg="#D9D9D9", fg="black", justify="left", command=lambda: logout_button())
    button.place(x=450, y=175, height=30)

    manageMembers = tk.Button(frame1, text="Manage Memberships", font=("Inter", 12, "normal"),
                              bg="#D9D9D9", fg="black", justify="left", command= lambda: manage_members_button())
    manageMembers.place(x=75, y=300, width=180, height=30)

    upload = tk.Button(frame1, text="Upload MT940 File", font=("Inter", 12, "normal"),
                       bg="#D9D9D9", fg="black", justify="left", command=lambda: upload_button_click())
    upload.place(x=300, y=300, width=180, height=30)

    searchBar = tk.Entry(frame1, font=("Inter", 14, "normal"), bg="#D9D9D9", fg="black", justify="left")
    searchBar.place(x=75, y=400, width=180, height=30)

    search = tk.Button(frame1, text="Search Keyword", font=("Inter", 12, "normal"),
                       bg="#D9D9D9", fg="black", justify="left", command=save_text)
    search.place(x=300, y=400, width=180, height=30)

    downloadJSONFile = tk.Button(frame1, text="Download Transactions in JSON", font=("Inter", 12, "normal"),
                                 bg="#D9D9D9", fg="black", justify="left", command=lambda: requests.get(api_server_ip + "/api/downloadJSON"))
    downloadJSONFile.place(x=35, y=500, width=250, height=30)

    downloadXMLFile = tk.Button(frame1, text="Download Transactions in XML", font=("Inter", 12, "normal"),
                                bg="#D9D9D9", fg="black", justify="left", command=lambda: requests.get(api_server_ip + "/api/downloadXML"))
    downloadXMLFile.place(x=300, y=500, width=250, height=30)

    balance_label = tk.Label(frame1, text="Available Balance:", font=("Inter", 15), bg="#D9D9D9", fg="#000000", justify="left")
    balance_label.place(x=35, y=600, width=160, height=24)

    balance_number = tk.Label(frame1, text=balance, font=("Inter", 15), bg="#D9D9D9", fg="#000000", justify="left")
    balance_number.place(x=210, y=600, width=160, height=24)

    # ---------------------------------------------------- Frame 2 --------------------------------------------------- #
    savedText = tk.Label(frame2, text="", font=("Inter", 14, "normal"), bg="#F0AFAF", fg="black",
                         justify="left")
    savedText.place(x=20, y=20, width=550, height=50)
    table = ttk.Treeview(frame2, columns=("ID", "Date", "Details", "Description", "Ref", "Amount"),
                         show="headings", style="Custom.Treeview")
    table.heading("ID", text="ID")
    table.heading("Date", text="Date")
    table.heading("Details", text="Company Name")
    table.heading("Description", text="Description")
    table.heading("Ref", text="Ref")
    table.heading("Amount", text="Amount")

    # Looping through the columns and get the heading
    for column in table["columns"]:
        # Assigning the heading as text of the column
        table.heading(column, text=column, command=lambda: None)

    # Apply the background color to the entire table
    style = ttk.Style()
    style.configure("Custom.Treeview", background="#F0AFAF", rowheight=60)

    table.column("ID", width=20)  # Set width of column zero
    table.column("Date", width=100)  # Set the width of the first column
    table.column("Details", width=200)  # Set the width of the second column
    table.column("Description", width=100)  # Set the width of the third column
    table.column("Ref", width=50)  # Set the width of the forth column
    table.column("Amount", width=100)  # Set the width of the fifth
    table.config(height=600)  # Set the height of the table to 10 rows

    rows = retrieveDB()

    # # Clear existing rows in the table
    table.delete(*table.get_children())

    # Insert retrieved data into the table
    for row in rows:
        table.insert("", "end", values=row)

    # Pack the table into the frame and center it horizontally
    table.pack(fill="both", expand=False)  # Fill the frame with the table
    table.place(x=15, y=100)  # Place the table 15 pixels from the left and 100 pixels from the top
    table.bind("<ButtonRelease-1>", on_click_table_row, "+") # Bind row selection
    frame2.pack_propagate(False)  # Prevent the frame from resizing to fit the table

    edit_button = ttk.Button(frame2, text="Edit", command=lambda: edit_button_click())
    edit_button.place(x=15, y=35, width=100, height=30)

    def on_closing():
        window.destroy()

    # Bind the on_closing function to the window close event
    window.protocol("WM_DELETE_WINDOW", on_closing)

    # Start the main event loop
    window.mainloop()
    # ------------------------------------------------------ Run ----------------------------------------------------- #
    window.mainloop()

# adminPanel()