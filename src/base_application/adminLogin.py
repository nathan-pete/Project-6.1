import tkinter as tk
from adminPanel import adminPanel


def login_admin_page():
    # create the main window
    window = tk.Tk()
    window.geometry("1200x900")
    window.title("Sports Accounting - Register a user")

    window.resizable(False, False)

    def login_button_click(user, password):
        print(user, password)
        # Check credentials
        adminPanel()

    def back_button_click():
        window.destroy()


    # create two frames side by side
    frame1 = tk.Frame(window, width=600, height=900, bg="#D9D9D9")
    frame2 = tk.Frame(window, width=600, height=900, bg="#F0AFAF")

    frame1.pack(side="left")
    frame2.pack(side="right")

    # add a label to frame1 with the specified properties
    label = tk.Label(frame1, text="Admin Panel", font=("Inter", 24, "normal"), bg="#D9D9D9", fg="black", justify="left")
    label.place(x=20, y=20, width=190, height=50)

    # set the line height to 29 pixels and vertical alignment to top
    label.config(anchor="nw", pady=0, padx=0, wraplength=0, height=0, width=0)

    # add a label and text area to frame1 for Username
    user_label = tk.Label(frame1, text="Username", font=("Inter", 18, "normal"), bg="#D9D9D9", fg="black",
                          justify="left")
    user_label.place(x=20, y=300, width=123, height=24)
    user_entry = tk.Entry(frame1, font=("Inter", 18, "normal"), bg="white", fg="black", justify="left")
    user_entry.place(x=153, y=300, width=300, height=28)

    # add a label and text area to frame1 for Password
    pass_label = tk.Label(frame1, text="Password", font=("Inter", 18, "normal"), bg="#D9D9D9", fg="black",
                          justify="left")
    pass_label.place(x=20, y=350, width=123, height=24)
    pass_entry = tk.Entry(frame1, show="*", font=("Inter", 18, "normal"), bg="white", fg="black", justify="left")
    pass_entry.place(x=153, y=350, width=300, height=28)

    # add a login button to frame1
    login_button = tk.Button(frame1, text="Login", font=("Inter", 12), bg="white", fg="black",
                             bd=0, highlightthickness=0, activebackground="#B3B3B3",
                             command=lambda: login_button_click(user_entry.get(), pass_entry.get()))
    login_button.place(x=200, y=450, width=82, height=24)

    # add a back button to frame1
    back_button = tk.Button(frame1, text="Back", font=("Inter", 12), bg="white", fg="black",
                            bd=0, highlightthickness=0, activebackground="#B3B3B3",
                            command=back_button_click)
    back_button.place(x=20, y=700, width=82, height=24)

    # run the main loop
    window.mainloop()