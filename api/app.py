from flask import Flask
from flask_cors import CORS
from routes.index import blueprint

app= Flask(__name__)
CORS(app)
app.register_blueprint(blueprint, url_prefix="/api/users")

@app.route('/health')
def hello_world():
   return "Alive"

if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)

