from datetime import datetime
from zoneinfo import ZoneInfo
def run_time_duration_converter():
    print("-=-=-=-=-=- TIME & DURATION -=-=-=-=-=-")
    print("Function menu\n1 - Convert time units | 2 - How many days | 3 - Time zone")
    try:
        func = int(input("> "))
        if not (1 <= func <= 3):
            raise ValueError("Invalid input. Please enter a number from 1 to 3.")
    except ValueError as e:
        print(f"Error: {e}")
        exit()
    print()
    if func == 1:
        print("-=-=-=-=-=- CONVERT TIME UNITS -=-=-=-=-=-")
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
    elif func == 2:
        print("-=-=-=-=-=- HOW MANY DAYS -=-=-=-=-=-")
        try:
            d1 = input("First date (DD-MM-AAAA) - ")
            date1 = datetime.strptime(d1,"%d-%m-%Y")
            d2 = input("Second date (DD-MM-AAAA) - ")
            date2 = datetime.strptime(d2, "%d-%m-%Y")
            difference = abs(date2 - date1)
            print(f"There are \033[1;31m{difference.days}\033[0m days between these dates.")
        except ValueError:
            print("Invalid input. Please, enter a date in the format DD-MM-AAAA (example: 31-12-2023).")
        except Exception as e:
            print(f"Error {e}")
            exit()
    elif func == 3:
        print("-=-=-=-=-=- TIME ZONE -=-=-=-=-=-")
        zones = [ZoneInfo("America/Sao_Paulo"), ZoneInfo("America/New_York"), ZoneInfo("America/Los_Angeles"), ZoneInfo("Europe/London"), ZoneInfo("Europe/Paris"), ZoneInfo("Asia/Tokyo"), ZoneInfo("Asia/Dubai"), ZoneInfo("Africa/Cairo"), ZoneInfo("Australia/Sydney"),]
        z = ["São Paulo","New York","Los Angeles","London","Paris","Tokyo","Dubai","Cairo","Sydney"]
        print("Time now in...\n1 - São Paulo [Brazil] | 2 - New York [EUA] | 3 - Los Angeles [EUA]\n4 - London [England]   | 5 - Paris [France] | 6 - Tokyo [Japan]\n7 - Dubai [UAE]        | 8 - Cairo [Egypt]  | 9 - Sydney [Australia]")
        try:
            zone = int(input("> "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")
            exit()
        now = datetime.now(zones[zone - 1])
        formatted = now.strftime("%Y-%m-%d %H:%M")
        print(f"Time zone in {z[zone - 1]}: {formatted}")
    else:
        print("Invalid option.")
