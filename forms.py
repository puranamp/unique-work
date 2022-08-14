from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class RoutineForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    routine = TextAreaField("What is your routine?",
                            validators=[DataRequired()])
    submit = SubmitField('Submit')
