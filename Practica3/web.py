"""
Created at 19/10/16
__author__ = 'Sergio Padilla'

"""
from flask import Flask, render_template, request
import os

from Practica3.Forms.Register import RegistrationForm

app = Flask(__name__)

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
TEMPLATES_DIR = os.path.join(SITE_ROOT, '/templates/')

@app.route("/", methods=['GET', 'POST'])
def index():
    form = RegistrationForm(request.form)
    return render_template('index.html', form=form)


    # if request.method == 'POST' and form.validate():
    #     user = User(form.username.data, form.email.data,
    #                 form.password.data)
    #     db_session.add(user)
    #     flash('Thanks for registering')
    #     return redirect(url_for('login'))
    # return render_template('register.html', form=form)

if __name__ == "__main__":
    app.run()
