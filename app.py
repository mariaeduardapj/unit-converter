from flask import Flask, render_template, request
from converter_logic.area import convert_area, areas
from converter_logic.length import convert_length, length
from converter_logic.volume import convert_volume, volumes
from converter_logic.weight import convert_weight, weights

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
            formatted = "{:.12f}".format(converted).rstrip('0').rstrip('.')
            result = f"{value} {from_unit} = {formatted} {to_unit}"
        except Exception as e:
            result = f"Erro: {e}"
    return render_template('weight.html', result=result, weights=weights)


if __name__ == '__main__':
    app.run(debug=True)
