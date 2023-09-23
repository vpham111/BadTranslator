from wtforms import SelectField, TextAreaField, SubmitField
from wtforms.validators import NoneOf, InputRequired
from flask_wtf import FlaskForm

class LanguageForm(FlaskForm):
    selectin = SelectField('Select Input Language', choices=[('Select', ''), ('es', 'Spanish'), ('fr', 'French'), ('de', 'German'), ('zh', 'Chinese'), ('en', 'English'), ('jp', 'Japanese'), ('kr', 'Korean'), ('vi', 'Vietnamese')])
    textin = TextAreaField('TextIn', validators=[InputRequired()])
    selectout = SelectField('Select Output Language', choices=[('Select', ''), ('es', 'Spanish'), ('fr', 'French'), ('de', 'German'), ('zh', 'Chinese'), ('en', 'English'), ('jp', 'Japanese'), ('kr', 'Vietnamese'), ('vi', 'Vietnamese')])
    textout = TextAreaField('TextOut')
    submit = SubmitField('Translate')
