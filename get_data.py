import os
import json
import gspread
from google.oauth2.service_account import Credentials
from flask import Flask, jsonify

# Инициализация Flask
app = Flask(__name__)

# Настройка пути к Google Sheets
SPREADSHEET_ID = "1gZV79trjzpC9MREgHeXd-wa8hEWlvciFk4iZRt--oVk"  # Укажите ID вашей Google Таблицы
RANGE_NAME = "Лист1!A1:D1000"  # Укажите диапазон ячеек, который вы хотите прочитать

# Задаем необходимые scope
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify({"data": "test data"})  # временный ответ для проверки
    try:
        # Получаем данные из переменных окружения
        credentials_json = {
            "type": os.getenv("GOOGLE_TYPE"),
    "project_id": os.getenv("GOOGLE_PROJECT_ID"),
    "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("GOOGLE_PRIVATE_KEY").replace("\\n", "\n"),
    "client_email": os.getenv("GOOGLE_CLIENT_EMAIL"),
    "client_id": os.getenv("GOOGLE_CLIENT_ID"),
    "auth_uri": os.getenv("GOOGLE_AUTH_URI"),
    "token_uri": os.getenv("GOOGLE_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("GOOGLE_AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("GOOGLE_CLIENT_X509_CERT_URL"),
        }

        # Авторизация через ключи
        creds = Credentials.from_service_account_info(credentials_json, scopes=SCOPES)
        client = gspread.authorize(creds)

        # Открываем таблицу и читаем данные
        sheet = client.open_by_key(SPREADSHEET_ID)
        worksheet = sheet.worksheet("Лист1")  # Укажите имя вашего листа
        data = worksheet.get(RANGE_NAME)

        # Возвращаем данные в JSON
        return jsonify({"status": "success", "data": data})

    except Exception as e:
        # Обрабатываем ошибки
        error_message = f"Ошибка при чтении данных из Google Sheets: {e}"
        return jsonify({"status": "error", "message": error_message})

if __name__ == '__main__':
    # Запуск Flask-приложения
    app.run(host='0.0.0.0', port=5000)