from flask import Flask

from routes.index import blueprint

app= Flask(__name__)

app.register_blueprint(blueprint, url_prefix="/api/users")

if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)

