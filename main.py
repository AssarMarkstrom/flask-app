# -*- coding: utf-8 -*-
import secrets
from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

SECRET_KEY = secrets.token_urlsafe(16) 

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

bootstrap = Bootstrap5(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__': 
    app.run() 