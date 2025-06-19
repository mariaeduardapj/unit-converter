ds_units = ["byte","KB","MB","GB","TB","PB","EB","ZB"]
factors_to_byte = {
    0: 1,       # byte to byte
    1: 1024,    # kb to byte
    2: 1024**2, # mb to byte
    3: 1024**3, # gb to byte
    4: 1024**4, # tb to byte
    5: 1024**5, # pb to byte
    6: 1024**6, # eb to byte
    7: 1024**7, # zb to byte
}
factors_from_bytes = {
    0: 1,             # byte from byte
    1: 1 / 1024,      # byte from kb
    2: 1 / (1024**2), # byte from mb
    3: 1 / (1024**3), # byte from gb
    4: 1 / (1024**4), # byte from tb
    5: 1 / (1024**5), # byte from pb
    6: 1 / (1024**6), # byte from eb
    7: 1 / (1024**7), # byte from zb
}
print("Menu options:\n1 - Byte          | 2 - Kilobyte (KB) | 3 - Megabyte (MB) | 4 - Gigabyte (GB)\n5 - Terabyte (TB) | 6 - Petabyte (PB) | 7 - Exabyte (EB)  | 8 - Zettabyte (ZB)")
try:
    f = int(input("Converter from - "))
    if 1 > f > 8:
        print("Invalid option. Please choose a number from 1 to 8.")
except ValueError:
    print("Invalid option. Please enter a number between 1 and 8.")
    exit()
try:
    t = int(input("To - "))
    if 1 > t > 8:
        print("Invalid option. Please choose a number from 1 to 8.")
except ValueError:
    print("Invalid option. Please enter a number between 1 and 8.")
    exit()
try:
    value = float(input(f"Value in {ds_units[f-1]} - "))
except ValueError:
    print("Invalid option. Please enter a number.")
    exit()
value_in_bytes = value * factors_to_byte[f-1]
converted_value = value_in_bytes * factors_from_bytes[t-1]
print(f"{value} {ds_units[f-1]} -> {converted_value} {ds_units[t-1]}")
