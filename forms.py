from wtforms import SelectField, TextAreaField, SubmitField
from wtforms.validators import NoneOf
from flask_wtf import FlaskForm

class LanguageForm(FlaskForm):
    selectin = SelectField('Select Input Language', validators=[NoneOf('Select')], choices=[('Select', ''), ('Spanish', 'Spanish'), ('French', 'French'), ('German', 'German'), ('Chinese', 'Chinese'), ('English', 'English'), ('Japanese', 'Japanese')])
    textin = TextAreaField('TextIn')
    selectout = SelectField('Select Output Language', validators=[NoneOf('Select')], choices=[('Select', ''), ('Spanish', 'Spanish'), ('French', 'French'), ('German', 'German'), ('Chinese', 'Chinese'), ('English', 'English'), ('Japanese', 'Japanese')])
    textout = TextAreaField('TextOut')
    submit = SubmitField('Translate')
