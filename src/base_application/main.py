import asyncio
import threading
from src.base_application import app, api_server_ip
from adminPanel import adminPanel
# from registerPage import register_page


if __name__ == '__main__':
    # # Start Flask app in a new thread
    # flask_thread_api = threading.Thread(target=app.run())
    # flask_thread = threading.Thread(target=register_page())
    # flask_thread.start()
    # # Open register page
    # flask_thread_api.start()
    app.run()

    # Create an event loop
    # loop = asyncio.get_event_loop()
    # Run the Flask app and Tkinter GUI concurrently
    # tasks = [loop.create_task(flask_thread_api.start()), loop.create_task(flask_thread.start())]
    # loop.run_until_complete(asyncio.wait(tasks))



