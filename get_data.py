from flask import Flask, jsonify, request
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# Настройки доступа к Google Таблице
SERVICE_ACCOUNT_FILE = "service_account.json"
SPREADSHEET_ID = "1gZV79trjzpC9MREgHeXd-wa8hEWlvciFk4iZRt--oVk"

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scopes)
client = gspread.authorize(creds)
spreadsheet = client.open_by_key(SPREADSHEET_ID)

@app.route('/get_data', methods=['GET'])
def get_data():
    """
    Эндпоинт для получения всех данных из Google Таблицы.
    """
    worksheet = spreadsheet.sheet1  # Первый лист таблицы
    data = worksheet.get_all_records()  # Считываем все строки
    return jsonify(data)  # Возвращаем данные в формате JSON

@app.route('/get_row', methods=['GET'])
def get_row():
    """
    Эндпоинт для получения определенной строки по номеру.
    """
    row_number = int(request.args.get('row', 1))  # Получаем номер строки из параметра 'row'
    worksheet = spreadsheet.sheet1
    row_data = worksheet.row_values(row_number)
    return jsonify(row_data)

if __name__ == '__main__':
    app.run(port=5000)  # Запускаем API-сервер на порту 5000