"""
Created at 23/10/16
__author__ = 'Sergio Padilla'

"""
from flask import Flask, render_template, request, redirect, url_for, session
import os
import shelve

from Practica3.Forms.Register import RegistrationForm
from Practica3.Utils.User import User

app = Flask(__name__)

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
TEMPLATES_DIR = os.path.join(SITE_ROOT, '/templates/')

user = None


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('home.html', register=True)


read_file = open("credential", mode='r')
app.secret_key = str(read_file.readline().replace('\n', ''))
read_file.close()


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        global user
        # Open shelve
        db = shelve.open('test-shelve.db', writeback=True)
        try:
            exist = db[form.username.data]
            if exist and len(exist) > 0:
                if exist == form.password.data:
                    user = User(form.username.data, form.password.data)
                    return render_template('home.html', user=user.username, register=True)
                else:
                    return render_template('register.html', form_register=form, error='Incorrect Password')
            else:
                db[form.username.data] = form.password.data
                db[form.username.data]['sites'] = []
                user = User(form.username.data, form.password.data)
                return render_template('home.html', user=user.username)
        except KeyError:
            db[form.username.data] = form.password.data
            db[form.username.data]['sites'] = []
            user = User(form.username.data, form.password.data)
            return render_template('home.html', user=user.username)
        finally:
            db.close()

    return render_template('register.html', form_register=form, register=True)


@app.route("/sites")
def sites():
    global user
    if user:
        # Open shelve
        db = shelve.open('test-shelve.db', writeback=True)
        try:
            sites = db[user.username]['sites']
            return render_template('sites.html', sites=sites, register=True)
        except KeyError:
            return render_template('sites.html', register=True)
        finally:
            db.close()
    else:
        return render_template('sites.html', register=True)


@app.route('/logout')
def logout():
    global user
    if user:
        # Open shelve
        db = shelve.open('test-shelve.db', writeback=True)
        try:
            db[user.username]
        finally:
            db.close()
    return redirect(url_for('index'))


@app.route('/about')
def about():
    if user:
        site_visited("about")
    return render_template('about.html', register=True)


@app.route('/contact')
def contact():
    if user:
        site_visited("contact")
    return render_template('contact.html', register=True)


@app.route('/newsblog')
def newsblog():
    if user:
        site_visited("newsblog")
    return render_template('newsblog.html', register=True)


@app.route('/surfbase')
def surfbase():
    if user:
        site_visited("surfbase")
    return render_template('surfbase.html', register=True)


@app.route('/me')
def personal():
    if user:
        site_visited("me")
    return render_template('personal.html', register=True)


def site_visited(site):
    global user
    # Open shelve
    db = shelve.open('test-shelve.db', writeback=True)
    try:
        sites = db[user.username]['sites']

        if sites:  # only for security
            if len(sites) < 3:
                sites.append(site)
            else:
                sites.pop(0)
                sites.append(site)

            db[user.username]['sites'] = sites
    finally:
        db.close()


if __name__ == "__main__":
    app.run()
