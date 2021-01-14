from flask import Flask
import json

app = Flask(__name__)

@app.route("/api/hello", methods=["GET"])
def hello_world():
    return json.dumps(['Hello World!']), 200


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
