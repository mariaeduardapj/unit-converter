# 🔄 Unit Converter

A Python project that allows you to convert between various types of units.  

## ✅ Current Features

- Temperature conversion (Celsius, Fahrenheit, Kelvin)
- Currency conversion (real-time exchange rates via exchangerate.host)
- Length conversion (Metric units - km, hm, dam, m, dm, cm, mm)

## 🛠️ Installation

Make sure you have Python 3.6 or higher.

1. Clone this repository  
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Planned Expansions

| Measurement | Digital / Math       | Time / Misc           |
|-------------|----------------------|-----------------------|
| 📦 Volume   | 🧮 Number bases      | ⏱️ Time & duration    |
| 📐 Area     | 📶 Digital storage   | 🌍 Time zones         |
| 🧊 Pressure | 🔋 Energy & power    | 🧳 Custom conversions |
| ⚖️ Weight   | 🧬 Frequency         | 💰 More currencies    |


## 📁 Project Structure

```bash
unit_converter/
├── main.py            # Main menu and logic dispatcher
├── temperature.py     # Temperature conversion logic
├── currency.py        # Currency conversion logic
├── requirements.txt   # Project dependencies
├── .gitignore         # Files ignored by Git
└── README.md          # Project documentation

