from flask import Flask, Response
import json
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# Подключение к Google Sheets API
SERVICE_ACCOUNT_FILE = "service_account.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

# Открываем нужный лист (Лист2)
SPREADSHEET_ID = "1IgCoywkrGDi02C2WxFANPJIswbd5u43LI2pd845bClo"
sheet = client.open_by_key(SPREADSHEET_ID).worksheet("Лист2")

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        data = sheet.get_all_records()  
        json_data = json.dumps(data, ensure_ascii=False)  # 👈 Правильная кодировка JSON
        return Response(json_data, content_type="application/json; charset=utf-8")  # 👈 Исправленный возврат данных
    except Exception as e:
        error_message = json.dumps({"error": str(e)}, ensure_ascii=False)
        return Response(error_message, content_type="application/json; charset=utf-8", status=500)  

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
