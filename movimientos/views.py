from movimientos import app  # estoy importando el app del fichero __init__.py
from movimientos.forms import MovimientosForm
from flask import render_template, request, url_for, redirect
import csv, sqlite3
from datetime import datetime

DBFILE = app.config['DBFILE']
# Función consulta a base de datos:
def consulta(query, params=()):
    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()
    c.execute(query, params)
    conn.commit()
    filas = c.fetchall()
    conn.close()
    if len(filas) == 0:
        return filas
    columnNames = []
    for columnName in c.description:
        columnNames.append(columnName[0])
    listaDeDiccionarios = []
    for fila in filas:
        d = {}
        for ix, columnName in enumerate(columnNames):
            d[columnName] = fila[ix]
        listaDeDiccionarios.append(d)
    return listaDeDiccionarios
   
@app.route('/')
def Movimientos():
    
    movimientos = consulta ('SELECT fecha, hora, desde, q1, hacia, q2, pu FROM movimientos;')
    '''
    c.execute('SELECT fecha, hora, desde, q1, hacia, q2, pu FROM movimientos;')  # el resultado de la columna está en 'c'. El execute es como darle al play en el DB Browser

    movimientos = c.fetchall() # este es el método que me devuelve todos los registros. El fetchall me devuelve una lista de tuplas
    
    conn.close()
    '''
    return render_template('listaMovimientos.html', datos=movimientos)  # render template es un método. Se va a ir a la carpeta template y busca el fichero listaMovimientos.html. Render_template trabaja junto (se lo pasa) a jinja2 que es un motor de plantillas. El nombre delante del igual es el que va a jinja

    #la única manera de meterle un boton a un formulario y que me redireccione (sin meterle javascript) es con un formulario.
   
@app.route('/purchase', methods=['GET', 'POST'])

def compra():
    ahora = datetime.now()
    dia = ahora.date()
    hora = ahora.strftime('%H:%M:%S')

    form = MovimientosForm()
    
    if request.method == 'POST': # si es un GET no hace nada. Devuelve el template vacío, es decir, se va al return. Si es POST, puesto lo que se inidca debajo del IF
        # INSERT INTO movimientos (fecha, hora
        # , desde, q1, hacia, q2, pu) VALUES ("05-05-2019", "12:09", "EUR", 25000, "BTC", 3456, 36);
        
        
        consulta('INSERT INTO movimientos (fecha, hora, desde, q1, hacia, q2, pu) VALUES ( ?, ?, ?, ?, ?, ?, ?);',
            (
                dia,
                hora,
                form.desde.data,
                form.q1.data,
                form.hacia.data,
                form.q2.data,
                form.pu.data
            )
        )  # el resultado de la consulta está en 'c'. El execute es como darle al play en el DB Browser. El resultado es una tupla y en la tupla le metemos lo valores que queremos. La tupla se la estoy pasando como segundo parámetro a c.execute
        '''
        conn.commit() # cuando se hace una modificación en la BBDD siempre hay que hacer esto. Fija los cambios y no puede faltar esta instrucción. Se utiliza para el INSERT, UPDATE y DELETE.
        conn.close()
        '''
        return redirect(url_for('Movimientos', form=form))  # tambien se puede poner: return redirect('/')
        
        '''
        seleccionMonedas = form.desde ('SELECT DISTINCT desde FROM movimientos;')
        '''
    

    return render_template('compra.html', form=form)