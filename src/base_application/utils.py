import json
import mt940;

def parse_mt940(file_path) ->  dict:
    # Parse the file
    statement = mt940.parse(file_path)
    # Convert the statement to a JSON string
    statement = json.dumps(statement, indent=4, sort_keys=True, cls=mt940.JSONEncoder)
    # Convert the JSON string to a dictionary
    statement = json.loads(statement)
    return statement




