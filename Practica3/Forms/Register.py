"""
Created at 20/10/16
__author__ = 'Sergio Padilla'

"""
from wtforms import validators, StringField, Form, PasswordField


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')