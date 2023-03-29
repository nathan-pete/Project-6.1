import jsonschema
import json

# Define the JSON schema
schema = {
    "type": "object",
    "properties": {
        "account_identification": {"type": "string"},
        "available_balance": {
            "type": "object",
            "properties": {
                "amount": {
                    "type": "object",
                    "properties": {
                        "amount": {"type": "string"},
                        "currency": {"type": "string"}
                    }
                },
                "date": {"type": "string"},
                "status": {"type": "string"}
            }
        },
        "final_closing_balance": {
            "type": "object",
            "properties": {
                "amount": {
                    "type": "object",
                    "properties": {
                        "amount": {"type": "string"},
                        "currency": {"type": "string"}
                    }
                },
                "date": {"type": "string"},
                "status": {"type": "string"}
            }
        },
        "final_opening_balance": {
            "type": "object",
            "properties": {
                "amount": {
                    "type": "object",
                    "properties": {
                        "amount": {"type": "string"},
                        "currency": {"type": "string"}
                    }
                },
                "date": {"type": "string"},
                "status": {"type": "string"}
            }
        },
        "forward_available_balance": {
            "type": "object",
            "properties": {
                "amount": {
                    "type": "object",
                    "properties": {
                        "amount": {"type": "string"},
                        "currency": {"type": "string"}
                    }
                },
                "date": {"type": "string"},
                "status": {"type": "string"}
            }
        },
        "sequence_number": {"type": ["string", "null"]},
        "statement_number": {"type": "string"},
        "transaction_reference": {"type": "string"},
        "transactions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "amount": {
                        "type": "object",
                        "properties": {
                            "amount": {"type": "string"},
                            "currency": {"type": "string"}
                        }
                    },
                    "bank_reference": {"type": "string"},
                    "currency": {"type": "string"},
                    "customer_reference": {"type": "string"},
                    "date": {"type": "string"},
                    "entry_date": {"type": "string"},
                    "extra_details": {"type": "string"},
                    "funds_code": {"type": ["string", "null"]},
                    "guessed_entry_date": {"type": "string"},
                    "id": {"type": "string"},
                    "status": {"type": "string"},
                    "transaction_details": {"type": "string"}
                },
                "required": ["amount", "bank_reference", "currency", "date", "entry_date", "id", "status",
                             "transaction_details"]
            }
        }
    },
    "required": ["account_identification", "available_balance", "final_closing_balance", "final_opening_balance",
                 "forward_available_balance", "statement_number", "transaction_reference", "transactions"]
}
