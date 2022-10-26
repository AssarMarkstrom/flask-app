from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
bootstrap = Bootstrap5(app)
"""
class MyForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(1, 20)])
"""
@app.route("/")
def index():
    return render_template("base.html")
if __name__ == '__main__': 
    app.run() 