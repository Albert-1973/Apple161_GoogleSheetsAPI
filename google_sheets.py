import gspread
from google.oauth2.service_account import Credentials

# Подключение к Google Sheets через сервисный аккаунт
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = "service_account.json"  # Файл с ключами сервисного аккаунта

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

# ID таблицы (возьмите из ссылки)
SPREADSHEET_ID = "1IgCoywkrGDi02C2WxFANPJIswbd5u43LI2pd845bClo"

def read_data():
    """Читает данные из Google Sheets"""
    sheet = client.open_by_key(SPREADSHEET_ID).sheet1  # Открывает первый лист
    return sheet.get_all_records()  # Возвращает данные в виде списка словарей
