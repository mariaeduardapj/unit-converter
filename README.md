# 🔄 Unit Converter

A Python project that allows you to convert between various types of units.  

## ✅ Current Features

- Temperature conversion (Celsius, Fahrenheit, Kelvin)
- Currency conversion (real-time exchange rates via exchangerate.host)
- Length conversion (Metric units - km, hm, dam, m, dm, cm, mm)
- Time and duration conversion (Time units, day county and time zones)
- Volume (Volume units - km³, hm³, dam³, m³, dm³, cm³, mm³, kL, hL, daL, L, dL, cL, mL)
- Digital storage (bytes, kb, mb, gb, tb, pb, eb, zb)

## 🛠️ Installation

Make sure you have Python 3.6 or higher.

1. Clone this repository  
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Planned Expansions

| Measurement   | Digital / Math    | Time / Misc           |
|---------------|-------------------|-----------------------|
| 📐 Area       | 🔋 Energy & power | 🧳 Custom conversions |
| 🧊 Pressure   | 🧬 Frequency      |
| ⚖️ Weight     |


## 📁 Project Structure

```bash
unit_converter/
├── main.py            # Main menu and logic dispatcher
├── temperature.py     # Temperature conversion logic
├── currency.py        # Currency conversion logic
├── length.py          # Length conversion logic
├── time_duration.py   # Time and duration conversion logic
├── volume.py          # Volume conversion logic
├── digital_storage.py # Digital storage conversion logic
├── requirements.txt   # Project dependencies
├── .gitignore         # Files ignored by Git
└── README.md          # Project documentation

