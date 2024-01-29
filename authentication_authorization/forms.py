"""Forms for reviews"""

from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    """Register form"""

    username = StringField("Username", validators=[InputRequired(), Length(min=1, max=20)], render_kw={"class": "usernameForm"})
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6, max=55)], render_kw={"class": "passwordForm"})
    email = StringField("Email", validators=[InputRequired(), Length(max=50)], render_kw={"class": "emailForm"})
    first_name = StringField("First Name", validators=[InputRequired(), Length(max=30)], render_kw={"class": "firstNameForm"})
    last_name = StringField("Last Name", validators=[InputRequired(), Length(max=30)], render_kw={"class": "lastNameForm"})


class LoginForm(FlaskForm):
    """Login form for user"""

    username = StringField("Username", validators=[InputRequired(), Length(min=1, max=20)])   
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6, max=55)])


class FeedbackForm(FlaskForm):
    """Feedback form"""

    title = StringField("Title", validators=[InputRequired(), Length(max=100)])
    content = StringField("Content", validators=[InputRequired()])