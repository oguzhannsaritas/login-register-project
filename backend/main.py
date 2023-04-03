from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Home Page"


@app.route("/login", methods=["GET", "POST"])
def login():
    return {"status": True, "message": "Logined"}, 200


if __name__ == "__main__":
    app.run(debug=True, port="5555")
