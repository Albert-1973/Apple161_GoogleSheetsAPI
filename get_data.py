from flask import Flask, jsonify
from google_sheets import read_data  # Импорт функции для чтения данных

app = Flask(__name__)

@app.route("/get_data", methods=["GET"])
def get_data():
    """Эндпоинт для получения данных из Google Sheets"""
    try:
        data = read_data()  # Читаем данные из таблицы
        return jsonify(data), 200  # Автоматически устанавливает `Content-Type: application/json`
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Дублируем эндпоинт с другим названием
@app.route("/get_products", methods=["GET"])
def get_products():
    """Эндпоинт для получения списка товаров"""
    return get_data()  # Просто вызываем существующую функцию

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
