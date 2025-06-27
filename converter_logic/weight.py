weights = ["ton","kg","hg","dag","g","dg","cg","mg"]
factors_to_g = {
    "ton": 10**6,
    "kg": 10**3,
    "hg": 10**2,
    "dag": 10,
    "g": 1,
    "dg": 1 / 10,
    "cg": 1 / 10**2,
    "mg": 1 / 10**3
}
factors_from_g = {
    "ton": 1 / 10**6,
    "kg": 1 / 10**3,
    "hg": 1 / 10**2,
    "dag": 1 / 10,
    "g": 1,
    "dg": 10,
    "cg": 10**2,
    "mg": 10**3
}
def convert_weight(value, from_unit, to_unit):
    if from_unit not in factors_from_g or to_unit not in factors_from_g:
        raise ValueError("Invalid Unit")
    value_in_g = value * factors_to_g[from_unit]
    return value_in_g * factors_from_g[to_unit]
