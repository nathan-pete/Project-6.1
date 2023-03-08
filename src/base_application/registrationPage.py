import tkinter as tk
from tkinter import ttk
from tkinter import *
# Create the main window
root = tk.Tk()
root.title("Register a user")
root.geometry("1200x900")
# Create a frame to hold the left section

left_frame = tk.Frame(root, bg="#D9D9D9") # Set the background color to grey
left_frame.pack(side="left", fill="both", expand=True)


# Create a frame to hold the right section
right_frame = tk.Frame(root, bg="#F0AFAF") # Set the background color to pink
right_frame.pack(side="right", fill="both", expand=True, padx=(0, 5))  # Add padding to prevent overlap

#Headings
heading1 = tk.Label(left_frame, text="New user registration", font=("Roboto", 28), bg="#D9D9D9", fg="#000000",
                    justify="center")
heading1.place(x=85, y=100, width=350, height=50)

heading2 = tk.Label(left_frame, text="Before we continue let's make an account", font=("Roboto", 14), bg="#D9D9D9", fg="#000000",
                    justify="center")
heading2.place(x=25, y=160, width=500, height=50)

#Inputs for the registration
#assoc name
assoc_name = tk.Entry(left_frame)
assoc_name.place(x=160, y=300, width=300, height=30)
assoc_name.insert(0, "association name")

#password
passwd = tk.Entry(left_frame)
passwd.place(x=160, y=345, width=300, height=22)
passwd.insert(0, "password")

#IBAN
iban = tk.Entry(left_frame)
iban.place(x=160, y=390, width=300, height=30)
iban.insert(0, "iban")

button1 = ttk.Button(left_frame, text="Sign up")

button1.place(x=140, y=500, width=300, height=60)



# Start the main event loop
root.mainloop()

