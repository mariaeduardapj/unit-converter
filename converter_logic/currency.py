import requests
from dotenv import load_dotenv
import os
currencies = ["USD", "EUR", "GBP", "JPY", "BRL", "CNY"]

def currency_converter(f, to, value):
    load_dotenv()
    access_key = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?from={f}&to={to}&amount={value}"
    headers = {"apikey": access_key}
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if "result" in data:
            return data["result"]
        else:
            raise ValueError("Unexpected response from API.")
    except Exception as e:
        raise ConnectionError(f"Failed to connect to the API: {e}")
