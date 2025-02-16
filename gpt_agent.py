import requests

# URL вашего API на Render
API_URL = "https://apple161-googlesheetsapi.onrender.com/get_data"

def get_products():
    """Функция получает данные из API Render"""
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json().get("data", [])
        else:
            return f"Ошибка: {response.status_code}, {response.text}"
    except Exception as e:
        return f"Ошибка запроса: {str(e)}"
