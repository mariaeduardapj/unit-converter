volumes = ["km³", "hm³", "dam³", "m³", "dm³", "cm³", "mm³", "kL", "hL", "daL", "L", "dL", "cL", "mL"]
factors_to_ml = {
    "km³": 10**15,
    "hm³": 10**12,
    "dam³": 10**9,
    "m³": 10**6,
    "dm³": 10**3,
    "cm³": 1,
    "mm³": 10**(-3),
    "kL": 10**6,
    "hL": 10**5,
    "daL": 10**4,
    "L": 10**3,
    "dL": 10**2,
    "cL": 10**1,
    "mL": 1
}
factors_from_ml = {
    "km³": 1 / 10 ** 15,
    "hm³": 1 / 10 ** 12,
    "dam³": 1 / 10 ** 9,
    "m³": 1 / 10 ** 6,
    "dm³": 1 / 10 ** 3,
    "cm³": 1,
    "mm³": 1 / 10 ** (-3),
    "kL": 1 / 10 ** 6,
    "hL": 1 / 10 ** 5,
    "daL": 1 / 10 ** 4,
    "L": 1 / 10 ** 3,
    "dL": 1 / 10 ** 2,
    "cL": 1 / 10 ** 1,
    "mL": 1
}
def convert_volume(value, from_unit, to_unit):
    if from_unit not in factors_to_ml or to_unit not in factors_from_ml:
        raise ValueError("Invalid Unit")
    value_in_ml = value * factors_to_ml[from_unit]
    return value_in_ml * factors_from_ml[to_unit]