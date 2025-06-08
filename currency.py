import requests

def currency_converter(f, to, value):
    url = f"https://api.exchangerate.host/convert?from={f}&to={to}&amount={value}"
    answer = requests.get(url)
    date = answer.json()
    return date["result"]

def run_currency_converter():
    currencies = ["USD", "EUR", "GBP", "JPY", "BRL", "CNY"]
    print(
        "Convert from:\n1 - US Dollar\n2 - Euro\n3 - Pound sterling\n4 - Japanese Yen\n5 - Brazilian Real\n6 - Chinese Yuan")
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
    print(f"{value} {f} -> {result:.2f} {to}")

