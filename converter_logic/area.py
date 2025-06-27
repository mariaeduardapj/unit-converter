areas = ["km²", "hm²", "dam²", "m²", "dm²", "cm²", "mm²"]
factors_to_mm = {
    "km²": 10**12,
    "hm²": 10**10,
    "dam²": 10**8,
    "m²": 10**6,
    "dm²": 10**4,
    "cm²": 10**2,
    "mm²": 1
}
factors_from_mm = {
    "km²": 1 / 10**12,
    "hm²": 1 / 10**10,
    "dam²": 1 / 10**8,
    "m²": 1 / 10**6,
    "dm²": 1 / 10**4,
    "cm²": 1 / 10**2,
    "mm²": 1
}
def convert_area(value, from_unit, to_unit):
    if from_unit not in factors_from_mm or to_unit not in factors_from_mm:
        raise ValueError("Invalid Unit")
    value_in_mm = value * factors_to_mm[from_unit]
    return value_in_mm * factors_from_mm[to_unit]