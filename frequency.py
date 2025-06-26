def run_frequency_converter():
    frequencies = ["Hz","kHz","MHz","GHz","THz","cps","rpm","bpm","fps"]
    factors_to_hz = {
        0: 1,      # Hz to Hz
        1: 10**3,  # kHz to Hz
        2: 10**6,  # MHz to Hz
        3: 10**9,  # GHz to Hz
        4: 10**12, # THz to Hz
        5: 1,      # cps to Hz
        6: 1 / 60, # rpm to Hz
        7: 1 / 60, # bpm to Hz
        8: 1       # fps to Hz
    }
    factors_from_hz = {
        0: 1,          # Hz to Hz
        1: 1 / 10**3,  # Hz to kHz
        2: 1 / 10**6,  # Hz to MHz
        3: 1 / 10**9,  # Hz to GHz
        4: 1 / 10**12, # Hz to THz
        5: 1,          # Hz to cps
        6: 60,         # Hz to rpm
        7: 60,         # Hz to bpm
        8: 1           # Hz to fps
    }
    print("-=-=-=-=-=- FREQUENCY CONVERTER -=-=-=-=-=-")
    print("Menu options:\n1 - Hertz (Hz)       | 4 - Gigahertz (GHz)         | 7 - Revolutions Per Minute (rpm)\n2 - Kilohertz (kHz)  | 5 - Terahertz (THz)         | 8 - Beats Per Minute (bpm)\n3 - Megahertz (MHz)  | 6 - Cycles Per Second (cps) | 9 - Frames Per Second (fps)")
    try:
        f = int(input("Convert from - "))
        if f < 1 or f > 9:
            print("Invalid option. Please choose a number between 1 and 9.")
    except ValueError:
        print("Invalid option. Please, enter a number from 1 to 9.")
        exit()
    try:
        t = int(input("To - "))
        if t < 1 or t > 9:
            print("Invalid option. Please choose a number between 1 and 9.")
    except ValueError:
        print("Invalid option. Please, enter a number from 1 to 9.")
        exit()
    try:
        value = float(input(f"Value in {frequencies[f - 1]} - "))
    except ValueError:
        print("Invalid value. Please enter a number.")
        exit()
    value_in_hz = value * factors_to_hz[f - 1]
    converted_value = value_in_hz * factors_from_hz[t - 1]
    print(f"{value} {frequencies[f - 1]} -> {converted_value} {frequencies[t - 1]}")