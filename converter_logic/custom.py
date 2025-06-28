operations = {
    "plus": lambda x, y: x + y,
    "minus": lambda x, y: x - y,
    "times": lambda x, y: x * y,
    "divided": lambda x, y: x / y if y != 0 else float("inf"),
    "raised": lambda x, y: x ** y,
}
def convert_custom(value, operator, number):
    if operator not in operations:
        raise ValueError("Invalid operator")
    return operations[operator](value, number)
