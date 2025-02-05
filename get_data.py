import os
from google.oauth2.service_account import Credentials
import gspread

# Чтение ключей из переменных окружения
credentials_dict = {
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
creds = Credentials.from_service_account_info(credentials_dict)
client = gspread.authorize(creds)

# Пример использования: чтение данных из Google Sheets
def fetch_sheet_data(sheet_name, worksheet_index=0):
    try:
        sheet = client.open(sheet_name).get_worksheet(worksheet_index)  # Открываем Google Sheet
        data = sheet.get_all_records()  # Получаем все строки в виде списка словарей
        return data
    except Exception as e:
        print(f"Ошибка при чтении данных из Google Sheets: {e}")
        return None

# Тест: замените "Название таблицы" на имя вашей Google таблицы
if __name__ == "__main__":
    sheet_name = "тест"
    data = fetch_sheet_data(sheet_name)
    if data:
        print(data)
