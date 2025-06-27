ds_units = ["byte","KB","MB","GB","TB","PB","EB","ZB"]
factors_to_byte = {
    "byte": 1,
    "KB": 1024,
    "MB": 1024**2,
    "GB": 1024**3,
    "TB": 1024**4,
    "PB": 1024**5,
    "EB": 1024**6,
    "ZB": 1024**7,
}
factors_from_bytes = {
    "byte": 1,
    "KB": 1 / 1024,
    "MB": 1 / (1024**2),
    "GB": 1 / (1024**3),
    "TB": 1 / (1024**4),
    "PB": 1 / (1024**5),
    "EB": 1 / (1024**6),
    "ZB": 1 / (1024**7),
}
def convert_digital_storage(value,from_unit,to_unit):
    if from_unit not in factors_from_bytes or to_unit not in factors_from_bytes:
        raise ValueError("Invalid unit")
    value_in_bytes = value * factors_to_byte[from_unit]
    return value_in_bytes * factors_from_bytes[to_unit]

