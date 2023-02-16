import json
import mt940

def parse_mt940_file(file_path) -> dict:
    # Parse the contents of the MT940 file
    transactions = mt940.parse(file_path)

    # Convert the parsed transactions to a JSON string
    transactions = json.dumps(transactions, indent=4, sort_keys=True, cls=mt940.JSONEncoder)

    # Load the JSON string as a dictionary
    transactions = json.loads(transactions)

    # Return the dictionary containing the parsed transactions
    return transactions


def check_mt940_file():
    return 1

