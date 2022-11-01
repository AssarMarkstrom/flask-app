from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap5(app)

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

@app.route("/")
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('base.html', form=form)

if __name__ == '__main__': 
    app.run() 