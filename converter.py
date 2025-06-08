import requests
print("UNIT CONVERTER\n1 - Temperature Converter\n2 - Currency Converter")
try:
    unit = int(input("Choose an option - "))
except ValueError:
    print("Invalid option. Please, enter a number from 1 to 2.")
    exit()
#----------------------------------------------------------------
if unit == 1:
    print("TEMPERATURE CONVERTER\n1 - Celsius to Fahrenheit\n2 - Fahrenheit to Celsius\n3 - Celsius to Kelvin\n4 - Kelvin to Celsius\n5 - Fahrenheit to Kelvin\n6 - Kelvin to Fahrenheit")
    try:
        temp = int(input("Choose an option - "))
    except ValueError:
        print("Invalid option. Please, enter a number from 1 to 6.")
        exit()
    if temp == 1:
        celsius = float(input("Celsius - "))
        print(f"{celsius}°C -> {(9/5*celsius)+32:.1f}°F")
    elif temp == 2:
        fahrenheit = float(input("Fahrenheit - "))
        print(f"{fahrenheit}°F -> {5/9*(fahrenheit-32):.1f}°C")
    elif temp == 3:
        celsius = float(input("Celsius - "))
        print(f"{celsius}°C -> {celsius+273.15:.1f}K")
    elif temp == 4:
        kelvin = float(input("Kelvin - "))
        print(f"{kelvin}K -> {kelvin-273.15:.1f}°C")
    elif temp == 5:
        fahrenheit = float(input("Fahrenheit - "))
        print(f"{fahrenheit}°F -> {(5/9*(fahrenheit-32))+273.15:.1f}K")
    elif temp == 6:
        kelvin = float(input("Kelvin - "))
        print(f"{kelvin}K -> {(9/5*(kelvin-273.15))+32:.1f}°F")
    else:
        print("Invalid option.")
#--------------------------------------------------------------
elif unit == 2:
    def currency_converter(f, to, value):
        url = f"https://api.exchangerate.host/convert?from={f}&to={to}&amount={value}"
        answer = requests.get(url)
        date = answer.json()
        return date["result"]
    currencies = ["USD", "EUR", "GBP", "JPY", "BRL", "CNY"]
    print("Convert from:\n1 - US Dollar\n2 - Euro\n3 - Pound sterling\n4 - Japanese Yen\n5 - Brazilian Real\n6 - Chinese Yuan")
    try:
        x1 = int(input("Choose an option - "))
    except ValueError:
        print("Invalid option. Please, enter a number from 1 to 6.")
        exit()
    print("Convert to:\n1 - US Dollar\n2 - Euro\n3 - Pound sterling\n4 - Japanese Yen\n5 - Brazilian Real\n6 - Chinese Yuan")
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
    f = currencies[x1-1]
    to = currencies[x2-1]
    result = currency_converter(f,to,value)
    print(f"{value} {f} -> {result:.2f} {to}")


