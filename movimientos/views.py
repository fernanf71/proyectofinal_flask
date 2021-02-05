from movimientos import app  # estoy importando el app del fichero __init__.py
from movimientos.forms import MovimientosForm, Status
from flask import render_template, request, url_for, redirect
from datetime import datetime
from movimientos.api import*
from movimientos.balance import*


@app.route('/')
def Movimientos():
    mensajes= []
    
    try:
        movimientos = consulta('SELECT fecha, hora, desde, q1, hacia, q2, pu FROM movimientos;')
    except Exception as e:
        print("**ERROR**: Acceso a la base de datos -movimientos: {} {}". format(type(e).__name__, e))
        mensajes.append('Error en acceso a base de datos. Consulte con el administrador')

        return render_template('listaMovimientos.html', mensajes=mensajes)
    
    return render_template('listaMovimientos.html', datos=movimientos, mensajes=[])  # render template es un método. Se va a ir a la carpeta template y busca el fichero listaMovimientos.html. Render_template trabaja junto (se lo pasa) a jinja2 que es un motor de plantillas. El nombre delante del igual es el que va a jinja

    #la única manera de meterle un boton a un formulario y que me redireccione (sin meterle javascript) es con un formulario.

@app.route('/purchase', methods=['GET', 'POST'])
def compra():
    mensajes= []
    interruptor = False
    ahora = datetime.now()
    dia = ahora.date()
    hora = ahora.strftime('%H:%M:%S')

    form = MovimientosForm()

    try:
        form.desde.choices= seleccionDesde()
        saldoMonedas = valorActual()
    except Exception as e:
        print("**ERROR**: Acceso a la base de datos -compra cryptos: {} {}". format(type(e).__name__, e))
        mensajes.append('Error en acceso a base de datos. Consulte con el administrador')
        return render_template('compra.html', form=form)
        
    if request.method == 'POST': # si es un GET no hace nada. Devuelve el template vacío, es decir, se va al return. Si es POST, puesto lo que se inidca debajo del IF
        # INSERT INTO movimientos (fecha, hora
        # , desde, q1, hacia, q2, pu) VALUES ("05-05-2019", "12:09", "EUR", 25000, "BTC", 3456, 36);
        
        if form.calc.data == True:
            interruptor = True
                
            try:
                peticion = exchange(form.desde.data, form.q1.data, form.hacia.data)
            except Exception as e:
                print("**ERROR**: Error llamada API -compra_API: {} {}". format(type(e).__name__, e))
                mensajes.append('Error en acceso a base de datos. Consulte con el administrador')
                return render_template('compra.html', form=form, interruptor=True, mensajes=mensajes)

            unitPrice = round(peticion/form.q1.data, 8)


            form.q2.data = peticion
            form.pu.data = unitPrice

            return render_template('compra.html', form=form, interruptor=True, mensajes=[])

        elif form.aceptar.data == True:
            try:
                consulta('INSERT INTO movimientos (fecha, hora, desde, q1, hacia, q2, pu) VALUES ( ?, ?, ?, ?, ?, ?, ?);',
                    (
                        dia,
                        hora,
                        form.desde.data,
                        form.q1.data,
                        form.hacia.data,
                        form.q2.data,
                        form.pu.data,
                    
                    )
                )  # el resultado de la consulta está en 'c'. El execute es como darle al play en el DB Browser. El resultado es una tupla y en la tupla le metemos lo valores que queremos. La tupla se la estoy pasando como segundo parámetro a c.execute
                return redirect(url_for('Movimientos', form=form))  # tambien se puede poner: return redirect('/')
            except Exception as e:
                print("**ERROR**: Acceso a la base de datos -insert: {} {}". format(type(e).__name__, e))
                mensajes.append('Error en acceso a base de datos. Consulte con el administrador')
                return render_template('compra.html', form=form, mensajes=mensajes)

    return render_template('compra.html', form=form, interruptor=interruptor, mensajes=mensajes)

@app.route('/status')
def status():
    mensajes= []
    form = Status()

    try:

        saldoEuros =saldoEuros()
        totalEuros =eurosInvertidos()
        valorActual = EURexchange()

    except Exception as e:
        print("**ERROR**: Acceso a la base de datos -status: {} {}". format(type(e).__name__, e))
        mensajes.append('Error en acceso a base de datos. Consulte con el administrador')
        return render_template('status.html', form=form, mensajes=mensajes)

    form.invertido.data = totalEuros
    form.valorActual.data = totalEuros + saldoEuros + valorActual

    return render_template('status.html', form=form, mensajes=mensajes)