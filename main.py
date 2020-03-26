from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import nbc

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'



class ReusableForm(Form):
    x = TextField('x:', validators=[validators.required()])
    y = TextField('y:', validators=[validators.required()])
    z = TextField('z:', validators=[validators.required()])


def checkValidation(var):
    try:
        val = int(var)
        return val
    except ValueError:
        return None

@app.route("/", methods=['GET', 'POST'])
def home():
    form = ReusableForm(request.form)

    print (form.errors)
    if request.method == 'POST':
        x = checkValidation(request.form['x'])
        y = checkValidation(request.form['y'])
        z = checkValidation(request.form['z'])
        if x == None or y == None or z == None:
            return render_template('home.html', form=form, status=False)
            
    sms = ''
    if form.validate():
        sms = nbc.predictClass(x, y, z)
    
    return render_template('home.html', form=form, message=sms, status=True)
    
    

if __name__ == "__main__":
    app.run(debug=True)
