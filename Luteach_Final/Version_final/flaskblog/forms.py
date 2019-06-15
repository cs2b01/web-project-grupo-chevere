from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed


class FormDeRegistros(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=9, max=9)])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different ')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different ')


class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
        email = StringField('Email', validators=[DataRequired(), Email()])
        picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'gif'])])
        submit = SubmitField('Update')

        def validate_username(self, username):
            if username.data != current_user.username:
                user = User.query.filter_by(username=username.data).first()
                if user:
                    raise ValidationError('That username is taken. Please choose a different ')

        def validate_email(self, email):
            if email.data != current_user.email:
                user = User.query.filter_by(email=email.data).first()
                if user:
                    raise ValidationError('That email is taken. Please choose a different ')


class LearnForm(FlaskForm):
   tema = StringField('Tema', validators=[DataRequired(), Length(min=2, max=20)])
   curso = StringField('Curso', validators=[DataRequired(), Length(min=2, max=20)])
   lugar = StringField('Lugar', validators=[DataRequired(), Length(min=2, max=20)])
   fecha = StringField('Fecha', validators=[DataRequired(), Length( max=10)])
   hora = StringField('Hora', validators=[DataRequired(), Length(max=4)])
   alumnos = StringField('Alumnos', validators=[DataRequired(), Length(max=8)])
   tiempo = StringField('Tiempo', validators=[DataRequired(), Length(max=1)])
   submit = SubmitField('Enviar')

class TeachForm(FlaskForm):
   name = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=20)])
   last_name = StringField('Apellido', validators=[DataRequired(), Length(min=2, max=20)])
   address = StringField('Direccion', validators=[DataRequired(), Length(min=2, max=20)])
   fecha = StringField('Fecha', validators=[DataRequired(), Length( max=10)])
   curso = StringField('Curso', validators=[DataRequired(), Length(max=4)])
   submit = SubmitField('Enviar')
