"""
Created at 23/10/16
__author__ = 'Sergio Padilla'

"""
from flask import Flask, render_template, request, redirect, url_for, session
import shelve
from Practica3.Forms.Register import RegistrationForm

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render('home.html')


read_file = open("credential", mode='r')
app.secret_key = str(read_file.readline().replace('\n', ''))
read_file.close()


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # Open shelve
        db = shelve.open('test-shelve.db', writeback=True)
        try:
            exist = db[form.username.data]
            if exist and len(exist) > 0:
                if exist['password'] == form.password.data:
                    session['username'] = form.username.data
                    return render_template('home.html', user=session['username'], register=True)
                else:
                    return render_template('register.html', form_register=form, error='Incorrect Password')
            else:
                db[form.username.data] = {'password': form.password.data, 'sites': []}
                session['username'] = form.username.data
                return render_template('home.html', user=session['username'])
        except KeyError:
            db[form.username.data] = {'password': form.password.data, 'sites': []}
            session['username'] = form.username.data
            return render_template('home.html', user=session['username'])
        finally:
            db.close()

    return render_template('register.html', form_register=form, register=True)


@app.route("/sites")
def sites():
    if 'username' in session:
        # Open shelve
        db = shelve.open('test-shelve.db', writeback=True)
        try:
            exist = db[session['username']]
            sites = exist['sites']
            return render_template('sites.html', user=session['username'], sites=sites)
        except KeyError:
            return render_template('sites.html', register=True)
        finally:
            db.close()
    else:
        return render_template('sites.html', register=True)


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/about')
def about():
    site_visited("about")
    return render('about.html')


@app.route('/contact')
def contact():
    site_visited("contact")
    return render('contact.html')


@app.route('/newsblog')
def newsblog():
    site_visited("newsblog")
    return render('newsblog.html')


@app.route('/surfbase')
def surfbase():
    site_visited("surfbase")
    return render('surfbase.html')


@app.route('/me', methods=['GET', 'POST'])
def personal():
    form = RegistrationForm(request.form)
    site_visited("me")
    if request.method == 'POST' and form.validate():
        # Open shelve
        db = shelve.open('test-shelve.db', writeback=True)
        try:
            exist = db[session['username']]
            if session['username'] == form.username.data:
                db[form.username.data] = {'password': form.password.data, 'sites': []}
                return render_template('personal.html', username=session['username'], password=form.password.data,
                                       form_register=form, user=session['username'])
            else:
                return render_template('personal.html', username=session['username'], password=exist['password'],
                                       form_register=form, error='Change username not allow', user=session['username'])
        finally:
            db.close()
    if 'username' in session:
        db = shelve.open('test-shelve.db', writeback=True)
        try:
            exist = db[session['username']]
            return render_template('personal.html', username=session['username'], password=exist['password'],
                                   form_register=form, user=session['username'])
        finally:
            db.close()

    return render('personal.html')


def site_visited(site):
    if 'username' in session:
        # Open shelve
        db = shelve.open('test-shelve.db', writeback=True)
        try:
            exist = db[session['username']]
            sites = exist['sites']
            if len(sites) < 3:
                sites.append(site)
            else:
                sites.pop(0)
                sites.append(site)
            exist['sites'] = sites
        finally:
            db.close()


def render(template):
    if 'username' in session:
        return render_template(template, user=session['username'])
    else:
        return render_template(template, register=True)


if __name__ == "__main__":
    app.run()
