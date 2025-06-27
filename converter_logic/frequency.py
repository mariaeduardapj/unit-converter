frequencies = ["Hz","kHz","MHz","GHz","THz","cps","rpm","bpm","fps"]
factors_to_hz = {
    "Hz": 1,
    "kHz": 10**3,
    "MHz": 10**6,
    "GHz": 10**9,
    "THz": 10**12,
    "cps": 1,
    "rpm": 1 / 60,
    "bpm": 1 / 60,
    "fps": 1
}
factors_from_hz = {
    "Hz": 1,
    "kHz": 1 / 10**3,
    "MHz": 1 / 10**6,
    "GHz": 1 / 10**9,
    "THz": 1 / 10**12,
    "cps": 1,
    "rpm": 60,
    "bpm": 60,
    "fps": 1
}
def convert_frequency(value,from_unit,to_unit):
    if from_unit not in factors_from_hz or to_unit not in factors_from_hz:
        raise ValueError("Invalid unit")
    value_in_hz = value * factors_to_hz[from_unit]
    return value_in_hz * factors_from_hz[to_unit]