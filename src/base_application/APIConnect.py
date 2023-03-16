import json
from tkinter import filedialog

import tkinter as tk
from flask import jsonify, request, make_response
from utils import parse_mt940_file, check_mt940_file

from bson import json_util, ObjectId
# Get instances of Flask App and MongoDB collection from dataBaseConnectionPyMongo file
from src.base_application import app, transactions_collection
from bson.json_util import dumps as json_util_dumps



@app.route("/")
def index():
    answer = {
        "message": "Welcome to Sports Accounting API",
        "api": {
            "test": "/api/test",
            "getTransactionsAmount": "/api/getTransactionsCount",
            "getTransactions": "/api/getTransactions",
            "uploadMT940File": "/api/uploadFile",
            "searchKeywordSQL": "/api/searchKeyword/<keyword>",
            "insertAssociationSQL": "/api/insertAssociation",
            "insertFileSQL": "/api/insertFile",
            "insertTransactionSQL": "/api/insertTransaction",
            "insertMemberSQL": "/api/insertMemberSQL",
            "updateTransactionSQL": "/api/updateTransactionSQL/<transaction_id>",
            "deleteMemberSQL": "/api/deleteMember/<member_id>",

        }
    }
    return make_response(jsonify(answer), 200)


@app.route("/api/test")
def test():
    # file_path = "C:/University/Semester_2/Project6.1/Project-6.1_Code/src/resources/mt940Example.txt"
    # transaction = parse_mt940_file(file_path)
    # transactions_collection.insert_one(transaction)
    # return make_response(json.loads(json_util.dumps(transaction)), 200)
    return make_response(jsonify("API works fine!"))
    # return make_response("API works fine - Test")


@app.route("/api/getTransactionsCount", methods=["GET"])
def get_transactions_count():
    output = {"transactionsCount": transactions_collection.count_documents({})}
    return output


def download():
    with app.app_context():
        # Get the data from the database
        try:
            data = get_all_transactions()
        except TypeError:
            data = []

        # Create a response object
        response = make_response(json_util_dumps(data))
        response.headers['Content-Type'] = 'application/json'
        response.headers['Content-Disposition'] = 'attachment; filename=data.json'

    # Extract the data from the response
    data = response.get_data()

    # Prompt the user to select a file path
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension='.json')

    # Write the data to the selected file path
    with open(file_path, 'w') as f:
        f.write(data.decode('utf-8'))

    return response


@app.route("/api/getTransactions", methods=["GET"])
def get_all_transactions():
    output_transactions = []

    for trans in transactions_collection.find():
        print(trans)
        output_transactions.append(trans)

    return output_transactions


# Send a POST request with the file path to this function
@app.route("/api/uploadFile", methods=["POST"])
def file_upload():
    # Grab the file path from the post request sent to this function of API
    file_path = request.form.get('file_path')

    if not check_mt940_file(file_path):
        return make_response(jsonify(error="File is not correct format. Unprocessable Entity"), 422)

    # Insert into No SQL Db
    transaction = parse_mt940_file(file_path)
    transactions_collection.insert_one(transaction)

    return make_response(jsonify(status="File uploaded!"), 200)
