# 🔄 Unit Converter

A Python project that allows you to convert between various types of units.  

## ✅ Current Features

- Temperature conversion (Celsius, Fahrenheit, Kelvin)
- Currency conversion (real-time exchange rates via exchangerate.host)
- Length conversion (Units: km, hm, dam, m, dm, cm, mm)
- Time and duration conversion (Time units, day county and time zones)
- Volume (Units: km³, hm³, dam³, m³, dm³, cm³, mm³, kL, hL, daL, L, dL, cL, mL)
- Digital storage (Units: bytes, kb, mb, gb, tb, pb, eb, zb)
- Weight (Units: ton, kg, hg, dag, g, dg, cg, mg)
- Area (Units: km², hm², dam², m², dm², cm², mm²)
- Energy (Units: W, kW, J, kJ, cal, kcal, eV, BTU)
- Pressure (Units: Pa, kPa, MPa, bar, atm, mmHg, psi)

## 🛠️ Installation

Make sure you have Python 3.6 or higher.

1. Clone this repository  
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Planned Expansions

| Measurement | Digital / Math  | Time / Misc           |
|-------------|-----------------|-----------------------|
|             | 🧬 Frequency    | 🧳 Custom conversions |


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
├── weight.py          # Weight conversion logic
├── area.py            # Area conversion logic
├── energy.py          # Energy conversion logic
├── pressure.py        # Pressure conversion logic
├── requirements.txt   # Project dependencies
├── .gitignore         # Files ignored by Git
└── README.md          # Project documentation

