import threading
from src.base_application import app
from adminPanel import adminPanel
# from registerPage import register_page


if __name__ == '__main__':
    # # Start Flask app in a new thread
    # flask_thread = threading.Thread(target=adminPanel())
    # flask_thread.start()
    # # Open register page
    # flask_thread_api = threading.Thread(target=app.run())
    # flask_thread_api.start()
    app.run()
