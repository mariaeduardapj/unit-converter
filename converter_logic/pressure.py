pressures = ["Pa","kPa","MPa","bar","atm","mmHg","psi"]
factors_to_pascal = {
    "Pa": 1,
    "kPa": 10**3,
    "MPa": 10**6,
    "bar": 10**5 ,
    "atm": 101.325,
    "mmHg": 133.322,
    "psi": 6894.76
}
factors_from_pascal = {
    "Pa": 1,
    "kPa": 1 / 10**3,
    "MPa": 1 / 10**6,
    "bar": 1 / 10**5 ,
    "atm": 1 / 101.325,
    "mmHg": 1 / 133.322,
    "psi": 1 / 6894.76
}
def convert_pressure(value, from_unit, to_unit):
    if from_unit not in factors_from_pascal or to_unit not in factors_from_pascal:
        raise ValueError("Invalid Unit")
    value_in_pascal = value * factors_to_pascal[from_unit]
    return value_in_pascal * factors_from_pascal[to_unit]
