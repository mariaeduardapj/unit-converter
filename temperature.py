def run_temperature_converter():
    print(
        "TEMPERATURE CONVERTER\n1 - Celsius to Fahrenheit\n2 - Fahrenheit to Celsius\n3 - Celsius to Kelvin\n4 - Kelvin to Celsius\n5 - Fahrenheit to Kelvin\n6 - Kelvin to Fahrenheit")
    try:
        temp = int(input("Choose an option - "))
    except ValueError:
        print("Invalid option. Please, enter a number from 1 to 6.")
        exit()
    if temp == 1:
        celsius = float(input("Celsius - "))
        print(f"{celsius}°C -> {(9 / 5 * celsius) + 32:.1f}°F")
    elif temp == 2:
        fahrenheit = float(input("Fahrenheit - "))
        print(f"{fahrenheit}°F -> {5 / 9 * (fahrenheit - 32):.1f}°C")
    elif temp == 3:
        celsius = float(input("Celsius - "))
        print(f"{celsius}°C -> {celsius + 273.15:.1f}K")
    elif temp == 4:
        kelvin = float(input("Kelvin - "))
        print(f"{kelvin}K -> {kelvin - 273.15:.1f}°C")
    elif temp == 5:
        fahrenheit = float(input("Fahrenheit - "))
        print(f"{fahrenheit}°F -> {(5 / 9 * (fahrenheit - 32)) + 273.15:.1f}K")
    elif temp == 6:
        kelvin = float(input("Kelvin - "))
        print(f"{kelvin}K -> {(9 / 5 * (kelvin - 273.15)) + 32:.1f}°F")
    else:
        print("Invalid option.")