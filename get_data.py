from flask import Flask, jsonify
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# Подключение к Google Sheets
SERVICE_ACCOUNT_FILE = "service_account.json"  # Убедись, что этот файл загружен в Render
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

# ID таблицы Google Sheets
SPREADSHEET_ID = "1IgCoywkrGDi02C2WxFANPJIswbd5u43LI2pd845bClo"
SHEET_NAME = "Лист2"  # Убедись, что лист действительно называется "Лист2"

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)
        data = sheet.get_all_records()

        # Фильтрация товаров по наличию
        filtered_data = [row for row in data if row.get("наличие") and row["наличие"].lower() != "нет"]

        if not filtered_data:
            return jsonify({"message": "К сожалению, в наличии сейчас ничего нет."})

        return jsonify(filtered_data)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
