from movimientos import app
import sqlite3

DBFILEUSERS = app.config['DBFILEUSERS']
def consultaUsuarios(query, params=()):
    conn = sqlite3.connect('movimientos/data/usuarios.db')
    c = conn.cursor()
    c.execute(query, params)
    conn.commit()
    filas = c.fetchall()
    conn.close()


    if len(filas) == 0:
        return filas #devuelve una lista vacía y no proceso el diccionario

    columnNames = []
    for columnName in c.description:  #estoy recorriendo la tupla. 
        columnNames.append(columnName[0])
    
    listaDeDiccionarios = []
    
    for fila in filas:
        d={}
        for ix, columnName in enumerate(columnNames):  #devuelve una tupla con la posición y el valor (0,'id'), (1,'concepto')
            d[columnName] = fila[ix]
        listaDeDiccionarios.append(d)
    
    return listaDeDiccionarios

def email():
    emails = consultaUsuarios('SELECT correo FROM usuarios;')
    correos = []
    for correo in emails:
        for x in correo:
            correos.append(correo[x])
    return correos