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
    if "@" in email and 2 < len(email) < 21:
        return True
    else:
        return False
def valid_usrnm(usrnm):
    if ' ' in usrnm or 2 < len(usrnm) < 21 or usrnm == '':
        return False
    else:
        return True
def valid_psswrd(psswrd):
    if ' ' in psswrd or 2 < len(psswrd) < 21 or psswrd == '':
        return False
    else:
        return True
def psswrd_match(psswrd, repeat):
    if psswrd == repeat:
        return True
    else:
        return False

@app.route("/signup")
def display_signup():
    template = jinja_env.get_template('signup_page.html')
    return template.render()
app.run()