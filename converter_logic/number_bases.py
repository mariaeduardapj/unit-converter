bases = ["decimal","hexadecimal","octal","binary"]
factors_to_decimal = {
    "decimal": lambda x: int(x, 10),
    "hexadecimal": lambda x: int(x, 16),
    "octal": lambda x: int(x, 8),
    "binary": lambda x: int(x, 2)
}
factors_from_decimal = {
    "decimal": lambda x: str(x),
    "hexadecimal": lambda x: hex(x)[2:],
    "octal": lambda x: oct(x)[2:],
    "binary": lambda x: bin(x)[2:]
}
def convert_number_base(value, from_base, to_base):
    value = str(value).strip()
    if from_base not in factors_to_decimal or to_base not in factors_from_decimal:
        raise ValueError("Invalid base")
    try:
        decimal = factors_to_decimal[from_base](value)
    except ValueError:
        raise ValueError(f"The value '{value}' is invalid for the base {from_base}.")
    return factors_from_decimal[to_base](decimal)