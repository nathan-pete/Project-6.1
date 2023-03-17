from dataBaseConnectionPyMongo import get_database, get_collection, get_flask_app, get_connection_postgre

app = get_flask_app()
transactions_collection = get_collection()
postgre_connection = get_connection_postgre()
api_server_ip = "http://127.0.0.1:5000"

from src.base_application import APIConnect  # Import API