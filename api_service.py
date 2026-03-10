from flask import Flask, jsonify

app = Flask(__name__)

data = [
    {"id": 1, "amount": 200},
    {"id": 2, "amount": 350},
    {"id": 3, "amount": 500}
]

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(data)

@app.route("/total", methods=["GET"])
def total_amount():
    total = sum(item["amount"] for item in data)
    return jsonify({"total_amount": total})

if __name__ == "__main__":
    app.run(debug=True)
