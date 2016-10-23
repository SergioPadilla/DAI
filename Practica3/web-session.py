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
    if request.method == 'POST' and form.validate():
        session['username'] = form.username.data
        session['password'] = form.password.data
        return redirect(url_for('login'))
    elif 'username' in session:
        return redirect(url_for('login'))
    else:
        return render_template('home.html', form=form)


read_file = open("credential", mode='r')
app.secret_key = str(read_file.readline().replace('\n', ''))
read_file.close()


@app.route("/login")
def login():
    if 'username' in session:
        user = User(session['username'], session['password'])
        return render_template('home.html', user=user.username)
    else:
        return redirect(url_for('index'))


@app.route("/sites")
def sites():
    return render_template('sites.html')


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/newsblog')
def newsblog():
    return render_template('newsblog.html')


@app.route('/surfbase')
def surfbase():
    return render_template('surfbase.html')


@app.route('/me')
def personal():
    return render_template('personal.html')


if __name__ == "__main__":
    app.run()
