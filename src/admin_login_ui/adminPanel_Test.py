# ----------------------------------------------------- Imports ------------------------------------------------------ #
import sqlite3
import tkinter as tk
from  tkinter import ttk

# ----------------------------------------------- Frames and Base Page ----------------------------------------------- #
window = tk.Tk()
window.geometry("1200x900")

window.resizable(False, False)

frame1 = tk.Frame(window, width=600, height=900, bg="#D9D9D9")
frame2 = tk.Frame(window, width=600, height=900, bg="#F0AFAF")

frame1.pack(side="left")
frame2.pack(side="right")


# ----------------------------------------------------- Functions ---------------------------------------------------- #
# def connect():

def save_text():
    global input_text
    input_text = searchBar.get()
    savedText.config(text="Search Results for: " + input_text)
    print("Saved:", input_text)


# ------------------------------------------------------ Frame 1 ----------------------------------------------------- #
label = tk.Label(frame1, text="Admin Panel", font=("Inter", 24, "normal"), bg="#D9D9D9", fg="black", justify="left")
label.place(x=20, y=20, width=190, height=50)

label.config(anchor="nw", pady=0, padx=0, wraplength=0, height=0, width=0)

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
                   bg="#D9D9D9", fg="black", justify="left", command=save_text)
search.place(x=300, y=400, width=180, height=30)

# ------------------------------------------------------ Frame 2 ----------------------------------------------------- #
savedText = tk.Label(frame2, text="", font=("Inter", 14, "normal"),  bg="#F0AFAF", fg="black",
                     justify="left")
savedText.place(x=20, y=20, width=550, height=50)







# -------------------------------------------------------- Run ------------------------------------------------------- #
window.mainloop()
