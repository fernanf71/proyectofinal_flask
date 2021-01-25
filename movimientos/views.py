from movimientos import app  # estoy importando el app del fichero __init__.py
from movimientos.forms import MovimientosForm
from flask import render_template, request, url_for, redirect
import csv, sqlite3
from datetime import date

DBFILE=app.config['DBFILE']

def consulta(query, params=()): # hay veces que el params no mando nada, pues le pongo que sea una tupla vacía, por defecto.
    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()

    c.execute(query, params) # en las siguientes lineas vamos a convertir esta lista de tuplas en un diccionario. Para ello se usa c.description
    

    nombresColumnas =[]
    for nombreColumna in c.description:  # en nombrecolumna voy a tener la tupla de 7. Todos es explicado en el 2:10:49 del video de (241:53)
        nombresColumnas.append(nombreColumna[0])  #me crea una lista con los nombres de las columnas de la BBDD.
    
    listaDeDiccionarios = []
    filas = c.fetchall()

    for fila in filas:
        d = {}
        for ix, nombreColumna in enumerate(nombresColumnas):
            d[nombreColumna] = fila[ix]
        listaDeDiccionarios.append(d)

    conn.commit()
    conn.close()
    
    '''
    resultado = c.fetchall() #esto es una lista de tuplas que ha recueperado.¿Como hacer para que por cada registro me devuelva un diccionario?
    '''
    if len(listaDeDiccionarios) == 1:
        return listaDeDiccionarios[0]
    elif len(listaDeDiccionarios) == 0:
        return None
    else:
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

    form = MovimientosForm()

    listamonedas = ['EUR', 'BTC', 'ETH', 'XRP', 'LTC', 'BCH', 'BNB', 'USDT', 'EOS', 'BSV', 'XLM', 'ADA', 'TRX']
    if request.method == 'POST': # si es un GET no hace nada. Devuelve el template vacío, es decir, se va al return. Si es POST, puesto lo que se inidca debajo del IF
        # INSERT INTO movimientos (fecha, hora, desde, q1, hacia, q2, pu) VALUES ("05-05-2019", "12:09", "EUR", 25000, "BTC", 3456, 36);
        

        consulta('INSERT INTO movimientos (fecha, hora, desde, q1, hacia, q2, pu) VALUES ( ?, ?, ?, ?, ?, ?, ?);',
            (
                request.form.get('fecha'),
                request.form.get('hora'),
                request.form.get('desde'),
                float(request.form.get('q1')),
                request.form.get('hacia'),
                float(request.form.get('q2')),
                request.form.get('pu')
            )
        )  # el resultado de la consulta está en 'c'. El execute es como darle al play en el DB Browser. El resultado es una tupla y en la tupla le metemos lo valores que queremos. La tupla se la estoy pasando como segundo parámetro a c.execute
        '''
        conn.commit() # cuando se hace una modificación en la BBDD siempre hay que hacer esto. Fija los cambios y no puede faltar esta instrucción. Se utiliza para el INSERT, UPDATE y DELETE.
        conn.close()
        '''
        return redirect(url_for('Movimientos', form=form))  # tambien se puede poner: return redirect('/')
    return render_template('compra.html', listamonedas=listamonedas, form=form)