from flask import render_template
from flask import Flask, request, redirect, session, flash, url_for
import usuarios

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', titulo="Home")
@app.route('/atv-metas')
def atv_metas():
    return render_template('atv_metas.html', titulo='Atividades')
@app.route('/login')
def site_login():
    return render_template('login.html', titulo="login")
app.run(debug=True)
