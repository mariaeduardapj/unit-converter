def run_pressure_converter():
    pressures = ["Pa","kPa","MPa","bar","atm","mmHg","psi"]
    factors_to_pascal = {
        0: 1,       # Pa to Pa
        1: 10**3,   # kPa to Pa
        2: 10**6,   # MPa to Pa
        3: 10**5 ,  # bar to Pa
        4: 101.325, # atm to Pa
        5: 133.322, # mmHg to Pa
        6: 6894.76  # psi to Pa
    }
    factors_from_pascal = {
        0: 1,           # Pa to Pa
        1: 1 / 10**3,   # kPa to Pa
        2: 1 / 10**6,   # MPa to Pa
        3: 1 / 10**5 ,  # bar to Pa
        4: 1 / 101.325, # atm to Pa
        5: 1 / 133.322, # mmHg to Pa
        6: 1 / 6894.76  # psi to Pa
    }
    print("-=-=-=-=-=- PRESSURE CONVERTER -=-=-=-=-=-")
    print("MENU OPTIONS:\n1 - Pascal (Pa)      | 2 - Kilopascal (kPa)    | 3 - Megapascal (MPa)     | 4 - Bar (bar)\n5 - Atmosphere (atm) | 6 - Millimeter of Mercury (mmHg) | 7 - Pound per Square Inch (psi)")
    try:
        f = int(input("Convert from - "))
        if 1 > f > 7:
            print("Invalid option. Please choose a number between 1 and 7.")
    except ValueError:
        print("Invalid option. Please, enter a number from 1 to 7.")
        exit()
    try:
        t = int(input("To - "))
        if 1 > t > 7:
            print("Invalid option. Please choose a number between 1 and 7.")
    except ValueError:
        print("Invalid option. Please, enter a number from 1 to 7.")
        exit()
    try:
        value = float(input(f"Value in {pressures[f-1]} - "))
    except ValueError:
        print("Invalid value. Please enter a number.")
        exit()
    value_in_pascal = value * factors_to_pascal[f-1]
    converted_value = value_in_pascal * factors_from_pascal[t-1]
    print(f"{value} {pressures[f-1]} -> {converted_value} {pressures[t-1]}")