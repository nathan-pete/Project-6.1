import sys
import mt940
import json
from utils import parse_mt940_file, check_tag, check_file_extension
from tkinter import Tk, filedialog
from tkinter.ttk import Button, Label
from dataBaseConnectionPyMongo import get_database, get_collection

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Sports Accounting - MT940 Parser")

        # Create the "Select File" button
        self.select_file_button = Button(self.master, text="Select File", command=self.select_file)
        self.select_file_button.pack()

        # Create the label to display the selected file name
        self.selected_file_label = Label(self.master, text="")
        self.selected_file_label.pack()

        # Create the "Parse" button
        self.parse_button = Button(self.master, text="Parse", command=self.parse_file)
        self.parse_button.pack()

    def select_file(self):
        """Open a file dialog to select an MT940 file."""
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("MT940 Files", "*.txt"), ("All Files", "*.*")])
        self.selected_file_label.config(text=file_path)
        self.file_path = file_path

    def parse_file(self):
        """Parse the selected MT940 file and save the result as a JSON file."""
        # Check MT940 file
        if check_file_extension(self.file_path):
            # Check DataBase
            transactions_collection = get_collection()
            transactions_collection.insert_one(parse_mt940_file(self.file_path))
        # Close Window
        sys.exit()

def main():
    root = Tk()
    root.geometry("400x200")
    MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
