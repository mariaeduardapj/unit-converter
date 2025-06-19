def run_length_converter():
    print("-=-=-=-=-=- LENGTH CONVERTER -=-=-=-=-=-")
    length = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
    print("Menu options: 1 - km | 2 - hm | 3 - dam | 4 - m | 5 - dm | 6 - cm | 7 - mm")
    try:
        f = int(input("Converter from - "))
        if f < 1 or f > 7:
            print("Invalid option. Please choose a number between 1 and 7.")
            return
    except ValueError:
        print("Invalid option. Please, enter a number from 1 to 7.")
        exit()
    try:
        t = int(input("To - "))
        if t < 1 or t > 7:
            print("Invalid option. Please choose a number between 1 and 7.")
            return
    except ValueError:
        print("Invalid option. Please, enter a number from 1 to 7.")
        exit()
    v = float(input(f"Valor em {length[f-1]} - "))
    if f > t:
        x = v / 10**(f-t)
    elif f < t:
        x = v * 10**(t-f)
    elif f == t:
        x = v
    print(f"{v}{length[f-1]} -> {x}{length[t-1]}")
