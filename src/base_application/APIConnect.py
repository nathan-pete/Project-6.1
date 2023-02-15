import json

from flask import jsonify, request, make_response
from utils import parse_mt940_file
from bson import json_util, ObjectId
# Get instances of Flask App and MongoDB collection from __init__ file
from src.base_application import app, transactions_collection


@app.route("/")
def index():
    answer = {
        "message": "Welcome to Sports Accounting API",
        "api": {
            "test": "/api/test",
            "getTransactionsAmount": "/api/getTransactionsCount",
            "getTransactions": "/api/getTransactions",
            "getTransaction": "/api/getTransaction/<transaction_id>",
            "searchKeyword": "/api/searchKeyword/<keyword>",
            "uploadMT940File": "/api/uploadFile"
        }
    }
    return make_response(jsonify(answer), 200)


@app.route("/api/test")
def test():
    file_path = "C:/University/Semester_2/Project6.1/Project-6.1_Code/src/resources/mt940Example.txt"
    transaction = parse_mt940_file(file_path)
    transactions_collection.insert_one(transaction)
    return make_response(json.loads(json_util.dumps(transaction)), 200)


@app.route("/api/getTransactionsCount", methods=["GET"])
def get_transactions_count():
    output = {"transactionsCount": transactions_collection.count_documents({})}
    return output


@app.route("/api/getTransactions", methods=["GET"])
def get_all_transactions():
    output_transactions = []

    for trans in transactions_collection.find():
        print(trans)
        output_transactions.append(trans)

    return make_response(json.loads(json_util.dumps(output_transactions)), 200)
