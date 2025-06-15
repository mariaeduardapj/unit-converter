x = ["Year(s)","Month(s)","Day(s)","Hour(s)","Minute(s)","Second(s)"]
factors_to_seconds = {
    0: 31104000, # Year(s) to seconds
    1: 2592000,  # Month(s) to seconds
    2: 86400,    # Day(s) to seconds
    3: 3600,     # Hour(s) to seconds
    4: 60,       # Minute(s) to seconds
    5: 1         # Second(s) to seconds
}
factors_from_seconds = {
    0: 1 / 31104000, # Seconds to year(s)
    1: 1 / 2592000,  # Seconds to month(s)
    2: 1 / 86400,    # Seconds to day(s)
    3: 1 /3600,      # Seconds to hour(s)
    4: 1 / 60,       # Seconds to minute(s)
    5: 1             # Seconds to second(s)
}
print("Convert from:\n1 - Year | 2 - Month | 3 - Day | 4 - Hour | 5 - Minute | 6 - Seconds")
try:
    f = int(input("> "))
    if not (1 <= f <= 6):
        raise ValueError("Invalid input. Please enter a number from 1 to 6.")
except ValueError as e:
    print(f"Error: {e}")
    exit()
print("Convert to:\n1 - Year | 2 - Month | 3 - Day | 4 - Hour | 5 - Minute | 6 - Seconds")
try:
    t = int(input("> "))
    if not (1 <= t <= 6):
        raise ValueError("Invalid input. Please enter a number from 1 to 6.")
except ValueError as e:
    print(f"Error: {e}")
    exit()
try:
    value = float(input(f"{x[f - 1]} - "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()
value_in_seconds = value * factors_to_seconds[f-1]
converted_value = value_in_seconds * factors_from_seconds[t-1]
print(f"{value} {x[f-1]} -> {converted_value} {x[t-1]}")