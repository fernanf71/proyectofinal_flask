from movimientos import app  # estoy importando el app del fichero __init__.py
from flask import render_template, request
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

@app.route('/purchase', methods=['GET', 'POST'])
def compra():
    if request.method == 'POST': # si es un GET no hace nada. Devuelve el template vacío, es decir, se va al return. Si es POST, puesto lo que se inidca debajo del IF
        print(request.form) # esto es un diccionario con las duplas de los datos completados en el formulario. Para pedirle solo la fecha le pones request.form('fecha'); pero lo que viaja es una cadena. Si está viajando un número lo tienes que convertir en un FLOAT


    return render_template('compra.html')







