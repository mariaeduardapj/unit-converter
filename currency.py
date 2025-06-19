import requests
from dotenv import load_dotenv
import os

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
            print("Error: unexpected response from API.")
            print("Response:", data)
            return None
    except Exception as e:
        print("Failed to connect to the API:", e)
        return None


def run_currency_converter():
    currencies = ["USD", "EUR", "GBP", "JPY", "BRL", "CNY"]
    print("-=-=-=-=-=- CURRENCY CONVERTER -=-=-=-=-=-")
    print("Convert from:\n1 - US Dollar\n2 - Euro\n3 - Pound sterling\n4 - Japanese Yen\n5 - Brazilian Real\n6 - Chinese Yuan")
    try:
        x1 = int(input("Choose an option - "))
    except ValueError:
        print("Invalid option. Please, enter a number from 1 to 6.")
        exit()
    print(
        "Convert to:\n1 - US Dollar\n2 - Euro\n3 - Pound sterling\n4 - Japanese Yen\n5 - Brazilian Real\n6 - Chinese Yuan")
    try:
        x2 = int(input("Choose an option - "))
    except ValueError:
        print("Invalid option. Please, enter a number from 1 to 6.")
        exit()
    try:
        value = float(input("Value for conversion - "))
    except ValueError:
        print("Invalid option. Please, enter a number.")
        exit()
    f = currencies[x1 - 1]
    to = currencies[x2 - 1]
    result = currency_converter(f, to, value)
    if result is not None:
        print(f"{value} {f} -> {result:.2f} {to}")
    else:
        print("Conversion failed.")
