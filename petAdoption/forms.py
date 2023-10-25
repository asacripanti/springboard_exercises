from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, NumberRange, Optional, URL

class addPetForm(FlaskForm):
    """Form for adding new pets to be adopted"""

    name = StringField("Pet Name", validators=[InputRequired(message="Please enter a name")])
    species = SelectField('Species',
    choices=[('porcupine', 'Porcupine'), ('cat', 'Cat'), ('dog', 'Dog')])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    notes = StringField('Notes', validators=[Optional()])


class editPetForm(FlaskForm):
    """Form for editing pet info"""

    photo_url = StringField('Photo URL', validators=[Optional(), URL()])    
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField('Available?')
