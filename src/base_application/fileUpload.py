from utils import parse_mt940_file, check_mt940_file, get_json_payload_mt940_file, get_json_payload_transaction
from tkinter import Tk, filedialog
from tkinter.ttk import Button, Label
import requests
from src.base_application import api_server_ip

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Sports Accounting - MT940 Parser")
        self.master.wm_attributes("-topmost", 1)

        # Create the "Select Files" button
        self.select_files_button = Button(self.master, text="Select Files", command=self.select_files)
        self.select_files_button.pack()

        # Create the label to display the selected files
        self.selected_files_label = Label(self.master, text="")
        self.selected_files_label.pack()

        # Create the "Parse" button
        self.parse_button = Button(self.master, text="Parse", command=self.parse_files)
        self.parse_button.pack()

        # Initialize list of file paths
        self.file_paths = []

    def select_files(self):
        """Open a file dialog to select MT940 files."""
        file_paths = filedialog.askopenfilenames(defaultextension=".sta", filetypes=[("MT940 Files", "*.sta"), ("All Files", "*.*")])
        self.selected_files_label.config(text="Selected Files: " + str(file_paths))
        self.file_paths = file_paths

    def parse_files(self):
        """Parse the selected MT940 files and save the results as JSON files."""
        for file_path in self.file_paths:
            # Check MT940 file
            if check_mt940_file(file_path):
                # Save to NoSQL DB
                url = api_server_ip + '/api/uploadFile'
                payload = {'file_path': file_path}
                response = requests.post(url, data=payload)

                # Save to SQL DB FILE
                payload = get_json_payload_mt940_file(file_path)
                reference = payload["referencenumber"]
                url = api_server_ip + '/api/insertFile/' + str(payload["referencenumber"]) + "/" + str(payload["statementnumber"]) + "/" + str(payload["sequencedetail"]) + "/" + str(payload["availablebalance"]) + "/" + str(payload["forwardavbalance"]) + "/" + str(payload["accountid"])
                response = requests.get(url)

                # Save to SQL DB Transaction
                json_trans = parse_mt940_file(file_path)
                for trans in json_trans["transactions"]:
                    url = api_server_ip + '/api/insertTransaction'
                    payload = get_json_payload_transaction(trans)
                    payload.update(referencenumber = reference)
                    response = requests.post(url, data=payload)

        # Close Window
        self.master.destroy()

def main():
    root = Tk()
    root.geometry("400x200")
    MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
