"""
Created at 19/10/16
__author__ = 'Sergio Padilla'

"""
from flask import Flask, render_template, request, redirect, url_for, session
import os

from Practica3.Forms.Register import RegistrationForm
from Practica3.Utils.User import User

app = Flask(__name__)

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
TEMPLATES_DIR = os.path.join(SITE_ROOT, '/templates/')

@app.route("/", methods=['GET', 'POST'])
def index():
    form = RegistrationForm(request.form)
    user = None
    if request.method == 'POST' and form.validate():
        session['username'] = form.username.data
        session['password'] = form.password.data
        user = User(form.username.data, form.password.data)
    elif 'username' in session:
        user = User(session['username'], session['password'])

    if user:
        return render_template('index.html', form=form, user=user.username)

    return render_template('index.html', form=form)


read_file = open("credential", mode='r')
app.secret_key = str(read_file.readline().replace('\n', ''))
read_file.close()


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
