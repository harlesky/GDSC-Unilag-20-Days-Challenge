from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Establish a connection to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Access the database
db = client["database"]

# Access the collection
collection = db["data"]

@app.route("/")
def hello_html():
    """Returns Hello GDSC in bold using HTML tags"""
    return f"<b>Hello GDSC</b>"

@app.route("/api/hello")
def hello_json():
    """Returns Hello GDSC in JSON format"""
    message = {"message": "Hello GDSC"}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
