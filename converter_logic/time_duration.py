from datetime import datetime
from zoneinfo import ZoneInfo
time_units = ["Year(s)","Month(s)","Day(s)","Hour(s)","Minute(s)","Second(s)"]
factors_to_seconds = {
    "Year(s)": 31104000,
    "Month(s)": 2592000,
    "Day(s)": 86400,
    "Hour(s)": 3600,
    "Minute(s)": 60,
    "Second(s)": 1
}
factors_from_seconds = {
    "Year(s)": 1 / 31104000,
    "Month(s)": 1 / 2592000,
    "Day(s)": 1 / 86400,
    "Hour(s)": 1 /3600,
    "Minute(s)": 1 / 60,
    "Second(s)": 1
}
timezones = {
    "São Paulo": ZoneInfo("America/Sao_Paulo"),
    "New York": ZoneInfo("America/New_York"),
    "Los Angeles": ZoneInfo("America/Los_Angeles"),
    "London": ZoneInfo("Europe/London"),
    "Paris": ZoneInfo("Europe/Paris"),
    "Tokyo": ZoneInfo("Asia/Tokyo"),
    "Dubai": ZoneInfo("Asia/Dubai"),
    "Cairo": ZoneInfo("Africa/Cairo"),
    "Sydney": ZoneInfo("Australia/Sydney")
}
def convert_time_unit(value,from_unit,to_unit):
    if from_unit not in factors_from_seconds or to_unit not in factors_from_seconds:
        raise ValueError("Invalid unit")
    value_in_seconds = value * factors_to_seconds[from_unit]
    return value_in_seconds * factors_from_seconds[to_unit]
def calculate_days_between(date1_str,date2_str):
    try:
        date1 = datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.strptime(date2_str, "%Y-%m-%d")
        return abs((date2-date1).days)
    except ValueError:
        raise ValueError("Invalid date format. Try YYYY-MM-DD")
def get_currency_time_in_zone(zone_name):
    if zone_name not in timezones:
        raise ValueError("Invalid time zone")
    now = datetime.now(timezones[zone_name])
    return now.strftime("%Y-%m-%d %H:%M")