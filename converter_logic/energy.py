energies = ["W","kW","J","kJ","cal","kcal","eV","BTU"]
factors_to_w = {
    "W": 1,
    "kW": 1000,
    "J": 1,
    "kJ": 1000,
    "cal": 4.184,
    "kcal": 4184,
    "eV": 1.602*10*-19,
    "BTU": 1055.06
}
factors_from_w = {
    "W": 1,
    "kW": 1 / 1000,
    "J": 1,
    "kJ": 1 / 1000,
    "cal": 1 / 4.184,
    "kcal": 1 / 4184,
    "eV": 1 / 1.602*10*-19,
    "BTU": 1 / 1055.06
}
def convert_energy(value,from_unit,to_unit):
    if from_unit not in factors_from_w or to_unit not in factors_to_w:
        raise ValueError("Invalid unit")
    value_in_w = value * factors_to_w[from_unit]
    return value_in_w * factors_from_w[to_unit]
