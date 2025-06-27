temperatures = ["°C","°F","K"]
factors_to_c = {
    "°C": lambda value: value,
    "°F": lambda value: (value - 32) * 5/9,
    "K": lambda value: value - 273.15
}
factors_from_c = {
    "°C": lambda value: value,
    "°F": lambda value: (value * 9/5) + 32,
    "K": lambda value: value + 273.15
}
def convert_temperature(value,from_unit,to_unit):
    if from_unit not in factors_from_c or to_unit not in factors_from_c:
        raise ValueError("Invalid unit")
    value_in_c = factors_to_c[from_unit](value)
    return factors_from_c[to_unit](value)