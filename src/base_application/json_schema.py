import json
import jsonschema

schema = {
    "type": "object",
    "properties": {
        "account_identification": {
            "type": "string"
        },
        "available_balance": {
            "type": "object",
            "properties": {
                "amount": {
                    "type": "object",
                    "properties": {
                        "amount": {
                            "type": "string"
                        },
                        "currency": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "amount",
                        "currency"
                    ]
                },
                "date": {
                    "type": "string"
                },
                "status": {
                    "type": "string"
                }
            },
            "required": [
                "amount",
                "date",
                "status"
            ]
        },
        "final_closing_balance": {
            "type": "object",
            "properties": {
                "amount": {
                    "type": "object",
                    "properties": {
                        "amount": {
                            "type": "string"
                        },
                        "currency": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "amount",
                        "currency"
                    ]
                },
                "date": {
                    "type": "string"
                },
                "status": {
                    "type": "string"
                }
            },
            "required": [
                "amount",
                "date",
                "status"
            ]
        },
        "final_opening_balance": {
            "type": "object",
            "properties": {
                "amount": {
                    "type": "object",
                    "properties": {
                        "amount": {
                            "type": "string"
                        },
                        "currency": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "amount",
                        "currency"
                    ]
                },
                "date": {
                    "type": "string"
                },
                "status": {
                    "type": "string"
                }
            },
            "required": [
                "amount",
                "date",
                "status"
            ]
        },
        "forward_available_balance": {
            "type": "object",
            "properties": {
                "amount": {
                    "type": "object",
                    "properties": {
                        "amount": {
                            "type": "string"
                        },
                        "currency": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "amount",
                        "currency"
                    ]
                },
                "date": {
                    "type": "string"
                },
                "status": {
                    "type": "string"
                }
            },
            "required": [
                "amount",
                "date",
                "status"
            ]
        },
        "sequence_number": {
            "type": "null"
        },
        "statement_number": {
            "type": "string"
        },
        "transaction_reference": {
            "type": "string"
        },
        "transactions": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "amount": {
                            "type": "object",
                            "properties": {
                                "amount": {
                                    "type": "string"
                                },
                                "currency": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "amount",
                                "currency"
                            ]
                        },
                        "bank_reference": {
                            "type": "string"
                        },
                        "currency": {
                            "type": "string"
                        },
                        "customer_reference": {
                            "type": "string"
                        },
                        "date": {
                            "type": "string"
                        },
                        "entry_date": {
                            "type": "string"
                        },
                        "extra_details": {
                            "type": "string"
                        },
                        "funds_code": {
                            "type": "null"
                        },
                        "guessed_entry_date": {
                            "type": "string"
                        },
                        "id": {
                            "type": "string"
                        },
                        "status": {
                            "type": "string"
                        },
                        "transaction_details": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "amount",
                        "bank_reference",
                        "currency",
                        "customer_reference",
                        "date",
                        "entry_date",
                        "extra_details",
                        "funds_code",
                        "guessed_entry_date",
                        "id",
                        "status",
                        "transaction_details"
                    ]
                }
            ]
        }
    },
    "required": [
        "account_identification",
        "available_balance",
        "final_closing_balance",
        "final_opening_balance",
        "forward_available_balance",
        "sequence_number",
        "statement_number",
        "transaction_reference",
        "transactions"
    ]

}

# Load the MT940 file as a JSON object
with open('C:/Users/Omen/IdeaProjects/pr1/venv/json_1.json.') as json_file:
    mt940_json = json.load(json_file)

try:
    jsonschema.validate(mt940_json, schema)
    print("MT940 file is valid.")
except jsonschema.exceptions.ValidationError as e:
    print("MT940 file is not valid. Validation error: ")
    print(e)
