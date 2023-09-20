from flask import Flask
import os
from dotenv import load_dotenv
from routes.index import blueprint
load_dotenv()
app= Flask(__name__)

app.register_blueprint(blueprint, url_prefix="/api/users")

if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)

