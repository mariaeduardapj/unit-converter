from flask import Flask, render_template, request
from converter_logic.area import convert_area, areas
from converter_logic.length import convert_length, length
from converter_logic.volume import convert_volume, volumes
from converter_logic.weight import convert_weight, weights
from converter_logic.pressure import convert_pressure, pressures
from converter_logic.frequency import convert_frequency, frequencies
from converter_logic.temperature import convert_temperature, temperatures
from converter_logic.energy import convert_energy, energies
from converter_logic.digital_storage import convert_digital_storage, ds_units
from converter_logic.number_bases import convert_number_base, bases
from converter_logic.time_duration import (time_units, convert_time_unit, calculate_days_between, get_currency_time_in_zone, timezones)
from converter_logic.currency import currency_converter, currencies

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/area', methods=['GET', 'POST'])
def area():
    result = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            converted = convert_area(value, from_unit, to_unit)
            formatted = "{:.12f}".format(converted).rstrip('0').rstrip('.')
            result = f"{value} {from_unit} = {formatted} {to_unit}"
        except Exception as e:
            result = f"Erro: {e}"
    return render_template('area.html', result=result, areas=areas)

@app.route('/length', methods=['GET', 'POST'])
def length_converter():
    result = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            converted = convert_length(value, from_unit, to_unit)
            formatted = "{:.6f}".format(converted).rstrip('0').rstrip('.')
            result = f"{value} {from_unit} = {formatted} {to_unit}"
        except Exception as e:
            result = f"Erro: {e}"
    return render_template('length.html', result=result, length=length)

@app.route('/volume', methods=['GET', 'POST'])
def volume_converter():
    result = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            converted = convert_volume(value, from_unit, to_unit)
            formatted = "{:.15f}".format(converted).rstrip('0').rstrip('.')
            result = f"{value} {from_unit} = {formatted} {to_unit}"
        except Exception as e:
            result = f"Erro: {e}"
    return render_template('volume.html', result=result, volumes=volumes)

@app.route('/weight', methods=['GET', 'POST'])
def weight_converter():
    result = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            converted = convert_weight(value, from_unit, to_unit)
            formatted = "{:.6f}".format(converted).rstrip('0').rstrip('.')
            result = f"{value} {from_unit} = {formatted} {to_unit}"
        except Exception as e:
            result = f"Erro: {e}"
    return render_template('weight.html', result=result, weights=weights)

@app.route('/pressure', methods=['GET', 'POST'])
def pressure_converter():
    result = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            converted = convert_pressure(value, from_unit, to_unit)
            formatted = "{:.6f}".format(converted).rstrip('0').rstrip('.')
            result = f"{value} {from_unit} = {formatted} {to_unit}"
        except Exception as e:
            result = f"Erro: {e}"
    return render_template('pressure.html', result=result, pressures=pressures)

@app.route('/frequency', methods=['GET', 'POST'])
def frequency_converter():
    result = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            converted = convert_frequency(value, from_unit, to_unit)
            formatted = "{:.12f}".format(converted).rstrip('0').rstrip('.')
            result = f"{value} {from_unit} = {formatted} {to_unit}"
        except Exception as e:
            result = f"Erro: {e}"
    return render_template('frequency.html', result=result, frequencies=frequencies)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature_converter():
    result = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            converted = convert_temperature(value, from_unit, to_unit)
            formatted = "{:.2f}".format(converted).rstrip('0').rstrip('.')
            result = f"{value} {from_unit} = {formatted} {to_unit}"
        except Exception as e:
            result = f"Erro: {e}"
    return render_template('temperature.html', result=result, temperatures=temperatures)

@app.route('/energy', methods=['GET', 'POST'])
def energy_converter():
    result = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            converted = convert_energy(value, from_unit, to_unit)
            formatted = "{:.19f}".format(converted).rstrip('0').rstrip('.')
            result = f"{value} {from_unit} = {formatted} {to_unit}"
        except Exception as e:
            result = f"Erro: {e}"
    return render_template('energy.html', result=result, energies=energies)

@app.route('/digital_storage', methods=['GET', 'POST'])
def digital_storage_converter():
    result = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            converted = convert_digital_storage(value, from_unit, to_unit)
            formatted = "{:.7f}".format(converted).rstrip('0').rstrip('.')
            result = f"{value} {from_unit} = {formatted} {to_unit}"
        except Exception as e:
            result = f"Erro: {e}"
    return render_template('digital_storage.html', result=result, ds_units=ds_units)

@app.route('/number_bases', methods=['GET', 'POST'])
def number_bases_converter():
    result = None
    if request.method == 'POST':
        try:
            value = int(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            converted = convert_number_base(value, from_unit, to_unit)
            result = f"{value} {from_unit} = {converted} {to_unit}"
        except Exception as e:
            result = f"Erro: {e}"
    return render_template('number_bases.html', result=result, bases=bases)

@app.route('/time_duration', methods=['GET', 'POST'])
def time_duration_converter():
    result = None
    if request.method == 'POST':
        form_type = request.form.get('form_type')
        try:
            if form_type == 'convert_units':
                value = float(request.form['value'])
                from_unit = request.form['from_unit']
                to_unit = request.form['to_unit']
                converted = convert_time_unit(value, from_unit, to_unit)
                result = f"{value} {from_unit} = {converted:,.0f} {to_unit}"
            elif form_type == 'days_between':
                date1 = request.form['date1']
                date2 = request.form['date2']
                days = calculate_days_between(date1,date2)
                result = f"{days} day(s) between {date1} and {date2}"
            elif form_type == 'timezone':
                zone = request.form['zone']
                current_time = get_currency_time_in_zone(zone)
                result = f"Real time in {zone}: {current_time}"
        except Exception as e:
            result = f"Error: {e}"
    return render_template('time_duration.html', result=result, time_units=time_units, zones=list(timezones.keys()))

@app.route('/currency', methods=['GET', 'POST'])
def currency_converter_page():
    result = None
    if request.method == 'POST':
        try:
            from_currency = request.form['from_unit']
            to_currency = request.form['to_unit']
            value = float(request.form['value'])
            converted = currency_converter(from_currency,to_currency,value)
            result = f"{value} {from_currency} = {format(converted, '.2f')} {to_currency}"
        except Exception as e:
            result = f"Erro: {e}"
    return render_template('currency.html', result=result, currencies=currencies)

if __name__ == '__main__':
    app.run(debug=True)
