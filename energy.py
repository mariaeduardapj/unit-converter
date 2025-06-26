def run_energy_converter():
    energies = ["W","kW","J","kJ","cal","kcal","eV","BTU"]
    factors_to_w = {
        0: 1,            # W to W
        1: 1000,         # kW to W
        2: 1,            # J/s to W
        3: 1000,         # kJ/s to W
        4: 4.184,        # cal/s to W
        5: 4184,         # kcal/s to W
        6: 1.602*10*-19, # eV/s to W
        7: 1055.06       # BTU/s to W
    }
    factors_from_w = {
        0: 1,                # W to W
        1: 1 / 1000,         # W to kW
        2: 1,                # W to J/s
        3: 1 / 1000,         # W to kJ/s
        4: 1 / 4.184,        # W to cal/s
        5: 1 / 4184,         # W to kcal/s
        6: 1 / 1.602*10*-19, # W to eV/s
        7: 1 / 1055.06       # W to BTU/s
    }
    print("MENU OPTIONS:\n1 - Watt (W)          | 2 - Kilowatt (kW)          | 3 - Joule/s (J/s)          | 4 - Kilojoule/s (kJ/s)\n5 - Calorie/s (cal/s) | 6 - Kilocalorie/s (kcal/s) | 7 - Electron-volt/s (eV/s) | 8 - British Thermal Unit/s (BTU/s)")
    try:
        f = int(input("Convert from - "))
        if not (1 <= f <= 8):
            print("Invalid option. Please choose a number between 1 and 8.")
            return
    except ValueError:
        print("Invalid option. Please, enter a number from 1 to 8.")
        exit()
    try:
        t = int(input("To - "))
        if not (1 <= t <= 8):
            print("Invalid option. Please choose a number between 1 and 8.")
            return
    except ValueError:
        print("Invalid option. Please, enter a number from 1 to 8.")
        exit()
    try:
        value = float(input(f"Value in {energies[f - 1]} - "))
    except ValueError:
        print("Invalid value. Please enter a number.")
        exit()
    value_in_w = value * factors_to_w[f - 1]
    converted_value = value_in_w * factors_from_w[t - 1]
    print(f"{value} {energies[f - 1]} -> {converted_value} {energies[t - 1]}")
