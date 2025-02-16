from flask import Flask, jsonify
from google_sheets import read_data

app = Flask(__name__)

@app.route("/get_data", methods=["GET"])
def get_data():
    """Эндпоинт для получения данных из Google Sheets"""
    try:
        data = read_data()
        return jsonify({"data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
