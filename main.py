from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,length
from flask_bootstrap import Bootstrap

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class LoginForm(FlaskForm):
    email= StringField(label='Email', validators=[DataRequired(),Email(message="please enter a valid e-mail")])
    password= PasswordField(label='Password', validators=[DataRequired(),length(min=8, message="password must be atleast 8 characters")])
    submit= SubmitField(label='log in')

app = Flask(__name__)
bootstrap= Bootstrap(app)
app.secret_key= "some secret string"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["get","post"])
def login():
    login_form= LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data== "admin@email.com" and login_form.password.data== "12345678":
            return render_template('success.html')
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
