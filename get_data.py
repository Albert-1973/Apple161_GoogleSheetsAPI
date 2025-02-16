from flask import Flask, jsonify, request  # Добавили request для логирования
from flask_cors import CORS
import json
from google_sheets import read_data  # Импорт функции для чтения данных

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Разрешаем доступ всем

# Логирование всех запросов
@app.before_request
def log_request_info():
    print(f"Получен запрос: {request.method} {request.url}")
    print(f"Заголовки: {dict(request.headers)}")
    if request.data:
        print(f"Тело запроса: {request.data.decode('utf-8')}")

@app.route("/get_data", methods=["GET"])
def get_data():
    """Эндпоинт для получения всех данных из Google Sheets"""
    try:
        data = read_data()  # Читаем данные из таблицы
        return app.response_class(
            response=json.dumps({"data": data}, ensure_ascii=False, indent=4),
            status=200,
            mimetype="application/json"
        )
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route("/get_products", methods=["GET"])
def get_products():
    """Эндпоинт для получения только списка товаров"""
    try:
        data = read_data()  # Получаем данные из таблицы
        # Оставляем только товары (например, фильтруем по категории "Телефоны")
        products = [item for item in data if item.get("Category") == "Телефоны"]

        return app.response_class(
            response=json.dumps({"data": products}, ensure_ascii=False, indent=4),
            status=200,
            mimetype="application/json"
        )
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=10000)  # Используем Waitress

