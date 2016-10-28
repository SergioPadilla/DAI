"""
Created at 19/10/16
__author__ = 'Sergio Padilla'

"""
from flask import Flask, render_template, request, redirect, url_for, session
from Practica3.Forms.Register import RegistrationForm

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        session['username'] = form.username.data
        session['password'] = form.password.data
        session['sites'] = []
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
        return render_template('home.html', user=session['username'])
    else:
        return redirect(url_for('index'))


@app.route("/sites")
def sites():
    if 'sites' in session:
        return render_template('sites.html', user=session['username'], sites=session['sites'])
    else:
        return render_template('sites.html')


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


@app.route('/me')
def personal():
    site_visited("me")
    return render('personal.html')


def site_visited(site):
    if 'sites' in session:
        sites = session['sites']
        if len(sites) < 3:
            sites.append(site)
        else:
            sites.pop(0)
            sites.append(site)
        session['sites'] = sites


def render(template):
    if 'username' in session:
        return render_template(template, user=session['username'])
    else:
        return render_template(template)


if __name__ == "__main__":
    app.run()
