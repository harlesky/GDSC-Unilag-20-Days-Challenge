from flask import Flask, jsonify

app = Flask(__name__)

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
    app.run(debug=True)