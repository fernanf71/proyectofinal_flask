from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Length


class MovimientosForm(FlaskForm):
    q1 = FloatField('Q', validators=[DataRequired()])
    q2 = FloatField('Q', validators=[DataRequired()])

    submit = SubmitField('Aceptar')
    calc = SubmitField('Calcular')
      