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
    window = tk.Tk()
    window.geometry("1200x900")
    window.title("Sports Accounting - Admin Panel")

    window.resizable(False, False)

    frame1 = tk.Frame(window, width=600, height=900, bg="#D9D9D9")
    frame2 = tk.Frame(window, width=600, height=900, bg="#F0AFAF")

    frame1.pack(side="left")
    frame2.pack(side="right")

    # --------------------------------------------------- Functions -------------------------------------------------- #
    def save_text():
        global input_text
        input_text = searchBar.get()
        savedText.config(text="Search Results for: " + input_text)
        print("Saved:", input_text)

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

    def manage_members_button():
        manage_members()
        window.destroy()

    def upload_button_click():
        main()

    def logout_button():
        # create_window()
        window.destroy()

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

    # ---------------------------------------------------- Frame 2 --------------------------------------------------- #
    savedText = tk.Label(frame2, text="", font=("Inter", 14, "normal"), bg="#F0AFAF", fg="black",
                         justify="left")
    savedText.place(x=20, y=20, width=550, height=50)

    table = ttk.Treeview(frame2, columns=("Member ID", "Name", "DoB", "Contact", "Member Since", "Paid"),
                         show="headings", style="Custom.Treeview")
    table.heading("Member ID", text="Member ID")
    table.heading("Name", text="Name")
    table.heading("DoB", text="DoB")
    table.heading("Contact", text="Contact")
    table.heading("Member Since", text="Member Since")
    table.heading("Paid", text="Paid")

    for column in table["columns"]:
        table.heading(column, text=column, command=lambda: None)
        table.bind("<Button-1>", lambda event: "break")

        retrieveDB(table)

    table.column("Member ID", width=100)
    table.column("Name", width=100)
    table.column("DoB", width=50)
    table.column("Contact", width=100)
    table.column("Member Since", width=100)
    table.column("Paid", width=50)
    table.config(height=2)

    table.pack(fill="both", expand=False)
    table.place(x=50, y=150)
    frame2.pack_propagate(False)
    # ------------------------------------------------------ Run ----------------------------------------------------- #
    window.mainloop()
# #
adminPanel()