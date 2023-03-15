import json
from flask import jsonify, request, make_response
from utils import parse_mt940_file, check_mt940_file
from bson import json_util, ObjectId
# Get instances of Flask App and MongoDB collection from dataBaseConnectionPyMongo file
from src.base_application import app, transactions_collection
from bson import ObjectId
import requests


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
            "uploadMT940File": "/api/uploadFile",
            "getFileFromDB": "/api/getFileBack"
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


@app.route("/api/getTransactions", methods=["GET"])
def get_all_transactions():
    output_transactions = []

    for trans in transactions_collection.find():
        print(trans)
        output_transactions.append(trans)

    return make_response(json.loads(json_util.dumps(output_transactions)), 200)


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
