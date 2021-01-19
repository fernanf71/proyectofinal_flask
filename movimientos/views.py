from movimientos import app  # estoy importando el app del fichero __init__.py
from flask import render_template
import csv


@app.route('/')
def Movimientos():
    fMovimientos = open('movimientos/data/basededatos.csv', 'r')
    csvReader = csv.reader(fMovimientos, delimiter = ",", quotechar = '"')
    movimientos = list(csvReader)  #lo pasamos a lista para que jinja pueda trabajar.
    
    sumador = 0
    for movimiento in movimientos:
        sumador += float(movimiento[6])

    return render_template('listaMovimientos.html', datos=movimientos, total=sumador)  # render template es un método. Se va a ir a la carpeta template y busca el fichero listaMovimientos.html. Render_template trabaja junto (se lo pasa) a jinja2 que es un motor de plantillas. El nombre delante del igual es el que va a jinja

    #la única manera de meterle un boton a un formulario y que me redireccione (sin meterle javascript) es con un formulario.

@app.route('/purchase')
def compra():
    return 'Me he quedado aquí  '







