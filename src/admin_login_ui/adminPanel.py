import sqlite3
import tkinter as tk


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
    welcome = tk.Label(frame1, text="Welcome", font=("Inter", 18, "normal"), bg="#D9D9D9",
                       fg="black", justify="left")
    welcome.place(x=40, y=50, width=190, height=50)

    # label.config(anchor="nw", pady=0, padx=0, wraplength=0, height=0, width=0)

    # association_name =



    window.mainloop()


adminPanel()
