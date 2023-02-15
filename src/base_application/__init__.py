from dataBaseConnectionPyMongo import get_database, get_collection, get_flask_app

app = get_flask_app()
transactions_collection = get_collection()

from src.base_application import APIConnect  # Import API
