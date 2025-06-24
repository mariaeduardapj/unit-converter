def run_weight_converter():
    weights = ["ton","kg","hg","dag","g","dg","cg","mg"]
    print("-=-=-=-=-=- WEIGHT CONVERTER -=-=-=-=-=-")
    factors_to_g = {
        0: 10**6,
        1: 10**3,
        2: 10**2,
        3: 10,
        4: 1,
        5: 1 / 10,
        6: 1 / 10**2,
        7: 1 / 10**3
    }
    factors_from_g = {
        0: 1 / 10**6,
        1: 1 / 10**3,
        2: 1 / 10**2,
        3: 1 / 10,
        4: 1,
        5: 10,
        6: 10**2,
        7: 10**3
    }
    print("MENU OPTIONS:\n1 - Metric ton (t) | 2 - Kilogram (kg)  | 3 - Hectogram (hg) | 4 - Dekagram (dag) \n5 - Gram (g)       | 6 - Centigram (cg) | 7 - Decigram (dg)  | 8 - Miligram (mg)")
    try:
        f = int(input("Convert from - "))
        if 1 > f > 8:
            print("Invalid option. Please, choose a number between 1 and 8.")
            return
    except ValueError:
        print("Invalid option. Please, enter a number from 1 to 8.")
    try:
        t = int(input("To - "))
        if 1 > t > 8:
            print("Invalid option. Please, choose a number between 1 and 8.")
            return
    except ValueError:
        print("Invalid option. Please, enter a number from 1 to 8.")
    try:
        value = float(input(f"Value in {weights[f-1]} - "))
    except ValueError:
        print("Invalid option. Please, enter a number.")
    value_in_gram = value * factors_to_g[f-1]
    converted_value = value_in_gram * factors_from_g[t-1]
    print(f"{value} {weights[f-1]} -> {converted_value} {weights[t-1]}")