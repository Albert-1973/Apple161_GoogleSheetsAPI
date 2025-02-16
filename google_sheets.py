import gspread
import json
from google.oauth2.service_account import Credentials

# Подключение к Google Sheets через сервисный аккаунт
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = "service_account.json"  # Файл с ключами сервисного аккаунта

try:
    # Загружаем учетные данные
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)

    # ID таблицы (замените на свой)
    SPREADSHEET_ID = "1IgCoywkrGDi02C2WxFANPJIswbd5u43LI2pd845bClo"

    def read_data():
        """Читает данные из Google Sheets"""
        try:
            sheet = client.open_by_key(SPREADSHEET_ID).sheet1  # Открываем первый лист
            data = sheet.get_all_records()  # Получаем данные как список словарей
            
            # Вывод данных в консоль в читаемом формате
            print(json.dumps(data, ensure_ascii=False, indent=4))

            return data
        except Exception as e:
            print(f"Ошибка при чтении данных: {e}")
            return []

except Exception as e:
    print(f"Ошибка подключения к Google Sheets: {e}")
    
if __name__ == "__main__":
    print("Читаем данные из Google Sheets...")
    data = read_data()
    print("Полученные данные:", data)
