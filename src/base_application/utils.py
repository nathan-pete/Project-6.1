import hashlib
import json
import jsonschema
import mt940
import re
from lxml import etree
import os
# Make a regular expression for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
xml_schema_path = os.path.join(os.path.dirname(__file__), 'xmlSchema.xsd')
json_schema_path = os.path.join(os.path.dirname(__file__), 'mt940_schema.json')

def parse_mt940_file(file_path) -> dict:
    # Parse the contents of the MT940 file
    transactions = mt940.parse(file_path)

    # Convert the parsed transactions to a JSON string
    transactions = json.dumps(transactions, indent=4, sort_keys=True, cls=mt940.JSONEncoder)

    # Load the JSON string as a dictionary
    transactions = json.loads(transactions)

    # Return the dictionary containing the parsed transactions
    return transactions


def check_mt940_file(file_path):
    if check_tag(file_path) and check_file_extension(file_path):
        return True
    else:
        return False


def check_tag(file_path):
    tag_20 = ':20:'
    tag_25 = ':25:'
    tag_28c = ':28C:'
    tag_60 = ':60F:'
    tag_62 = ':62F:'
    tags = [':20:', ':25:', ':28C:', ':60F:', ':62F:']
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if all the strings from tag array are present in the file
        if all(tag in content for tag in tags):
            isTag = True
        else:
            isTag = False
        if tag_20 not in content:
            print("Transaction Reference Number( tag 20 ) is missing")
        if tag_25 not in content:
            print("Account Identification ( tag 25 ) is missing")
        if tag_28c not in content:
            print("Statement number( tag 28C )  is missing")
        if tag_60 not in content:
            print("Opening Balance (tag 60F )is missing")
        if tag_62 not in content:
            print("Closing balance ( tag 62F ) is missing")
    return isTag


def check_file_extension(file_path):
    # check if the file name ends with .sta
    if file_path.endswith('.sta'):
        return True
    else:
        return False


def hash_password(password):
    # Convert the password string to bytes and hash it using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


def check_email(email):
    # pass the regular expression and the string into the fullmatch() method
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def get_json_payload_mt940_file(file_path):
    json_transactions = parse_mt940_file(file_path)

    # Extract values from a JSON into variables for the File table
    reference_number = json_transactions["transaction_reference"]
    statement_number = json_transactions["statement_number"]
    sequence_detail = json_transactions["sequence_number"]
    available_balance = json_transactions["available_balance"]["amount"]["amount"]
    forward_available_balance = json_transactions["forward_available_balance"]["amount"]["amount"]
    account_identification = json_transactions["account_identification"]
    # Extract values from a JSON into variables for the Transaction table

    payload = {'referencenumber': reference_number, 'statementnumber': statement_number, 'sequencedetail': sequence_detail, 'availablebalance': available_balance,
               'forwardavbalance': forward_available_balance, 'accountid': account_identification}

    return payload


def get_json_payload_transaction(trans_set):
    amount = trans_set["amount"]["amount"]
    currency = trans_set["amount"]["currency"]
    transaction_date = trans_set["date"]
    transaction_details = str(trans_set["transaction_details"])
    transaction_details = transaction_details.replace("/", "-")
    description = None
    typetransaction = trans_set["status"]

    payload = {"amount": amount, "currency": currency, "transaction_date": transaction_date,
               "transaction_details": transaction_details, "description": description, "typetransaction": typetransaction}

    return payload


def validate_xml(xml_file):
    with open(xml_schema_path, 'r') as f:
        xsd = etree.parse(f)

    with open(xml_file, 'r') as f:
        xml = etree.parse(f)

    schema = etree.XMLSchema(xsd)

    is_valid = schema.validate(xml)

    return is_valid


def validate_json(json_inp):
    try:
        with open(json_schema_path) as r:
            schema = json.load(r)
        jsonschema.validate(json_inp, schema)
        return True
    except (Exception, jsonschema.ValidationError) as error:
        return False



