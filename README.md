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
- Frequency (Units: Hz, kHz, MHz, GHz, THz, cps, rpm, bpm, fps)
- Custom (2 Variable conversor)

## 🛠️ Installation

- Python 3.10 or higher
- Flask

Install dependencies with:

```bash
pip install -r requirements.txt

## 📁 Project Structure

```bash
unit_converter/
├── app.py
├── requirements.txt
├── converter_logic/
│ ├── area.py
│ └── length.py
│ └── volume.py
│ └── weight.py
│ └── pressure.py
│ └── frequency.py
│ └── temperature.py
│ └── energy.py
│ └── digital_storage.py
│ └── number_bases.py
├── templates/
│ ├── index.html
│ ├── area.html
│ └── length.html
│ └── volume.html
│ └── weight.html
│ └── pressure.html
│ └── frequency.html
│ └── temperature.html
│ └── energy.html
│ └── digital_storage.html
│ └── number_bases.html
├── .gitignore           
└── README.md             

