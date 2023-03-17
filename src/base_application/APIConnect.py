import json
from tkinter import filedialog
import xml.etree.ElementTree as ET
import tkinter as tk
from flask import jsonify, request, make_response
from json2xml import json2xml

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


def downloadJSON():
    with app.app_context():
        # Get the data from the database
        try:
            data = get_all_transactions()
        except TypeError:
            data = []

        # Create a response object
        json_data = json_util.dumps(data, indent=4)
        response = make_response(json_data)
        response.headers['Content-Type'] = 'application/json'
        response.headers['Content-Disposition'] = 'attachment; filename=data.json'

    # Prompt the user to select a file path
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension='.json')

    # Write the data to the selected file path
    with open(file_path, 'w') as f:
        f.write(json_data)

    return response


def downloadXML():
    with app.app_context():
        # Get the data from the database
        try:
            data = get_all_transactions()
        except TypeError:
            data = []

        # Convert the data to a JSON string
        json_data = json_util.dumps(data)

        # Convert the JSON data to an ElementTree
        xml_root = ET.fromstring(json2xml.Json2xml(json.loads(json_data)).to_xml())

        # Prompt the user to select a file path
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename(defaultextension='.xml')

        # Write the XML data to the selected file path
        if file_path:
            with open(file_path, 'wb') as f:
                f.write(ET.tostring(xml_root))

        # Create a response with appropriate headers
        response = make_response()
        response.headers['Content-Type'] = 'application/xml'
        response.headers['Content-Disposition'] = 'attachment; filename=data.xml'

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
