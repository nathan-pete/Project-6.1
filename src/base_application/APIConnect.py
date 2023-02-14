import json

from flask import app, jsonify, request, make_response
from utils import parse_mt940_file
from bson import json_util, ObjectId


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
def testAPI():
    file_path = "C:\University\Semester_2\Project6.1\Project-6.1_Code\src\resources\mt940Example.txt"
    transaction = parse_mt940_file(file_path)
    return make_response(json.loads(json_util.dumps(transaction)),200)


