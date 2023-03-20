import json
from tkinter import filedialog
import xml.etree.ElementTree as ET
import xml.dom.minidom
import tkinter as tk
import psycopg2
from flask import jsonify, request, make_response
from json2xml import json2xml
from utils import parse_mt940_file, check_mt940_file, check_email
from bson import json_util, ObjectId
from bson.json_util import dumps as json_util_dumps

# Get instances of Flask App and MongoDB collection from dataBaseConnectionPyMongo file
from src.base_application import app, transactions_collection, postgre_connection


@app.route("/")
def index():
    answer = {
        "message": "Welcome to Sports Accounting API",
        "api": {
            "test": "/api/test",
            "getTransactionsAmount": "/api/getTransactionsCount",
            "getTransactions": "/api/getTransactions",
            "uploadMT940File": "/api/uploadFile",
            "downloadJSON": "/api/downloadJSON",
            "downloadXML": "/api/downloadXML",
            "searchKeywordSQL": "/api/searchKeyword/<keyword>",
            "insertAssociationSQL": "/api/insertAssociation",
            "insertFileSQL": "/api/insertFile",
            "insertTransactionSQL": "/api/insertTransaction",
            "insertMemberSQL": "/api/insertMemberSQL/<name>/<email>",
            "updateTransactionSQL": "/api/updateTransactionSQL/<transaction_id>",
            "deleteMemberSQL": "/api/deleteMember/<member_id>",
            "getAssociationSQL": "/api/getAssociation"


        }
    }
    return make_response(jsonify(answer), 200)

# ----------------------- No SQL MongoDB functions of the API ---------------------------------


@app.route("/api/test")
def test():
    return make_response(jsonify("API works fine!"))


@app.route("/api/getTransactionsCount", methods=["GET"])
def get_transactions_count():
    output = {"transactionsCount": transactions_collection.count_documents({})}
    return output


@app.route("/api/downloadJSON", methods=["GET"])
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


@app.route("/api/downloadXML", methods=["GET"])
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
            xml_string = ET.tostring(xml_root, encoding='utf-8', method='xml')
            xml_string_pretty = xml.dom.minidom.parseString(xml_string).toprettyxml()
            with open(file_path, 'wb') as f:
                f.write(xml_string_pretty.encode('utf-8'))

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


# -------------------------- SQL PostGreSQL DB functions of the API ---------------------------
@app.route("/api/deleteMember/<member_id>", methods=["GET"])
def delete_member(member_id):
    try:
        cursor = postgre_connection.cursor()

        # call a stored procedure
        cursor.execute('CALL delete_member(%s)', member_id)

        # commit the transaction
        postgre_connection.commit()

        # close the cursor
        cursor.close()

        return make_response(jsonify(status="Member Removed"), 200)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if postgre_connection is not None:
            postgre_connection.close()


# The function receives a hashed password
@app.route("/api/insertAssociation", methods=["POST"])
def insert_association():
    try:
        accountID = request.form.get('accountID')
        name = request.form.get('name')
        hashed_password = request.form.get('password')

        cursor = postgre_connection.cursor()

        # call a stored procedure
        cursor.execute('CALL insert_into_association(%s,%s,%s)', (accountID, name, hashed_password))

        # commit the transaction
        postgre_connection.commit()

        # close the cursor
        cursor.close()

        return make_response(jsonify(status="Data inserted!"), 200)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


# @app.route("/api/getAssociation", methods=["GET"])
# def getAssociation():
#     try:
#         cursor = postgre_connection.cursor()
#
#         # Call a stored procedure
#         cursor.callproc("get_association")
#         # Get the output
#         output = cursor.fetchall()
#
#         cursor.close()
#
#         # Return the results as JSON
#         return make_response(jsonify(output), 200)
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if postgre_connection is not None:
#             postgre_connection.close()


@app.route("/api/insertMemberSQL/<name>/<email>", methods=["GET"])
def insert_member(name, email):
    try:
        cursor = postgre_connection.cursor()

        # call a stored procedure
        cursor.execute('CALL insert_into_member(%s,%s)', (name, email))

        # commit the transaction
        postgre_connection.commit()

        # close the cursor
        cursor.close()

        return make_response(jsonify(status="Data inserted!"), 200)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if postgre_connection is not None:
            postgre_connection.close()

@app.route("/api/getAssociation", methods=["GET"])
def get_association():
    try:
        cursor = postgre_connection.cursor()

        # call a stored procedure
        cursor.execute('SELECT * FROM association')

        # Get all data from the stored procedure
        data = cursor.fetchall()

        # Return data in JSON format
        # return make_response(jsonify(response), 200)
        return jsonify(data)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if postgre_connection is not None:
            postgre_connection.close()





