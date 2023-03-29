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
json_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "$id": "quintor_schema",
    "title": "MT940 JSON Schema",
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
                    }
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
    ]
}


with open("C:/University/Semester_2/Project6.1/Project-6.1_Code/src/resources/mt940Example.json", 'r') as f:
    mt940_data = json.load(f)

print(mt940_data)
print(json_schema)

if jsonschema.validate(instance=mt940_data, schema=json_schema):
    print(1)

if not jsonschema.validate(instance=mt940_data, schema=json_schema):
    print(0)



