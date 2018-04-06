from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return redirect("/signup")

def valid_email(email):
    if email != '':
        if email.count("@") != 1 or email.count(".") != 1 or not (2 < len(email) < 21):
            valid_email.error = 'Invalid email. must contain "@" and ".", must be 3-20 characters in length, no spaces.'
        else:
          valid_email.error = ''
    else:
        valid_email.error = ''

    return valid_email.error

    
def valid_usrnm(usrnm):
    if ' ' in usrnm or not (2 < len(usrnm) < 21):
        valid_usrnm.error = 'Invalid username, must be 3-20 characters in length, no spaces.'
    elif usrnm == '':
        valid_usrnm.error = 'Field required.'
    else:
        valid_usrnm.error = ''
    
    return valid_usrnm.error

def valid_psswrd(psswrd):
    if ' ' in psswrd or not (2 < len(psswrd) < 21):
        valid_psswrd.error = 'Invalid password, must be 3-20 characters in length, no spaces.'
    elif psswrd == '':
        valid_psswrd.error = 'Field required.'
    else:
        valid_psswrd.error = ''
    
    return valid_psswrd.error

def psswrd_match(psswrd, confirm):
    if psswrd == confirm:
        psswrd_match.error = ''
    else:
        psswrd_match.error = 'Passwords do not match.'

    return psswrd_match.error

@app.route("/signup")
def display_signup():
    template = jinja_env.get_template('signup_page.html')
    return template.render()

@app.route("/welcome")
def welcome_page():
    username = request.args.get('username')
    template = jinja_env.get_template('welcome_page.html')
    return template.render(username=username)

@app.route("/signup", methods=['POST'])
def validate_signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['psw']
    confirm_psw = request.form['psw-repeat']

    usrnm_error = valid_usrnm(username)
    email_error = valid_email(email)
    psw_error = valid_psswrd(password)
    confirm_error = psswrd_match(password, confirm_psw)

    if not usrnm_error and not email_error and not psw_error and not confirm_error:

        return redirect('/welcome?username={0}'.format(username))
    
    else:
        template = jinja_env.get_template('signup_page.html')

        return template.render(username=username, email=email, usrnm_error=usrnm_error, email_error=email_error, 
        psw_error=psw_error, confirm_error=confirm_error)
        

app.run()