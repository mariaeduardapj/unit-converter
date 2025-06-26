def run_number_bases_converter():
    bases = ["decimal","hexadecimal","octal","binary"]
    print("-=-=-=-=-=- NUMBER BASES CONVERTER -=-=-=-=-=-")
    print("Menu options:\n1 - Decimal | 2 - Hexadecimal | 3 - Octal | 4 - Binary")
    try:
        f = int(input("Converter from - "))
        if not (1 <= f <= 4):
            print("Invalid option. Please choose an option between 1 and 4.")
    except ValueError:
        print("Invalid option. Please enter a number from 1 to 4.")
        exit()
    try:
        t = int(input("To - "))
        if not (1 <= t <= 4):
            print("Invalid option. Please choose an option between 1 and 4.")
    except ValueError:
        print("Invalid option. Please enter a number from 1 to 4.")
        exit()
    try:
        value = input(f"Value in {bases[f-1]} - ")
    except ValueError:
        print("Invalid option. Please enter a int number.")
        exit()
    if f == 1:
        dec = int(value)
    elif f == 2:
        dec = int(value,16)
    elif f == 3:
        dec = int(value,8)
    elif f == 4:
        dec = int(value,2)
    if t == 1:
        print(f"{value} {bases[f-1]} -> {dec} {bases[t-1]}")
    elif t == 2:
        print(f"{value} {bases[f-1]} -> {hex(dec)[2:]} {bases[t-1]}")
    elif t == 3:
        print(f"{value} {bases[f-1]} -> {oct(dec)[2:]} {bases[t-1]}")
    elif t == 4:
        print(f"{value} {bases[f-1]} -> {bin(dec)[2:]} {bases[t-1]}")
