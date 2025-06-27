frequencies = ["Hz","kHz","MHz","GHz","THz","cps","rpm","bpm","fps"]
factors_to_hz = {
    0: 1,      # Hz to Hz
    1: 10**3,  # kHz to Hz
    2: 10**6,  # MHz to Hz
    3: 10**9,  # GHz to Hz
    4: 10**12, # THz to Hz
    5: 1,      # cps to Hz
    6: 1 / 60, # rpm to Hz
    7: 1 / 60, # bpm to Hz
    8: 1       # fps to Hz
}
factors_from_hz = {
    0: 1,          # Hz to Hz
    1: 1 / 10**3,  # Hz to kHz
    2: 1 / 10**6,  # Hz to MHz
    3: 1 / 10**9,  # Hz to GHz
    4: 1 / 10**12, # Hz to THz
    5: 1,          # Hz to cps
    6: 60,         # Hz to rpm
    7: 60,         # Hz to bpm
    8: 1           # Hz to fps
}
def convert_frequency(value,from_unit,to_unit):
    if from_unit not in factors_from_hz or to_unit not in factors_from_hz:
        raise ValueError("Invalid unit")
    value_in_hz = value * factors_to_hz[from_unit]
    return value_in_hz * factors_from_hz[to_unit]