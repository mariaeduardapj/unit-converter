def run_length_converter():
    length = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
    factors_to_mm = {
        0: 10 ** 6, # km to mm
        1: 10 ** 5, # hm to mm
        2: 10 ** 4, # dam to mm
        3: 10 ** 3, # m to mm
        4: 10 ** 2, # dm to mm
        5: 10,      # cm to mm
        6: 1        # mm to mm
    }
    factors_from_mm = {
        0: 1 / 10 ** 6, # mm to km
        1: 1 / 10 ** 5, # mm to hm
        2: 1 / 10 ** 4, # mm to dam
        3: 1 / 10 ** 3, # mm to mm
        4: 1 / 10 ** 2, # mm to dm
        5: 1 / 10,      # mm to cm
        6: 1            # mm to mm
    }
    print("-=-=-=-=-=- LENGTH CONVERTER -=-=-=-=-=-")
    print("Menu options: 1 - km | 2 - hm | 3 - dam | 4 - m | 5 - dm | 6 - cm | 7 - mm")
    try:
        f = int(input("Converter from - "))
        if not (1 <= f <= 7):
            print("Invalid option. Please choose a number between 1 and 7.")
            return
    except ValueError:
        print("Invalid option. Please, enter a number from 1 to 7.")
        exit()
    try:
        t = int(input("To - "))
        if not (1 <= t <= 7):
            print("Invalid option. Please choose a number between 1 and 7.")
            return
    except ValueError:
        print("Invalid option. Please, enter a number from 1 to 7.")
        exit()
    value = float(input(f"Value in {length[f-1]} - "))
    value_in_mm = value * factors_to_mm[f-1]
    converted_value = value_in_mm * factors_from_mm[t-1]
    print(f"{value} {length[f-1]} -> {converted_value} {length[t-1]}")
