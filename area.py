def run_area_converter():
    areas = ["km²", "hm²", "dam²", "m²", "dm²", "cm²", "mm²"]
    factors_to_mm = {
        0: 10**12, # km² to mm²
        1: 10**10, # hm² to mm²
        2: 10**8, # dam² to mm²
        3: 10**6, # m² to mm²
        4: 10**4, # dm² to mm²
        5: 10**2,    # cm² to mm²
        6: 1      # mm² to mm²
    }
    factors_from_mm = {
        0: 1 / 10**12, # mm² to km²
        1: 1 / 10**10, # mm² to hm²
        2: 1 / 10**8, # mm² to dam²
        3: 1 / 10**6, # mm² to m²
        4: 1 / 10**4, # mm² to dm²
        5: 1 / 10**2,    # mm² to cm²
        6: 1          # mm² to mm²
    }
    print("-=-=-=-=-=- AREA CONVERTER -=-=-=-=-=-")
    print("MENU OPTIONS:\n1 - km² | 2 - hm² | 3 - dam² | 4 - m² | 5 - dm² | 6 - cm² | 7 - mm²")
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
        value = float(input(f"Value in {areas[f-1]} - "))
    except ValueError:
        print("Invalid value. Please enter a number.")
        exit()
    value_in_mm = value * factors_to_mm[f-1]
    converted_value = value_in_mm * factors_from_mm[t-1]
    print(f"{value}{areas[f-1]} -> {converted_value}{areas[t-1]}")