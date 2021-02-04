from movimientos import app
import sqlite3


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

datos = consulta('SELECT desde, q1, hacia, q2 FROM MOVIMIENTOS;')
def balance(listaMoneda):
    q1 = 0
    q2 = 0
    for dato in datos:
        if dato['hacia'] == listaMoneda:
            q2 += float(dato['q2'])
        elif dato['desde'] == listaMoneda:
            q1 -= float(dato['q1'])
    balance = q2 - q1
    return balance

def seleccionDesde():
    listaMonedas = ['BTC', 'ETH', 'XRP', 'LTC', 'BCH', 'BNB', 'USDT', 'EOS', 'BSV', 'XLM', 'ADA', 'TRX']
    monedas = {}

    for listaMoneda in listaMonedas:
        monedas[listaMoneda] = balance(listaMoneda)

    for clave in monedas:
        if float(monedas[clave]) <= 0:
            listaMonedas.remove(clave)

    listaMonedas.insert(0, 'EUR')
    return listaMonedas

def pepito():
    EURSaldo = 0
    for dato in datos:
        if dato['hacia'] == 'EUR':
            EURSaldo += dato['q2']
        elif dato['desde'] == 'EUR':
            EURSaldo -= dato['q1']
    return EURSaldo

def eurosInvertidos():
    EURInvertidos = 0
    for dato in datos:
        if dato['desde'] == 'EUR':
            EURInvertidos += dato['q1']
    return EURInvertidos

def valorActual():
    listaMonedas = ['BTC', 'ETH', 'XRP', 'LTC', 'BCH', 'BNB', 'USDT', 'EOS', 'BSV', 'XLM', 'ADA', 'TRX']
    monedasSaldo = {}

    for moneda in listaMonedas:
        monedasSaldo[moneda] = balance(moneda)
    return monedasSaldo






