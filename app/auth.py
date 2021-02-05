from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if loginVerified(email, password):
            return render_template("home.html")
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("home.html")

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        phone = request.form.get('phone')
        email = request.form.get('email')
        password = request.form.get('password')
        passwordConfirm = request.form.get('passwordConfirm')

        if signupVerified(fname, lname, phone, email, password, passwordConfirm):
            return render_template("login.html")
    return render_template("sign-up.html")

def loginVerified(email, password):
    return False

def signupVerified(fname, lname, phone, email, password, passwordConfirm):
    return False