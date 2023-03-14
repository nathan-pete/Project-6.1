import sqlite3
import tkinter as tk

from pip._internal.cli.cmdoptions import src


def adminPanel():
    def retrieveDB(table):
        conn = sqlite3.connect('quintor.db')
        cursor = conn.cursor()
        cursor.execute("")
        rows = cursor.fetchall()
        conn.close()

    # create the main window
    window = tk.Tk()
    window.geometry("1200x900")

    window.resizable(False, False)

    # create two frames side by side
    frame1 = tk.Frame(window, width=600, height=900, bg="#D9D9D9")
    frame2 = tk.Frame(window, width=600, height=900, bg="#F0AFAF")

    frame1.pack(side="left")
    frame2.pack(side="right")

    # add a label to frame1 with the specified properties
    label = tk.Label(frame1, text="Admin Panel", font=("Inter", 24, "normal"), bg="#D9D9D9", fg="black", justify="left")
    label.place(x=20, y=20, width=190, height=50)

    label.config(anchor="nw", pady=0, padx=0, wraplength=0, height=0, width=0)

    # association_name =

    line = tk.Label(frame1, text="_______________________________________________________",
                    font=("Inter", 18, "normal"), bg="#D9D9D9", fg="black", justify="left")
    line.place(x=61, y=180, width=450, height=30)

    welcome = tk.Label(frame1, text="Welcome", font=("Inter", 18, "normal"), bg="#D9D9D9",
                       fg="black", justify="left")
    welcome.place(x=15, y=175, width=190, height=30)

    button = tk.Button(frame1, text="Logout", font=("Inter", 12, "normal"), bg="#D9D9D9", fg="black", justify="left")
    button.place(x=450, y=175, height=30)

    manageMembers = tk.Button(frame1, text="Manage Memberships", font=("Inter", 12, "normal"),
                              bg="#D9D9D9", fg="black", justify="left")
    manageMembers.place(x=75, y=300, width=180, height=30)

    upload = tk.Button(frame1, text="Upload MT940 File", font=("Inter", 12, "normal"),
                       bg="#D9D9D9", fg="black", justify="left")
    upload.place(x=300, y=300, width=180, height=30)

    searchBar = tk.Entry(frame1, font=("Inter", 14, "normal"), bg="#D9D9D9", fg="black", justify="left")
    searchBar.place(x=75, y=400, width=180, height=30)

    search = tk.Button(frame1, text="Search Keyword", font=("Inter", 12, "normal"),
                       bg="#D9D9D9", fg="black", justify="left")
    search.place(x=300, y=400, width=180, height=30)

    # **Help linking buttons to functions**
    #
    # manageMembers = tk.Button(frame1, text="Manage Members", font=("Inter", 12, "normal"),
    #                           command=frame1.clickmanageMembers, bg="#D9D9D9", fg="black", justify="left")
    # manageMembers.place(x=50, y=300)
    #
    # def clickmanageMembers():
    #     print("clicked")

    # class Table:
    #
    #     def __init__(frame2, total_rows, total_columns, lst):
    #
    #         # code for creating table
    #         for i in range(total_rows):
    #             for j in range(total_columns):
    #                 frame2.e = tk.Entry(total_columns, width=20, fg='blue',
    #                                     font=('Inter', 14, 'bold'))
    #
    #                 frame2.e.grid(row=i, column=j)
    #                 frame2.e.insert(tk.END, lst[i][j])
    #
    #     total_rows = len(lst)
    #     total_columns = len(lst[0])
    #
    window.mainloop()


adminPanel()
