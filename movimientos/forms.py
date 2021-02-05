from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Length, ValidationError
from datetime import date
from movimientos.balance import*



listaMonedas = ['EUR', 'BTC', 'ETH', 'XRP', 'LTC', 'BCH', 'BNB', 'USDT', 'EOS', 'BSV', 'XLM', 'ADA', 'TRX']


def disponibilidadMonedas(form, field):
    disponibilidades = valorActual()
    for disponibilidad in disponibilidades:
        if disponibilidades[form.desde.data] < field.data:
                raise ValidationError('No tiene saldo suficiente')

def mismaMoneda(form, field):
    if form.desde.data == field.data:
        raise ValidationError('No puede realizar la operación con la misma moneda. Elija moneda distinta')


class MovimientosForm(FlaskForm):
    desde = SelectField('From', choices=listaMonedas)
    hacia = SelectField('To', choices=listaMonedas, validators=[DataRequired(), mismaMoneda])
    q1 = FloatField('Q', validators=[DataRequired(), disponibilidadMonedas ])
    q2 = FloatField('Q')
    pu = FloatField('P.U.')

    aceptar = SubmitField('Aceptar')
    cancelar = SubmitField('Cancelar')
    calc = SubmitField('Calcular')
    volver = SubmitField('Volver')

class Status(FlaskForm):
    invertido = FloatField('Invertido')
    valorActual = FloatField('Valor actual')
    volver = SubmitField('Volver')