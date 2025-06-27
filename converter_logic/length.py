length = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
factors_to_mm = {
    "km": 10 ** 6,
    "hm": 10 ** 5,
    "dam": 10 ** 4,
    "m": 10 ** 3,
    "dm": 10 ** 2,
    "cm": 10,
    "mm": 1
}
factors_from_mm = {
    "km": 1 / 10 ** 6,
    "hm": 1 / 10 ** 5,
    "dam": 1 / 10 ** 4,
    "m": 1 / 10 ** 3,
    "dm": 1 / 10 ** 2,
    "cm": 1 / 10,
    "mm": 1
}

def convert_length(value, from_unit, to_unit):
    if from_unit not in factors_to_mm or to_unit not in factors_from_mm:
        raise ValueError("Invalid Unit")
    value_in_mm = value * factors_to_mm[from_unit]
    return value_in_mm * factors_from_mm[to_unit]
