import sys
import mt940
import json
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
        file_path = filedialog.askopenfilename(defaultextension=".sta", filetypes=[("MT940 Files", "*.sta"), ("All Files", "*.*")])
        self.selected_file_label.config(text=file_path)
        self.file_path = file_path

    def parse_file(self):
        """Parse the selected MT940 file and save the result as a JSON file."""
        # Check MT940 file
        if check_mt940_file(self.file_path):
            # Save to NoSQL DB
            url = api_server_ip + '/api/uploadFile'
            payload = {'file_path': self.file_path}
            response = requests.post(url, data=payload)
            print(response.text)

            # Save to SQL DB FILE
            payload = get_json_payload_mt940_file(self.file_path)
            reference = payload["referencenumber"]
            url = api_server_ip + '/api/insertFile/' + str(payload["referencenumber"]) + "/" + str(payload["statementnumber"]) + "/" + str(payload["sequencedetail"]) + "/" + str(payload["availablebalance"]) + "/" + str(payload["forwardavbalance"]) + "/" + str(payload["accountid"])
            response = requests.get(url)
            print(response.text)

            # Save to SQL DB Transaction
            json_trans = parse_mt940_file(self.file_path)
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



# TEmp code
# payload = get_json_payload_transaction(trans)
# payload.update(referencenumber=reference)
# url = api_server_ip + '/api/insertTransaction/' + str(payload["referencenumber"]) + "/" + str(payload["amount"]) + "/" + str(payload["currency"]) + "/" + str(payload["transaction_date"]) + "/" + str(payload["transaction_details"]) + "/" + str(payload["description"]) + "/" + str(payload["typetransaction"])
# response_trans = requests.get(url)
# print(response_trans.text)
