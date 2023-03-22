import json
import jsonschema

schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "header": {
            "type": "object",
            "properties": {
                "sender": {"type": "string"},
                "receiver": {"type": "string"},
                "message_type": {"type": "string", "pattern": "^940$"},
                "message_date": {"type": "string", "format": "date"},
                "message_time": {"type": "string", "format": "time"},
                "reference": {"type": "string"}
            },
            "required": ["sender", "receiver", "message_type", "message_date"]
        },

        "transactions": {
            "transaction_reference": {"type": "string"},
            "account_identification": {"type": "string"},
            "statement_number": {"type": "string"},
            "final_opening_balance": {"type": "object", "properties": {"amount": {"type": "number"},
                                                                       "date": {"type": "string", "format": "date"}}},
            "final_closing_balance": {"type": "object", "properties": {"amount": {"type": "number"},
                                                                       "date": {"type": "string", "format": "date"}}},
            "transaction_details": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string", "format": "date"},
                        "entry_date": {"type": "string", "format": "date"},
                        "transaction_reference_number": {"type": "string"},
                        "amount": {"type": "number"},
                        "currency": {"type": "string", "pattern": "^[A-Z]{3}$"},
                        "transaction_type": {"type": "string", "pattern": "^[A-Z]{3}$"},
                        "transaction_details": {"type": "string"},
                    },
                    "required": ["transaction_date", "amount", "currency"]
                }
            }
        },
        "required": ["account_identification", "opening_balance", "closing_balance", "transactions"]

    },
    "required": ["transactions"]
}

with open('C:/Users/Omen/IdeaProjects/pr1/venv/json_1.json.') as json_file:
    mt940_json = json.load(json_file)

try:
    jsonschema.validate(mt940_json, schema)
    print("MT940 file is valid.")
except jsonschema.exceptions.ValidationError as e:
    print("MT940 file is not valid. Validation error: ")
    print(e)
