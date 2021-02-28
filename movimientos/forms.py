from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange, Email
from datetime import date
from movimientos.balance import valorActual
from movimientos.usuarios import email

listaMonedas = ['EUR', 'BTC', 'ETH', 'XRP', 'LTC', 'BCH', 'BNB', 'USDT', 'EOS', 'BSV', 'XLM', 'ADA', 'TRX']

def disponibilidadMonedas(form, field):
    disponibilidades = valorActual()
    if form.desde.data != 'EUR':
        if disponibilidades[form.desde.data] < field.data:
            raise ValidationError('No tiene saldo suficiente')

def mismaMoneda(form, field):
    if form.desde.data == field.data:
        raise ValidationError('No puede realizar la operación con las mismas monedas. Elija monedas distintas')

def mismoEmail(form, field):
    correoElectronico = email()
    print('***CORREO***', correoElectronico)
    if field.data in correoElectronico:
            raise ValidationError('La dirección de correo eléctronico ya ha sido registrada')

class MovimientosForm(FlaskForm):
    desde = SelectField('From', choices=listaMonedas)
    hacia = SelectField('To', choices=listaMonedas, validators=[DataRequired(), mismaMoneda ])
    q1 = FloatField('Cantidad From:', validators=[NumberRange(min=0.00000001, max=10000000000, message='La cantidad de ser mayor a cero y menor o igual a 10000000000 '), DataRequired(message='Debe introducir valor numérico'), disponibilidadMonedas ])
    q2 = FloatField('Cantidad To:')
    pu = FloatField('Precio unitario')

    aceptar = SubmitField('Aceptar')
    calc = SubmitField("Calcular")
    volver = SubmitField('Volver')

class Status(FlaskForm):
    valorEurosActualCryptos = FloatField('Valor euros actual cryptos')
    eurosAtrapadosInversion = FloatField('Euros atrapados en inversión')
    valorActual = FloatField('Valor actual')
    volver = SubmitField('Volver')

class Registro(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(), mismoEmail ])
    registrar = SubmitField('Registrar')