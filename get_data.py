from flask import Flask, jsonify
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# Подключение к Google Sheets API
SERVICE_ACCOUNT_FILE = "service_account.json"  # Файл с ключом (должен быть загружен в Render)
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

# Указанный ID твоей таблицы
SPREADSHEET_ID = "1IgCoywkrGDi02C2WxFANPJIswbd5u43LI2pd845bClo"
sheet = client.open_by_key(SPREADSHEET_ID).sheet1  # Первый лист

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        data = sheet.get_all_records()  # Читаем данные из таблицы
        return jsonify(data), 200, {'Content-Type': 'application/json; charset=utf-8'}  # Исправили кодировку
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Если произошла ошибка

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
